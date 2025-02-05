import logging
import time
from logging import Formatter

class SingleTonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]

class TrafficLogger(metaclass=SingleTonMeta):
    _logger = None

    def Setup(self, filename: str = "http-server.log"):
        """
        Setup sets up the logger if the logger is not set all ready.

        :param p1: sets the filename of of the desired log.
        """
        if self._logger == None:
            format_string = '%(client_ip)s - - [%(asctime)s +0000] "%(method)s %(url)s HTTP/1.1" %(status)s %(size)s'
            apache_format = Formatter(format_string, "%d/%b/%Y:%H:%M:%S")
            self._logger = logging.getLogger("traffic")
            file_handler = logging.FileHandler(filename)
            file_handler.setFormatter(apache_format)
            if not self._logger.hasHandlers():
                self._logger.addHandler(file_handler)

    def log(self, client_ip: str, http_method: str, request_uri: str, status_msg: str, size: str, level=logging.INFO):
        """
        logs outgoing server traffic.
        If the logger is not setup, it will setup before logging.

        :param p1: destination ip - string
        :param p2: HTTP method - string
        :param p3: Request URI - string
        :param p4: The status code + the msg - string
        :param p5: Size of the payload - string
        :param p5: level of the logging value. Default to logging.INFO - int
        """


        if not self._logger:
             self.Setup()
        info = {
            "client_ip": client_ip,
            "method": http_method,
            "url": request_uri,
            "status": status_msg,
            "size": size
        }

        self._logger.log(level=level, msg="", extra=info) 
        


class Log(metaclass=SingleTonMeta):
    """
    Class Log. Singleton logger class, for logging in the console.
    """

    _logger = None

    def Setup(self):
        """
        Setup sets up the logger if the logger is not set all ready.
        
        """
        if self._logger == None:
            self._logger = logging.getLogger("app")
            self._logger.setLevel(logging.DEBUG)
            console_handler = logging.StreamHandler()
            console_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
            console_handler.setFormatter(console_format)
            
            self._logger.addHandler(console_handler)

    def info(self, msg: str):
        """
        info writes a info level debug console message.
        :param p1: is the desired message to be printed to the console.
        """

        if not self._logger:
            self.Setup()
        self._logger.info(msg)

    def debug(self, msg: str):
        """
        debug writes a debug level debug console message.
        :param p1: is the desired message to be printed to the console.
        """

        if not self._logger:
            self.Setup()
        self._logger.debug(msg)

    def error(self, msg: str):
        """
        error writes a error level debug console message.
        :param p1: is the desired message to be printed to the console.
        """

        if not self._logger:
            self.Setup()
        self._logger.error(msg)

    def critical(self, msg: str):
        """
        critical writes a critical level debug console message.
        :param p1: is the desired message to be printed to the console.
        """

        if not self._logger:
            self.Setup()
        self._logger.critical(msg)