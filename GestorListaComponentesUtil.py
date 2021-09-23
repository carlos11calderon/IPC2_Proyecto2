from ListaComponentesUtil import ListaComponentesUtil


class GestorListaComponentesUtil:
    def __init__(self):
        self.cabeza= None

    def InsertarComponenteUtil(self, Componente):
        nuevo = ListaComponentesUtil(Componente, None)
        if self.cabeza is None: 
            self.cabeza = nuevo
        else: 
            auxiliar = self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar= auxiliar.siguiente
            auxiliar.siguiente = nuevo