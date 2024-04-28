from __future__ import annotations
from abc import ABC, abstractmethod
from ultralytics import YOLO
from rembg import remove


model = YOLO('model/clothes_classification.pt')


class Clothe(ABC):
    
    @abstractmethod
    def do_classification(self):
        pass

class ButtomClothe(Clothe):
    def __init__(self, classification):
        self.classification = classification
        self.c_type = None

    def do_classification(self):
        if self.classification in ["shorts", "skirt", "pants"]:
            self.c_type = "bottom"
        else:
            return "not bottom"
        
class TopClothe(Clothe):
    def __init__(self, classification):
        self.classification = classification
        self.c_type = None

    def do_classification(self):
        if self.classification in ["dress", "longsleeve", "outwear", "shirt", "t-shirt"]:
            self.c_type = "top"
        else:
            return "not top"
        
class Shoes(Clothe):
    def __init__(self, classification):
        self.classification = classification
        self.c_type = None

    def do_classification(self):
        if self.classification == "shoes":
            self.c_type = "shoes"
        else:
            return "not shoes"

class Accessory(Clothe):
    def __init__(self, classification):
        self.classification = classification
        self.c_type = None

    def do_classification(self):
        if self.classification == "hat":
            self.c_type = "hat"
        else:
            return "not hat"
        
class Creator(ABC):
    @abstractmethod
    def factory_method(self, clss):
        pass

    def _remove_backgroud_image(self, input_image, output_image):
        if input_image.endswith(('.png', 'jpg', 'jpeg')):
            with open(input_image, 'rb') as inp, open(output_image, 'wb') as outp:
                backgroud_output = remove(inp.read())
                outp.write(backgroud_output)
        else:
            print("The file is not valid")

    def do_detection(self, image) -> str:
        results = model(image, verbose=False)
        for r in results:
            probs = r.probs
            names = r.names
            clothe = probs.top1

        clothing_detected = names[clothe]
        return clothing_detected

    def operation(self, in_image, out_image) -> str:

        self._remove_backgroud_image(in_image, out_image)
        clothe_class = self.do_detection(out_image)
        clothe = self.factory_method(clothe_class)
        result = f"vlv el creador\n{clothe.do_classification()}\n{clothe_class}\n{clothe.c_type}"

        return result
    
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
    
def client_code(creator: Creator) -> None:

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.operation("OG.jpg", "out.png")}", end="")
    
if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(CreatorButtom())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(CreatorTop())
    print("\n")
    print("App: Launched with the ConcreteCreator2.")
    client_code(CreatorShoes())
    print("\n")
    print("App: Launched with the ConcreteCreator2.")
    client_code(CreatorAccessory())