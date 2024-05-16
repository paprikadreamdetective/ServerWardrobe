from abc import ABC, abstractmethod
import json
from pathlib import Path
from pprint import pprint
import random


# Abstract Factory
class AbstractOutfitFactory(ABC):
    @abstractmethod
    def create_casual_outfit(self):
        pass

    @abstractmethod
    def create_formal_outfit(self):
        pass

    @abstractmethod
    def create_random_outfit(self, clothes_list) -> dict:
        """
        Genera un outfit aleatorio combinando prendas de manera aleatoria.
        """

        outfit = {"top": {}, "buttom": {}, "shoes": {}, "accessory": {}}
        ramdom_outfit = []

        for types in clothes_list:
            ramdom_clothe = random.choice(list(types))
            ramdom_outfit.append(ramdom_clothe)

        outfit['top'].update({ramdom_outfit[0]: clothes_list[0][ramdom_outfit[0]]})
        outfit['buttom'].update({ramdom_outfit[1]: clothes_list[1][ramdom_outfit[1]]})
        outfit['shoes'].update({ramdom_outfit[2]: clothes_list[2][ramdom_outfit[2]]})
        outfit['accessory'].update({ramdom_outfit[3]: clothes_list[3][ramdom_outfit[3]]})

        return outfit

# Concrete Factory 1
class SummerOutfitFactory(AbstractOutfitFactory):
    def __init__(self, clothes_list: list):
        self.clothes_list = clothes_list

    def create_casual_outfit(self):
        return SummerCasualOutfit()

    def create_formal_outfit(self):
        return SummerFormalOutfit()
    
    def create_random_outfit(self) -> dict:
        return super().create_random_outfit(self.clothes_list)

# Concrete Factory 2
class WinterOutfitFactory(AbstractOutfitFactory):
    def __init__(self, clothes_list: list):
        self.clothes_list = clothes_list

    def create_casual_outfit(self):
        return WinterCasualOutfit()

    def create_formal_outfit(self):
        return WinterFormalOutfit()
    
    def create_random_outfit(self) -> dict:
        return super().create_random_outfit(self.clothes_list)

# Abstract Product
class Outfit(ABC):
    def wear(self):
        pass

# Concrete Products
class SummerCasualOutfit(Outfit):
    def wear(self):
        return "Wear summer casual outfit: t-shirt, shorts, and shoes"

class SummerFormalOutfit(Outfit):
    def wear(self):
        return "Wear summer formal outfit: shirt, pants, and shoes"

class WinterCasualOutfit(Outfit):
    def wear(self):
        return "Wear winter casual outfit: longsleeve, pants, and shoes"

class WinterFormalOutfit(Outfit):
    def wear(self):
        return "Wear winter formal outfit: outwear, skirt, and shoes"

# Client
def wear_outfit(factory: AbstractOutfitFactory):
    casual_outfit = factory.create_casual_outfit()
    formal_outfit = factory.create_formal_outfit()
    print("Casual Outfit:", casual_outfit.wear())
    print("Formal Outfit:", formal_outfit.wear())
    print("Random Outfit:", end=" ")
    pprint(factory.create_random_outfit())

# Other functions
def clean_data(data: dict) -> list:
    clothe_list = [{}, {}, {}, {}]

    categories = ["top", "buttom", "shoes", "accessory"]
    for index, category in enumerate(categories):
        for item, details in data["clothes_user"][category].items():
            clothe_list[index][item] = details[2]["color"]

    return clothe_list

# Usage
if __name__ == "__main__":
    with open(Path("./db/example.json")) as f:
        data = json.load(f)
    clothes_list = clean_data(data)

    summer_factory = SummerOutfitFactory(clothes_list)
    wear_outfit(summer_factory)

    winter_factory = WinterOutfitFactory(clothes_list)
    wear_outfit(winter_factory)
