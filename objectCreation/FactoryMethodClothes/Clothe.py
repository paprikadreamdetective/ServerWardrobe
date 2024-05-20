from abc import ABC, abstractmethod

class Clothe(ABC):
    @property
    @abstractmethod
    def type(self):
        pass