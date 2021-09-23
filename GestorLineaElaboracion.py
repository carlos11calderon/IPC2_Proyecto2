from NodoLineaElaboracion import *
class GestorLineaElaboracion:

    def __init__(self):
        self.cabeza= None

    def InsertarLineaElaboracion(self, Linea):
        nuevo = NodoLineaElaboracion(Linea, None)
        if self.cabeza is None: 
            self.cabeza = nuevo
        else: 
            auxiliar = self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar= auxiliar.siguiente
            auxiliar.siguiente = nuevo