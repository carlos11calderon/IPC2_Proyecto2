from ListaSimpleProductos import *
class GestorListaProductosSimular:
        contador=0
        def __init__(self):
                self.cabeza=None        
                
        def InsertarProductoLista(self, producto):
                nuevo = ListaSimpleProductos(producto, None)
                if self.cabeza is None: 
                        self.cabeza = nuevo
                else: 
                        auxiliar = self.cabeza
                        while auxiliar.siguiente is not None:
                                auxiliar= auxiliar.siguiente
                        auxiliar.siguiente = nuevo

        def AgregarCombo(self):
                auxiliar = self.cabeza
                         
                