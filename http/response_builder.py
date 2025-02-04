import time
from status_codes import format_status_code

class HeaderResponseBuilder:
    response = ""
    lines: list[str]
    required_fields = [
        "status code",
        "date",
        "content-length",

                       ]

    http_version: str
    status_code: int
    status_code_formatted: str
    date: time
    content_length: str
    content_type: str

    def __init__(self, http_version: str = "HTTP/1.1"):
        self.http_version = http_version
    
    def set_status_code(self, status_code: int):
        

        self.status_code_formatted = format_status_code(status_code)
        self.status_code = status_code

    def set_time(self, response_time: time):
        self.date = response_time

    def set_content_length(self, content_length: str):
        self.content_length = content_length

    def set_content_type(self, type: str, charset: str = "charset=ISO-8859-1"):
        self.content_type = f"{type} {charset}"
        