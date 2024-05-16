from .AbstractOutfitFactory import AbstractOutfitFactory
from .WinterCasualOutfit import WinterCasualOutfit
from .WinterFormalOutfit import WinterFormalOutfit

class WinterOutfitFactory(AbstractOutfitFactory):
    def __init__(self, clothes_list: list):
        self.clothes_list = clothes_list

    def create_casual_outfit(self):
        return WinterCasualOutfit()

    def create_formal_outfit(self):
        return WinterFormalOutfit()
    
    def create_random_outfit(self) -> dict:
        return super().create_random_outfit(self.clothes_list)