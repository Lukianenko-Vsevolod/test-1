from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

class FileLogger(Logger):
    def log(self, message: str):
        return 'Logging to file: ' + message

class ConsoleLogger(Logger):
    def log(self, message: str):
        return 'Logging to console: ' + message

class LoggerFactory(ABC):
    @abstractmethod
    def createLogger(self) -> Logger:
        pass

    def logMessage(self, message: str):
        logger = self.createLogger()
        logger.log(message)

class FileLoggerFactory(LoggerFactory):
    def createLogger(self) -> Logger:
        return FileLogger()

class ConsoleLoggerFactory(LoggerFactory):
    def createLogger(self) -> Logger:
        return ConsoleLogger()
