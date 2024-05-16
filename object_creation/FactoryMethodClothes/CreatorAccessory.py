from .Creator import Creator
from .Clothe import Clothe
from .Accessory import Accessory

class CreatorAccessory(Creator):
    def factory_method(self, clss) -> Clothe:
        return Accessory(clss)