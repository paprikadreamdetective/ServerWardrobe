from .AbstractOutfitFactory import AbstractOutfitFactory
from .SummerCasualOutfit import SummerCasualOutfit
from .SummerFormalOutfit import SummerFormalOutfit

class SummerOutfitFactory(AbstractOutfitFactory):
    def __init__(self, clothes_list: list):
        self.clothes_list = clothes_list

    def create_casual_outfit(self):
        return SummerCasualOutfit()

    def create_formal_outfit(self):
        return SummerFormalOutfit()
    
    def create_random_outfit(self) -> dict:
        return super().create_random_outfit(self.clothes_list)