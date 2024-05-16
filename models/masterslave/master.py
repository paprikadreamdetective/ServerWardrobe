from prenda_superior import Slave_PrendaSuperior
from prenda_inferior import Slave_PrendaInferior
from accesorios import Slave_Accesorios
from zapatos import Slave_Zapatos

class Master_ConjuntoRopa:
    def __init__(self, sel_PrendaSuperior, sel_PrendaInferior, sel_Accesorios, sel_Zapatos):
        self.sel_PrendaSuperior = sel_PrendaSuperior
        self.sel_PrendaInferior = sel_PrendaInferior
        self.sel_Accesorios = sel_Accesorios
        self.sel_Zapatos = sel_Zapatos

    def ejecucion_CrearConjunto(self):
        if self.sel_PrendaSuperior == 1:
            prendaSuperior = self.crear_PrendaSuperior("Suéter", "Azul", "M")
        else:
            prendaSuperior = None

        if self.sel_PrendaInferior == 1:
            prendaInferior = self.crear_PrendaInferior("Jeans", "Azul", "32")
        else:
            prendaInferior = None

        if self.sel_Accesorios == 1:
            accesorios = self.crear_Accesorios("Gorro", "Negro")
        else:
            accesorios = None

        if self.sel_Zapatos == 1:
            zapatos = self.crear_Zapatos("Tenis", "Blanco", "9")
        else:
            zapatos = None

        self.mostrar_Conjunto(prendaSuperior, prendaInferior, accesorios, zapatos)

        return [prendaSuperior, prendaInferior, accesorios, zapatos]

    def crear_PrendaSuperior(self, tipo, color, talla):
        return Slave_PrendaSuperior(tipo, color, talla)

    def crear_PrendaInferior(self, tipo, color, talla):
        return Slave_PrendaInferior(tipo, color, talla)

    def crear_Accesorios(self, tipo, color):
        return Slave_Accesorios(tipo, color)

    def crear_Zapatos(self, tipo, color, talla):
        return Slave_Zapatos(tipo, color, talla)

    def mostrar_Conjunto(self, prendaSuperior, prendaInferior, accesorios, zapatos):
        print("Conjunto de ropa:")

        if self.sel_PrendaSuperior == 1:
            print("Prenda superior:")
            print("Tipo:", prendaSuperior.get_tipo())
            print("Color:", prendaSuperior.get_color())
            print("Talla:", prendaSuperior.get_talla())

        if self.sel_PrendaInferior == 1:
            print("Prenda inferior:")
            print("Tipo:", prendaInferior.get_tipo())
            print("Color:", prendaInferior.get_color())
            print("Talla:", prendaInferior.get_talla())

        if self.sel_Accesorios == 1:
            print("Accesorios:")
            print("Tipo:", accesorios.get_tipo())
            print("Color:", accesorios.get_color())

        if self.sel_Zapatos == 1:
            print("Zapatos:")
            print("Tipo:", zapatos.get_tipo())
            print("Color:", zapatos.get_color())
            print("Talla:", zapatos.get_talla())
