class ListaSimulacionIndividual:
    def __init__(self, Linea, Componente,anterior,siguiente):
        self.Linea = Linea
        self.Componente = Componente
        self.LineaOcupada = False
        self.ComponenteActual = 0
        self.SeMueve = True
        self.Ensambla = False
        self.Ensamblado = False
        self.Anterior = anterior
        self.Siguiente = siguiente