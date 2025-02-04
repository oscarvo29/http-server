
from http.status_codes import *
from server import Server
from router import Router
from http.response_writer import *


"""
    Todo:
        - Add Apache style logger
        - Handle Errors
            * Error page
        - Html_loader 
        - ResponseWrite.write_html()

"""


def index(w: ResponseWriter):
    return w.write("<h1>Hallo, World</h1>", OK, content_type="text/html")
def about(w: ResponseWriter):
    return w.write("<h1>Hallo, From About Page</h1>", OK, content_type="text/html")

def main():
    router = Router()
    router.GET("/", index)
    router.GET("/about", about)

    s = Server(router)

    s.serve()



if __name__ == "__main__":
    main()