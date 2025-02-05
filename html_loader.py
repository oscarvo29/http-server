
class HtmlLoader:
    html_base_file_directory: str

    def __init__(self, html_dir: str = "./html/"):
        self.html_base_file_directory = self.__sanitizePath(html_dir)

    def have_extension(self, filename: str, extension: str) -> bool:
        return True if extension in filename else False

    def __sanitizePath(self, path: str) -> str:
        output = ""
        if not (path.startswith("./") or path.startswith("../")):
            output = "./"

        return output + path.rstrip("/") + "/"


    def setHTMLDir(self, base_dir: str) -> str:
        self.html_base_file_directory = self.__sanitizePath(base_dir)

    def html(self,filename: str) -> str:
        output = ""
        extenstion = ".html"

        if not self.have_extension(filename, extenstion):
            output = filename + extenstion
        else:
            output = filename
        try:
            
            with open(f"./html/{output}", "r") as file:
                return file.read()
        except:
            print("Couldn't find the file")
