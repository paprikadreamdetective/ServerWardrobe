from __future__ import annotations
from abc import ABC, abstractmethod

class WardrobeService(ABC):
    @abstractmethod
    def get_clothes(self, category: str):
        pass

    @abstractmethod
    def add_clothes(self, clothes: list):
        pass

# Implementación del servicio de guardarropa
class RealWardrobeService(WardrobeService):
    def get_clothes(self, category: str):
        pass

    def add_clothes(self, clothes: list):
        pass

# Implementación del proxy para el servicio de guardarropa
class ProxyWardrobeService(WardrobeService):
    def __init__(self, real_service: WardrobeService):
        self._real_service = real_service

    def get_clothes(self, category: str):
        return self._real_service.get_clothes(category)

    def add_clothes(self, clothes: list):
        return self._real_service.add_clothes(clothes)

