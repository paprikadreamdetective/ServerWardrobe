from .Creator import Creator
from .Clothe import Clothe
from .ButtomClothe import ButtomClothe

class CreatorButtom(Creator):
    def factory_method(self, clss) -> Clothe:
        return ButtomClothe(clss)