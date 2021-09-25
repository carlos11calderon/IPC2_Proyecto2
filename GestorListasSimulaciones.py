
from ListaSimulacionIndividual import *
import os

class GestorListaSimulacion:
    
    def __init__(self):
        self.Cabeza = None

    def InsertarEnSimularIndividual(self, Linea,Componente):
        nuevo = ListaSimulacionIndividual(int(Linea), int(Componente),None,None)
        if self.Cabeza is None:
            self.Cabeza=nuevo
        else: 
            aux = self.Cabeza
            while aux.Siguiente is not None:
                aux = aux.Siguiente
            aux.Siguiente= nuevo
            nuevo.Anterior= aux

    
    def ColaImportancia(self,producto):
        contAr=0
        aux = self.Cabeza
        producto = producto.replace(" ","_")
        f = open('ArchivosDots/archivo'+producto+'.dot', 'w', encoding='utf-8')
        node_data = ''
        edge_data = ''
        graph=''
        f.write( 'digraph List {\nrankdir=LR;\nnode [shape = record, color=black, style=filled, fillcolor=antiquewhite1];Inicio [shape = plaintext,fillcolor=white,label= \"\"];Final [shape = plaintext,fillcolor=white,label= \"\"];\n')
        counter = 0
        while(aux is not None):
            node_data += "Node" + str(counter) + "[label=\""+ 'L'+str(aux.Linea)+'C'+str(aux.Componente)+"\"];\n"
            counter+=1
            aux = aux.Siguiente
        graph += node_data
        counter=counter-1;
        cont = 0
        while(cont!=counter):
            edge_data += "Node" + str(cont) + "->Node" + str(cont+1) + ";\n"
            cont+=1
        

        graph += edge_data
        graph += "\n}"
        f.write(graph)
        f.close()
        
        os.system("dot -Tpng ArchivosDots/archivo"+producto+".dot -o ImagenesColas/salida"+producto+".png")
        #os.system("/ImagenesColas/salida"+producto+".png")
        contAr=contAr+1

          
    
    