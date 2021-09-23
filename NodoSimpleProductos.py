class NodoSimpleProductos:
    def __init__(self, nombre, elaboracion,ListaLineas,ListaComponentes):
        self.NombreProducto = nombre
        self.Elaboracion    = elaboracion
        self.Lineas         = ListaLineas
        self.Componentes    = ListaComponentes
        self.siguiente      = None