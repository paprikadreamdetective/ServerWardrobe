from objectCreation.FactoryMethodClothes.CreatorButtom import CreatorButtom
from objectCreation.FactoryMethodClothes.CreatorTop import CreatorTop
from objectCreation.FactoryMethodClothes.CreatorShoes import CreatorShoes
from objectCreation.FactoryMethodClothes.CreatorAccessory import CreatorAccessory
#from objectCreation.FactoryMethodClothes.Creator import client_factory
#from model.imageProcessing.process import process_image


def choose_creator(clothe_class):
    if clothe_class in ["dress", "longsleeve", "outwear", "shirt", "t-shirt"]:
        return CreatorTop()
    elif clothe_class in ["shorts", "skirt", "pants"]:
        return CreatorButtom()
    elif clothe_class == "shoes":
        return CreatorShoes()
    elif clothe_class == "hat":
        return CreatorAccessory()

'''
if __name__ == "__main__":
    # *** Factory Method ***
    image_w_back = "images/outputs/pantalon_w_back.png"
    clothe_class = process_image("images/inputs/pantalones.jpg", image_w_back)
    # print(clothe_class)
    client_factory(choose_creator(clothe_class), image_w_back, clothe_class)
'''