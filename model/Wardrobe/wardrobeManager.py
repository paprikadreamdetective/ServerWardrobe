from .WardrobeOutfitComposite import WardrobeOutfitComposite


from objectCreation.AbstractFactoryOutfits.SummerOutfitFactory import SummerOutfitFactory
from objectCreation.AbstractFactoryOutfits.WinterOutfitFactory import WinterOutfitFactory
from objectCreation.AbstractFactoryOutfits.AbstractOutfitFactory import wear_outfit

from pathlib import Path
import json

# ---------- Abstract Factory ----------
def clean_data(data: dict) -> list:
    clothe_list = [{}, {}, {}, {}]

    categories = ["top", "buttom", "shoes", "accessory"]
    for index, category in enumerate(categories):
        for item, details in data["clothes_user"][category].items():
            clothe_list[index][item] = details[2]["color"]
    return clothe_list


if __name__ == "__main__":
    wardrobe_outfit_composite = WardrobeOutfitComposite()

    #*** Abstract Factory ***
    with open(Path("./services/db/example.json")) as f:
        data = json.load(f)
    clothes_list = clean_data(data)

    summer_factory = SummerOutfitFactory(clothes_list)
    winter_factory = WinterOutfitFactory(clothes_list)

    wardrobe_outfit_composite.add(summer_factory.create_casual_outfit())
    wardrobe_outfit_composite.add(summer_factory.create_formal_outfit())
    wardrobe_outfit_composite.add(winter_factory.create_casual_outfit())
    wardrobe_outfit_composite.add(winter_factory.create_formal_outfit())
    
    wardrobe_outfit_composite.add(summer_factory.create_random_outfit())

    wardrobe_outfit_composite.execute()

    '''
    winter_factory = WinterOutfitFactory(clothes_list)

    
    '''
    
    #wear_outfit(summer_factory)

    
    #wear_outfit(winter_factory)
