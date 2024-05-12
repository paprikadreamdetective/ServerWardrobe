from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from ultralytics import YOLO
from rembg import remove
from collections import Counter
from PIL import Image


class Clothe(ABC):
    @property
    @abstractmethod
    def type(self):
        pass


class ButtomClothe(Clothe):
    def __init__(self, classification):
        self.classification = classification
        # self.c_type = "bottom"

    @property
    def type(self):
        return "bottom"

    # def do_classification(self):
    #     if self.classification in ["shorts", "skirt", "pants"]:
    #         return "bottom"
    #     else:
    #         return "not bottom"


class TopClothe(Clothe):
    def __init__(self, classification):
        self.classification = classification
        # self.c_type = "top"

    @property
    def type(self):
        return "top"

    # def do_classification(self):
    #     if self.classification in ["dress", "longsleeve", "outwear", "shirt", "t-shirt"]:
    #         return "top"
    #     else:
    #         return "not top"


class Shoes(Clothe):
    def __init__(self, classification):
        self.classification = classification
        # self.c_type = "shoes"

    @property
    def type(self):
        return "shoes"

    # def do_classification(self):
    #     if self.classification == "shoes":
    #         return "shoes"
    #     else:
    #         return "not shoes"


class Accessory(Clothe):
    def __init__(self, classification):
        self.classification = classification
        # self.c_type = "accessory"

    @property
    def type(self):
        return "accessory"

    # def do_classification(self):
    #     if self.classification == "hat":
    #         return "hat"
    #     else:
    #         return "not hat"


class Creator(ABC):
    @abstractmethod
    def factory_method(self, clss):
        pass

    # def _remove_backgroud_image(self, input_image, output_image):
    #     if input_image.endswith(('.png', 'jpg', 'jpeg')):
    #         with open(input_image, 'rb') as inp, open(output_image, 'wb') as outp:
    #             backgroud_output = remove(inp.read())
    #             outp.write(backgroud_output)
    #     else:
    #         print("The file is not valid")

    # def do_detection(self, image) -> str:
    #     model = YOLO('model/clothes_classification.pt')
    #     results = model(image, verbose=False)
    #     for r in results:
    #         probs = r.probs
    #         names = r.names
    #         clothe = probs.top1

    #     clothing_detected = names[clothe]
    #     return clothing_detected

    def recognize_predominant_color(self, image_path: str) -> tuple:
        img = Image.open(image_path)
        img = img.convert("RGBA")
        pixels = img.getdata()
        pixels_without_transparency = [p[:3] for p in pixels if p[3] != 0]
        counter = Counter(pixels_without_transparency)
        color = counter.most_common(1)[0][0]
        return color

    def operation(self, image, clothe_class) -> str:
        try:
            # self._remove_backgroud_image(in_image, out_image)
            # clothe_class = self.do_detection(out_image)
            clothe = self.factory_method(clothe_class)
            color_clothe = self.recognize_predominant_color(image)
            result = f"Creator operation:\n\tClothing detected: {clothe_class}\n\tClothing type: {
                clothe.type}\n\tPredominant color: {color_clothe}"
            return result
        except Exception as e:
            return f"Error: {str(e)}"


class CreatorButtom(Creator):
    def factory_method(self, clss) -> Clothe:
        return ButtomClothe(clss)


class CreatorTop(Creator):
    def factory_method(self, clss) -> Clothe:
        return TopClothe(clss)


class CreatorShoes(Creator):
    def factory_method(self, clss) -> Clothe:
        return Shoes(clss)


class CreatorAccessory(Creator):
    def factory_method(self, clss) -> Clothe:
        return Accessory(clss)


def client_code(creator: Creator, imagen: str, clothe_class: str) -> None:
    try:
        print("Client: Executing creator operation...")
        print(f"{creator.operation(imagen, clothe_class)}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")


# Ejemplo de uso
if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(CreatorTop(), "chamarra.jpg", "outwear")
