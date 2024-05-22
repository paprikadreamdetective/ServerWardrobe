import sys
from pathlib import Path
from objectCreation.factoryMethodClothes.CreatorButtom import CreatorButtom
from objectCreation.factoryMethodClothes.CreatorTop import CreatorTop
from objectCreation.factoryMethodClothes.CreatorShoes import CreatorShoes
from objectCreation.factoryMethodClothes.CreatorAccessory import CreatorAccessory
from objectCreation.factoryMethodClothes.Creator import client_factory
from model.imageProcessing.process import process_image


class CreateClothe():
    def __init__(self, clothe_class):
        self.clothe_class = clothe_class

    def choose_creator(self):
        if self.clothe_class in ["dress", "longsleeve", "outwear", "shirt", "t-shirt"]:
            return CreatorTop()
        elif self.clothe_class in ["shorts", "skirt", "pants"]:
            return CreatorButtom()
        elif self.clothe_class == "shoes":
            return CreatorShoes()
        elif self.clothe_class == "hat":
            return CreatorAccessory()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("Procesando y creando la prenda a partir de la imagen...\n")
        imagen = sys.argv[1]
        imagen = Path(imagen)
        image_back = f"./services/db/images/outputs/{imagen.stem}_backgroun.png"
        clothe_class = process_image(imagen.__str__(), image_back)
        client_factory(CreateClothe(clothe_class).choose_creator(),
                       image_back, clothe_class)
        print(f"\nImagen de entrada: {imagen}")
        print(f"Imagen de salida: {image_back}")
        sys.exit(1)
    elif len(sys.argv) == 1:
        print("Procesando imagen prestablecida...\n")
        imagen = Path("./services/db/images/inputs/chamarra1.png")
        image_back = f"./services/db/images/outputs/{imagen.stem}_backgroun.png"
        clothe_class = process_image(imagen.__str__(), image_back)
        client_factory(CreateClothe(clothe_class).choose_creator(),
                       image_back, clothe_class)
        print(f"\nImagen de entrada: {imagen}")
        print(f"Imagen de salida: {image_back}")
        sys.exit(1)
    else:
        print("Error: Número de argumentos inválido")
        sys.exit(1)
