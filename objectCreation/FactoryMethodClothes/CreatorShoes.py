from .Creator import Creator
from .Clothe import Clothe
from .Shoes import Shoes

class CreatorShoes(Creator):
    def factory_method(self, clss) -> Clothe:
        return Shoes(clss)