class NodoGeneralMaquina:
    def __init__(self, cantidadLineasProduccion,ListaLineas,ListaProductos,siguiente):
        self.CantidadLineas = cantidadLineasProduccion
        self.ListaLineas = ListaLineas
        self.ListaProductos= ListaProductos 
        self.siguiente=siguiente
        