class NodoSimpleLineas:
    def __init__(self, numero, cantidadComponentes, tiempoEnsamblaje):
        self.Numero = numero
        self.ComponentesLineas=cantidadComponentes
        self.TiempoEnsamble= tiempoEnsamblaje
        self.siguiente=None