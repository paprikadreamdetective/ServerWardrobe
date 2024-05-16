from __future__ import annotations
from abc import ABC, abstractmethod
from PIL import Image
import numpy as np


class Clothe(ABC):
    @property
    @abstractmethod
    def type(self):
        pass


class ButtomClothe(Clothe):
    def __init__(self, classification):
        self.classification = classification
        self.color = None

    @property
    def type(self):
        return "bottom"


class TopClothe(Clothe):
    def __init__(self, classification):
        self.classification = classification
        self.color = None

    @property
    def type(self):
        return "top"


class Shoes(Clothe):
    def __init__(self, classification):
        self.classification = classification
        self.color = None

    @property
    def type(self):
        return "shoes"


class Accessory(Clothe):
    def __init__(self, classification):
        self.classification = classification
        self.color = None

    @property
    def type(self):
        return "accessory"


class Creator(ABC):
    @abstractmethod
    def factory_method(self, clss):
        pass

    def recognize_predominant_color(self, image_path: str) -> tuple:
        img = Image.open(image_path)

        # Convertir la imagen a formato RGBA (si no lo está ya)
        img = img.convert('RGBA')

        # Obtener los datos de los píxeles
        pixels = np.array(img)

        # Filtrar los píxeles que no son transparentes
        pixels_without_transparency = pixels[:, :, 3] > 0
        pixels_without_transparency = pixels[pixels_without_transparency]

        # Calcular el color predominante
        color = np.mean(pixels_without_transparency[:, :3], axis=0)
        # Redondear los valores y convertir a tipo entero
        color = tuple(map(int, color))

        return color

    def operation(self, image, clothe_class) -> str:
        try:
            clothe = self.factory_method(clothe_class)
            clothe.color = self.recognize_predominant_color(image)
            result = f"Creator operation:\n\tClothing detected: {clothe_class}\n\tClothing type: {
                clothe.type}\n\tPredominant color: {clothe.color}"

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


def client_factory(creator: Creator, imagen: str, clothe_class: str) -> None:
    try:
        print("Client: Executing creator operation...")
        print(f"{creator.operation(imagen, clothe_class)}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")


# Ejemplo de uso
if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_factory(CreatorTop(), "chamarra.jpg", "outwear")
