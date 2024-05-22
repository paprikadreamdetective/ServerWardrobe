from abc import ABC, abstractmethod
from .Outfit import Outfit


class AbstractOutfitFactory(ABC):
    @abstractmethod
    def create_casual_outfit(self) -> 'Outfit':
        pass

    @abstractmethod
    def create_formal_outfit(self) -> 'Outfit':
        pass

    @abstractmethod
    def create_random_outfit(self) -> dict:
        pass
