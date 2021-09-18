from NodoGeneralMaquina import NodoGeneralMaquina
from NodoSimpleLineas import *
from NodoSimpleProductos import *

class GestorListaLineas:

    def __init__(self):
        self.cabeza = None

    

    def InsertarListaLineas(self,numero, cantidadComponentes, tiempoEnsamblaje):
        nuevo = NodoSimpleLineas(numero, cantidadComponentes,tiempoEnsamblaje)
        if self.cabeza is None:
            self.cabeza=nuevo
        else:
            auxiliar = self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar = auxiliar.siguiente
            auxiliar.siguiente = nuevo
        


    