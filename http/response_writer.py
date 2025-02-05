from .status_codes import format_status_code
from utils.time import get_formatted_time
from html_loader import HtmlLoader


class HeaderBuilder:
    http_version: str
    header_lines: list[str]
    line_end: str 
    status_line: str
    conent_length: str

    def __init__(self):
        self.header_lines = []
        self.http_version = "HTTP/1.1"
        self.line_end = "\r\n"

    def set_status_code(self, status_code: int):
        self.status_line = format_status_code(status_code)
        line = f"{self.http_version} {self.status_line}"
        self.header_lines.append(line)
        
    def set_content_type(self, content_type: str):
        line = f"Content-Type: {content_type}"
        self.header_lines.append(line)
        
    def set_content_length(self, content_length: str):
        line = f"Content-Length: {content_length}"
        self.conent_length = content_length
        self.header_lines.append(line)


    def set_time(self):
        now = get_formatted_time()
        self.header_lines.append(now)


    def write_header(self) -> str:
        header = ""
        for line in self.header_lines:
            header = header + line + self.line_end
        return header + self.line_end


class ResponseWriter:
    header: HeaderBuilder
    body: str
    html_loader: HtmlLoader
    
    def __init__(self, html_loader: HtmlLoader):
        self.header = HeaderBuilder()
        self.html_loader = html_loader

    def write(self, content: str, status_code: int, content_type: str ="text/plain"):
        self.header.set_status_code(status_code) 
        self.header.set_content_length(len(content))
        self.header.set_content_type(f"{content_type} ISO-8859-1")
        
        header_response = self.header.write_header()

        response = header_response + content
        return response
    
    def writeHtml(self, html_file: str, status_code: int) -> tuple[str, str, str]:
        body = self.html_loader.html(html_file)
        self.header.set_status_code(status_code) 
        self.header.set_content_length(str(len(body)))
        self.header.set_content_type("text/html ISO-8859-1")
        
        header_response = self.header.write_header()

        response = header_response + body
        return response, self.header.status_line, self.header.conent_length



        




