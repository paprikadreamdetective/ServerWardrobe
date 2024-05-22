from .WardrobeOutfitComposite import WardrobeOutfitComposite
from objectCreation.AbstractFactoryOutfits.SummerOutfitFactory import SummerOutfitFactory
from objectCreation.AbstractFactoryOutfits.WinterOutfitFactory import WinterOutfitFactory

wardrobe_outfit_composite = WardrobeOutfitComposite()

def create_casual_summer_outfit():
    global wardrobe_outfit_composite
    wardrobe_outfit_composite.add(SummerOutfitFactory([]).create_casual_outfit())

def create_formal_summer_outfit():
    global wardrobe_outfit_composite
    wardrobe_outfit_composite.add(SummerOutfitFactory([]).create_formal_outfit())

def create_casual_winter_outfit():
    global wardrobe_outfit_composite
    wardrobe_outfit_composite.add(WinterOutfitFactory([]).create_casual_outfit())

def create_formal_winter_outfit():
    global wardrobe_outfit_composite
    wardrobe_outfit_composite.add(WinterOutfitFactory([]).create_formal_outfit())
 
def add_outfit(_type):
    global wardrobe_outfit_composite
    
    if 'Summer Casual' == _type:
        create_casual_summer_outfit()
    elif 'Summer Formal' == _type:
        create_formal_summer_outfit()
    elif 'Winter Casual' == _type:
        create_casual_winter_outfit()
    elif 'Winter Formal' == _type:
        create_formal_winter_outfit()