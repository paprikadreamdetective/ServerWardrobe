import abc

class ImageProcessingService(abc.ABC):
    @abc.abstractmethod
    def send(self):
        pass