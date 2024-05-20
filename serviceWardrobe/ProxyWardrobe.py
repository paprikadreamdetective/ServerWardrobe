from ServiceWardrobe import WardrobeService

class ProxyWardrobeService(WardrobeService):
    def __init__(self, real_service: WardrobeService):
        self._real_service = real_service

    def get_clothes(self, category: str):
        return self._real_service.get_clothes(category)

    def add_clothes(self, clothes: list):
        return self._real_service.add_clothes(clothes)