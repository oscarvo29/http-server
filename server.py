from utils import request_utils
from router import Router
from http.response_writer import ResponseWriter
from html_loader import HtmlLoader
from logger import TrafficLogger
import socket
import http.status_codes

class Server:
    routes: dict
    addr: list[str, int]
    html_loader: HtmlLoader
    _traffic_logger: TrafficLogger
    log_traffic: bool

    def __init__(self, routes: Router, addr = ("", 8080), html_dir: str = "./html/", log_traffic: bool = False):
        self.addr = addr
        self.routes = routes.Routes()
        self.html_loader = HtmlLoader(html_dir)
        self.log_traffic = log_traffic
        self._traffic_logger = TrafficLogger() 

    def logTraffic(self, log: bool):
        self.log_traffic = log

    def serve(self):
        if len(self.routes) <= 0:
            print("No routes registered.")
            return

        server = socket.create_server(self.addr, family= socket.AF_INET6)
        server.listen(0)
        print(f"Server is running on PORT: {self.addr[1]}")
        while True:
            client_socket, client_address = server.accept()
            client_request = client_socket.recv(2048).decode("utf-8")
            request_header = request_utils.translate_request(client_request)
            req = f"{request_header["method"]}:{request_header["path"]}"

            if req in self.routes.keys():
                fn = self.routes[req]
                rw = ResponseWriter(self.html_loader)
                response, status, length = fn(rw)
                
                if self.log_traffic:
                    self._traffic_logger.logTraffic(client_address[0], request_header["method"], request_header["path"], status, length)

                client_socket.send(response.encode())
            elif request_header["path"] == "/favicon.ico":
                pass
            else:
                if request_header["method"] == "GET":
                    rw = ResponseWriter(self.html_loader)

                    response, status, length = rw.writeHtml("404", status_code=404)
                    if self.log_traffic:
                        self._traffic_logger.logTraffic(client_address[0], request_header["method"], request_header["path"], status, length)
                        
                    client_socket.send(response.encode())



               



