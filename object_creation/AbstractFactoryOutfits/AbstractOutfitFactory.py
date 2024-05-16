from abc import ABC, abstractmethod
import random
from pprint import pprint

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
    
def wear_outfit(factory: AbstractOutfitFactory):
    casual_outfit = factory.create_casual_outfit()
    formal_outfit = factory.create_formal_outfit()
    print("Casual Outfit:", casual_outfit.wear())
    print("Formal Outfit:", formal_outfit.wear())
    print("Random Outfit:", end=" ")
    pprint(factory.create_random_outfit())