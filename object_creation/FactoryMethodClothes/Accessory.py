from .Clothe import Clothe

class Accessory(Clothe):
    def __init__(self, classification):
        self.classification = classification
        self.color = None

    @property
    def type(self):
        return "accessory"