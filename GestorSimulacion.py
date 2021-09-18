from NodoGeneralSimulacion import *
class GestorSimulacion:
    def __init__(self):
        self.Cabeza= None

    def InsertarSimulacion(self, Nombre, Listaproducto):
        nuevo = NodoGeneralSimulacion(Nombre, Listaproducto, None)
        if self.cabeza is None: 
            self.cabeza = nuevo
        else: 
            auxiliar = self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar= auxiliar.siguiente
            auxiliar.siguiente = nuevo