from objectCreation.AbstractFactoryOutfits.SummerOutfitFactory import SummerOutfitFactory
from objectCreation.AbstractFactoryOutfits.WinterOutfitFactory import WinterOutfitFactory
import json
from pathlib import Path
from pprint import pprint

class GenerateOutfit():
    def __init__(self):
        pass

    def clean_data(self, data: dict) -> list:
        clothe_list = [{}, {}, {}, {}]

        categories = ["top", "buttom", "shoes", "accessory"]
        for index, category in enumerate(categories):
            for item, details in data["clothes_user"][category].items():
                clothe_list[index][item] = details[2]["color"]
        return clothe_list

    def _wear_outfit(self, factory):
        casual_outfit = factory.create_casual_outfit()
        formal_outfit = factory.create_formal_outfit()
        print("Casual Outfit:", casual_outfit.wear())
        print("Formal Outfit:", formal_outfit.wear())
        print("Random Outfit:", end=" ")
        pprint(factory.create_random_outfit())


    def operation(self):
        with open(Path("./services/db/example.json")) as f:
            data = json.load(f)
        clothes_list = self.clean_data(data)

        summer_factory = SummerOutfitFactory(clothes_list)
        self._wear_outfit(summer_factory)

        winter_factory = WinterOutfitFactory(clothes_list)
        self._wear_outfit(winter_factory)


if __name__ == "__main__":

    controller = GenerateOutfit()
    controller.operation()
