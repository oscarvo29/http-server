from utils import request_utils
from router import Router
from http.response_writer import ResponseWriter
import socket

class Server:
    routes: dict
    addr: list[str, int]

    def __init__(self, routes: Router, addr = ("", 8080)):
        self.addr = addr
        self.routes = routes.Routes()

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
            print(request_header)
            if req in self.routes.keys():
                print(self.routes[req])
                fn = self.routes[req]
                rw = ResponseWriter()

                res_header = fn(rw)
                print(f"Response: {res_header}")
                client_socket.send(res_header.encode())
               



