# Implementación de las clases Slave
class Slave_PrendaSuperior:
    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color

    def get_tipo(self):
        return self.tipo

    def get_color(self):
        return self.color


class Slave_PrendaInferior:
    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color

    def get_tipo(self):
        return self.tipo

    def get_color(self):
        return self.color


class Slave_Accesorios:
    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color

    def get_tipo(self):
        return self.tipo

    def get_color(self):
        return self.color

class Slave_Zapatos:
    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color

    def get_tipo(self):
        return self.tipo

    def get_color(self):
        return self.color


# Implementación de la clase Master_ConjuntoRopa
class Master_ConjuntoRopa:
    def __init__(self, sel_PrendaSuperior, sel_PrendaInferior, sel_Accesorios, sel_Zapatos):
        self.sel_PrendaSuperior = sel_PrendaSuperior
        self.sel_PrendaInferior = sel_PrendaInferior
        self.sel_Accesorios = sel_Accesorios
        self.sel_Zapatos = sel_Zapatos

    def ejecucion_CrearConjunto(self):
        if self.sel_PrendaSuperior == 1:
            prendaSuperior = self.crear_PrendaSuperior("Suéter", "Azul")
        else:
            prendaSuperior = None

        if self.sel_PrendaInferior == 1:
            prendaInferior = self.crear_PrendaInferior("Jeans", "Azul")
        else:
            prendaInferior = None

        if self.sel_Accesorios == 1:
            accesorios = self.crear_Accesorios("Gorro", "Negro")
        else:
            accesorios = None

        if self.sel_Zapatos == 1:
            zapatos = self.crear_Zapatos("Tenis", "Blanco")
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

# Uso de la clase Master_ConjuntoRopa
if __name__ == "__main__":
    conjunto = Master_ConjuntoRopa(1, 1, 1, 1)
    conjunto.ejecucion_CrearConjunto()