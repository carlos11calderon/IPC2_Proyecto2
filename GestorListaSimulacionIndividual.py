from NodoGeneralSimularIndividual import *
class GestorSimulacion:
    def __init__(self):
        self.Cabeza= None

    def InsertarEnSimularIndividual(self, Nombre, Lista):
        nuevo = NodoGeneralSimularIndividual(Nombre, Lista, None)
        if self.Cabeza is None:
            self.Cabeza=nuevo
        else: 
            aux = self.Cabeza
            while aux.Siguiente is not None:
                aux = aux.Siguiente
            aux.Siguiente= nuevo