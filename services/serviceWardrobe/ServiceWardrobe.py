from abc import ABC, abstractmethod

class WardrobeService(ABC):
    @abstractmethod
    def get_clothes(self, category: str):
        pass

    @abstractmethod
    def add_clothes(self, clothes: list):
        pass