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
            return self._create_outfit()

    def _create_outfit(self) -> dict:
        import random

        clothes = self.clothes_list
        outfit = {"top": {}, "buttom": {}, "shoes": {}, "accessory": {}}
        random_outfit = []

        for types in clothes:
            random_clothe = random.choice(list(types))
            random_outfit.append(random_clothe)

        outfit['top'].update({random_outfit[0]: clothes[0][random_outfit[0]]})
        outfit['buttom'].update({random_outfit[1]: clothes[1][random_outfit[1]]})
        outfit['shoes'].update({random_outfit[2]: clothes[2][random_outfit[2]]})
        outfit['accessory'].update({random_outfit[3]: clothes[3][random_outfit[3]]})

        return outfit
