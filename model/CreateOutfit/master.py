from .prenda_superior import Slave_PrendaSuperior
from .prenda_inferior import Slave_PrendaInferior
from .accesorios import Slave_Accesorios
from .zapatos import Slave_Zapatos

class Master_ConjuntoRopa:
    def __init__(self, sel_PrendaSuperior, sel_PrendaInferior, sel_Accesorios, sel_Zapatos):
        self.sel_PrendaSuperior = sel_PrendaSuperior
        self.sel_PrendaInferior = sel_PrendaInferior
        self.sel_Accesorios = sel_Accesorios
        self.sel_Zapatos = sel_Zapatos

    def ejecucion_CrearConjunto(self):
        if self.sel_PrendaSuperior == 1:
            tipo_superior = input("Introduce el tipo de prenda superior: ")
            color_superior = input("Introduce el color de la prenda superior: ")
            prendaSuperior = self.crear_PrendaSuperior(tipo_superior, color_superior)
        else:
            prendaSuperior = None

        if self.sel_PrendaInferior == 1:
            tipo_inferior = input("Introduce el tipo de prenda inferior: ")
            color_inferior = input("Introduce el color de la prenda inferior: ")
            prendaInferior = self.crear_PrendaInferior(tipo_inferior, color_inferior)
        else:
            prendaInferior = None

        if self.sel_Accesorios == 1:
            tipo_accesorio = input("Introduce el tipo de accesorio: ")
            color_accesorio = input("Introduce el color del accesorio: ")
            accesorios = self.crear_Accesorios(tipo_accesorio, color_accesorio)
        else:
            accesorios = None

        if self.sel_Zapatos == 1:
            tipo_zapato = input("Introduce el tipo de zapato: ")
            color_zapato = input("Introduce el color del zapato: ")
            zapatos = self.crear_Zapatos(tipo_zapato, color_zapato)
        else:
            zapatos = None

        self.mostrar_Conjunto(prendaSuperior, prendaInferior, accesorios, zapatos)

        return [prendaSuperior, prendaInferior, accesorios, zapatos]

    def crear_PrendaSuperior(self, tipo, color):
        return Slave_PrendaSuperior(tipo, color)

    def crear_PrendaInferior(self, tipo, color):
        return Slave_PrendaInferior(tipo, color)

    def crear_Accesorios(self, tipo, color):
        return Slave_Accesorios(tipo, color)

    def crear_Zapatos(self, tipo, color):
        return Slave_Zapatos(tipo, color)

    def mostrar_Conjunto(self, prendaSuperior, prendaInferior, accesorios, zapatos):
        print("Conjunto de ropa:")

        if self.sel_PrendaSuperior == 1:
            print("Prenda superior:")
            print("Tipo:", prendaSuperior.get_tipo())
            print("Color:", prendaSuperior.get_color())

        if self.sel_PrendaInferior == 1:
            print("Prenda inferior:")
            print("Tipo:", prendaInferior.get_tipo())
            print("Color:", prendaInferior.get_color())

        if self.sel_Accesorios == 1:
            print("Accesorios:")
            print("Tipo:", accesorios.get_tipo())
            print("Color:", accesorios.get_color())

        if self.sel_Zapatos == 1:
            print("Zapatos:")
            print("Tipo:", zapatos.get_tipo())
            print("Color:", zapatos.get_color())
