from abc import ABC, abstractmethod
import random
from pprint import pprint
from .Outfit import Outfit
class AbstractOutfitFactory(ABC):
    @abstractmethod
    def create_casual_outfit(self) -> 'Outfit':
        pass

    @abstractmethod
    def create_formal_outfit(self) -> 'Outfit':
        pass

    @abstractmethod
    def create_random_outfit(self) -> dict:
        pass
        # """
        # Genera un outfit aleatorio combinando prendas de manera aleatoria.
        # """

        # outfit = {"top": {}, "buttom": {}, "shoes": {}, "accessory": {}}
        # ramdom_outfit = []

        # for types in clothes_list:
        #     ramdom_clothe = random.choice(list(types))
        #     ramdom_outfit.append(ramdom_clothe)

        # outfit['top'].update({ramdom_outfit[0]: clothes_list[0][ramdom_outfit[0]]})
        # outfit['buttom'].update({ramdom_outfit[1]: clothes_list[1][ramdom_outfit[1]]})
        # outfit['shoes'].update({ramdom_outfit[2]: clothes_list[2][ramdom_outfit[2]]})
        # outfit['accessory'].update({ramdom_outfit[3]: clothes_list[3][ramdom_outfit[3]]})

        # return str(outfit)
