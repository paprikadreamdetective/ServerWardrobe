import json
from pathlib import Path

from ultralytics import YOLO
from rembg import remove

from object_creation.FactoryMethodClothes.CreatorButtom import CreatorButtom
from object_creation.FactoryMethodClothes.CreatorTop import CreatorTop
from object_creation.FactoryMethodClothes.CreatorShoes import CreatorShoes
from object_creation.FactoryMethodClothes.CreatorAccessory import CreatorAccessory

from object_creation.AbstractFactoryOutfits.AbstractOutfitFactory import wear_outfit
from object_creation.AbstractFactoryOutfits.WinterOutfitFactory import WinterOutfitFactory
from object_creation.AbstractFactoryOutfits.SummerOutfitFactory import SummerOutfitFactory


def remove_backgroud_image(input_image, output_image):
    if input_image.endswith(('.png', 'jpg', 'jpeg')):
        with open(input_image, 'rb') as inp, open(output_image, 'wb') as outp:
            backgroud_output = remove(inp.read())
            outp.write(backgroud_output)
    else:
        print("The file is not valid")


def do_detection(image) -> str:
    """
    Detections :
        - dress
        - hat
        - longsleeve
        - outwear
        - pants
        - shirt
        - shoes
        - shorts
        - skirt
        - t-shirt
    """
    model = YOLO('model/clothes_classification.pt')
    results = model(image, verbose=False)
    for r in results:
        probs = r.probs
        names = r.names
        clothe = probs.top1

    clothing_detected = names[clothe]
    return clothing_detected


def process_image(in_image, out_image):
    remove_backgroud_image(in_image, out_image)
    clothe = do_detection(out_image)
    return clothe


def choose_creator(clothe_class):
    if clothe_class in ["dress", "longsleeve", "outwear", "shirt", "t-shirt"]:
        return CreatorTop()
    elif clothe_class in ["shorts", "skirt", "pants"]:
        return CreatorButtom()
    elif clothe_class == "shoes":
        return CreatorShoes()
    elif clothe_class == "hat":
        return CreatorAccessory()
    
# ---------- Abstract Factory ----------

def clean_data(data: dict) -> list:
    clothe_list = [{}, {}, {}, {}]

    categories = ["top", "buttom", "shoes", "accessory"]
    for index, category in enumerate(categories):
        for item, details in data["clothes_user"][category].items():
            clothe_list[index][item] = details[2]["color"]

    return clothe_list
    

if __name__ == "__main__":
    # *** Factory Method ***
    # image_w_back = "images/outputs/pantalon_w_back.png"
    # clothe_class = process_image("images/inputs/pantalones.jpg", image_w_back)
    # # print(clothe_class)
    # client_code(choose_creator(clothe_class), image_w_back, clothe_class)

    # *** Abstract Factory ***
    with open(Path("./db/example.json")) as f:
        data = json.load(f)
    clothes_list = clean_data(data)

    summer_factory = SummerOutfitFactory(clothes_list)
    wear_outfit(summer_factory)

    winter_factory = WinterOutfitFactory(clothes_list)
    wear_outfit(winter_factory)

