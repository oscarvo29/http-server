
from http.status_codes import *
from server import Server
from router import Router
from http.response_writer import *

def index(w: ResponseWriter):
    return w.writeHtml("index", OK)
    
def about(w: ResponseWriter):
    return w.writeHtml("about", OK)

def main():
    router = Router()
    router.GET("/", index)
    router.GET("/about", about)

    s = Server(router, log_traffic=True)
    s.logTraffic(True)
    s.serve()



if __name__ == "__main__":
    main()