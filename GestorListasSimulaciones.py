
from ListaSimulacionIndividual import *


class GestorListaSimulacion:
    
    def __init__(self):
        self.Cabeza = None
        self.last = None

    def InsertarEnSimularIndividual(self, Linea,Componente):
        nuevo = ListaSimulacionIndividual(int(Linea), int(Componente),None,None)
        if self.Cabeza is None:
            self.Cabeza=self.last=nuevo
        else: 
            aux = self.Cabeza
            while aux.Siguiente is not None:
                aux = aux.Siguiente
            aux.Siguiente= nuevo
            nuevo.Anterior= aux

    
    
    
    
    def SeMueve(self,i):
        if i < self.Cabeza.Componente:
            valorMovimiento=self.Cabeza.SeMueve
            return valorMovimiento
        else:
            valorMovimiento = self.Cabeza.SeMueve
            self.Cabeza.SeMueve=False
            self.Cabeza.Ensambla=True
            return valorMovimiento

    
    def Ensambla(self,j,i):
        aux = self.Cabeza
        while aux.siguiente is not None:
            if j == aux.Linea:
                if aux.Componente == i+1:
                    aux.Ensambla = True 
            else:
                aux = aux.siguiente
            

    def Ensablado(self):
        pass
