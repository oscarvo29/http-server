from typing import Callable

# Registers the HTTP Method, the URL + the function to be called.
class Router:
    url_prefix: str = ""
    routes = {}

    def GET(self, url: str, fn: Callable):
        key = f"GET:{self.url_prefix}{url}"
        self.routes[key] = fn

    def POST(self, url: str, fn: Callable):
        key = f"POST:{self.url_prefix}{url}"
        self.routes[key] = fn

    # Adds a prefix, for a group of routes.
    # "GET:/user/profile", "POST:/user/login" ...
    def Group(self, url_group: str, func: Callable):
        prev_prefix = self.url_prefix
        self.url_prefix = url_group
        func(self)
        self.url_prefix = prev_prefix

    def Routes(self) -> dict:
        return self.routes