from .Creator import Creator
from .Clothe import Clothe
from .TopClothe import TopClothe

class CreatorTop(Creator):
    def factory_method(self, clss) -> Clothe:
        return TopClothe(clss)