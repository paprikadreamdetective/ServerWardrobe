import json
from pathlib import Path
from pprint import pprint
import ast
from objectCreation.abstractFactoryOutfits.SummerOutfitFactory import SummerOutfitFactory
from objectCreation.abstractFactoryOutfits.WinterOutfitFactory import WinterOutfitFactory

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
        message = f"Casual Outfit: {casual_outfit.wear()}\nFormal Outfit: {formal_outfit.wear()}\nRandom Outfit: \n{factory.create_random_outfit()}"
        # print("Casual Outfit:", casual_outfit.wear())
        # print("Formal Outfit:", formal_outfit.wear())
        # print("Random Outfit:", end=" ")
        # pprint(factory.create_random_outfit())
        return message


    def operation(self):
        with open(Path("./services/db/example.json")) as f:
            data = json.load(f)
        clothes_list = self.clean_data(data)

        summer_factory = SummerOutfitFactory(clothes_list)
        summer_o = self._wear_outfit(summer_factory)

        winter_factory = WinterOutfitFactory(clothes_list)
        winter_o = self._wear_outfit(winter_factory)
        message = f"{summer_o}\n\n{winter_o}"
        return message
    

def parse_outfit_string(input_string):
    lines = input_string.split('\n')
    result = []

    current_outfit_set = {}
    in_random_outfit = False

    for line in lines:
        if "Casual Outfit" in line or "Formal Outfit" in line:
            in_random_outfit = False
            outfit_type = line.split(":")[0]
            description = line.split(":")[1].strip()
            current_outfit_set[outfit_type] = description
        elif "Random Outfit" in line:
            in_random_outfit = True
            current_outfit_set["Random Outfit"] = ""
        elif in_random_outfit and line.startswith("{") and line.endswith("}"):
            random_outfit_dict = ast.literal_eval(line)
            current_outfit_set["Random Outfit"] = random_outfit_dict
            result.append(current_outfit_set)
            current_outfit_set = {}
            in_random_outfit = False

    return result


if __name__ == "__main__":

    controller = GenerateOutfit()
    print(controller.operation())
