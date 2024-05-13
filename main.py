from ultralytics import YOLO
from rembg import remove
from factories.FactoryMethodClothes import CreatorButtom, CreatorTop, CreatorShoes, CreatorAccessory, client_code


def remove_backgroud_image(input_image, output_image):
    if input_image.endswith(('.png', 'jpg', 'jpeg')):
        with open(input_image, 'rb') as inp, open(output_image, 'wb') as outp:
            backgroud_output = remove(inp.read())
            outp.write(backgroud_output)
    else:
        print("The file is not valid")


def do_detection(image) -> str:
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


if __name__ == "__main__":
    image_w_back = "images/outputs/pantalon_w_back.png"
    clothe_class = process_image("images/inputs/pantalones.jpg", image_w_back)
    # print(clothe_class)
    client_code(choose_creator(clothe_class), image_w_back, clothe_class)
