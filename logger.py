import logging


class SingleTonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]

class Log(metaclass=SingleTonMeta):
    _logger = None

    def Setup(self, filename: str = "http-server.log", level = logging.INFO):
        if self._logger == None:
            self._logger = logging.getLogger()
        
        logging.basicConfig(filename=filename, level=level)
    
    def info(self, log: str):
        self._logger.info(log)
    
    def critical(self, log: str):
        self._logger.critical(log)
    
    def error(self, log: str):
        self._logger.error(log)



