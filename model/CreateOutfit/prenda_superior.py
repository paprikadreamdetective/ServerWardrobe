from objectCreation.FactoryMethodClothes.factoryController import choose_creator

class Slave_PrendaSuperior:
    def __init__(self, tipo, color):
        #self._prenda_superior = choose_creator(tipo)
        self.tipo = tipo
        self.color = color

    def get_tipo(self):
        return self.tipo

    def get_color(self):
        return self.color
