import json
from pathlib import Path

from objectCreation.AbstractFactoryOutfits.AbstractOutfitFactory import wear_outfit
from objectCreation.AbstractFactoryOutfits.WinterOutfitFactory import WinterOutfitFactory
from objectCreation.AbstractFactoryOutfits.SummerOutfitFactory import SummerOutfitFactory


# ---------- Abstract Factory ----------


def clean_data(data: dict) -> list:
    clothe_list = [{}, {}, {}, {}]

    categories = ["top", "buttom", "shoes", "accessory"]
    for index, category in enumerate(categories):
        for item, details in data["clothes_user"][category].items():
            clothe_list[index][item] = details[2]["color"]

    return clothe_list


if __name__ == "__main__":

    # *** Abstract Factory ***
    with open(Path("./db/example.json")) as f:
        data = json.load(f)
    clothes_list = clean_data(data)

    summer_factory = SummerOutfitFactory(clothes_list)
    wear_outfit(summer_factory)

    winter_factory = WinterOutfitFactory(clothes_list)
    wear_outfit(winter_factory)
