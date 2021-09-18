from NodoSimpleProductos import *
class GestorListaProductos:

    def __init__(self):
        self.cabeza = None

    def InsertarListaProductos(self, Nombre, elaboracion):
        nuevo = NodoSimpleProductos(Nombre, elaboracion)
        if self.cabeza is None:
            self.cabeza= nuevo
        else:
            auxiliar = self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar = auxiliar.siguiente
            auxiliar.siguiente=nuevo