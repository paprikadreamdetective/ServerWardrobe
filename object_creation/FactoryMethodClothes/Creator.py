from abc import ABC, abstractmethod
from PIL import Image
import numpy as np

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
        
def client_factory(creator: Creator, imagen: str, clothe_class: str) -> None:
    try:
        print("Client: Executing creator operation...")
        print(f"{creator.operation(imagen, clothe_class)}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")