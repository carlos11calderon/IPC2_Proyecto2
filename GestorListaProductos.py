from GestorListaProductosSimular import GestorListaProductosSimular
from GestorListaComponentesUtil import GestorListaComponentesUtil
from PyQt5.sip import enableautoconversion
from NodoSimpleProductos import *
from ListaComponentesUtil import *
from GestorLineaElaboracion import *
from GestorListaSimulacionIndividual import *
class GestorListaProductos:

    def __init__(self):
        self.cabeza = None
        

    def InsertarListaProductos(self, Nombre, elaboracion):
        
        Nombre = Nombre.replace("\n",'')
        Nombre = Nombre.replace("\t",'')
        elaboracion = elaboracion.replace("\n",'')
        elaboracion = elaboracion.replace("\t",'')
        Lista1 = self.Lineas(elaboracion+"%")
        Lista2 = self.Componentes(elaboracion+"%")
        
        nuevo = NodoSimpleProductos(Nombre, elaboracion, Lista1, Lista2)
        if self.cabeza is None:
            self.cabeza= nuevo
        else:
            auxiliar = self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar = auxiliar.siguiente
            auxiliar.siguiente=nuevo
    
    def AgregarCombo(self,i):
        contador =0 
        auxiliar = self.cabeza
        while auxiliar !=None:
                if(i == contador):
                        return auxiliar.NombreProducto
                else: 
                        auxiliar = auxiliar.siguiente
                        contador+=1        
                        
        return None

    def ObtenerCantidadDeComponentes(self, producto):
        auxiliar = self.cabeza
        while auxiliar !=None:
                if( auxiliar.NombreProducto == producto):
                    auxiliar = auxiliar.Componentes.cabeza
                    if(auxiliar is None):
                        return 0
                    contador = 1
                    while auxiliar.siguiente is not None:
                        contador+=1
                        auxiliar=auxiliar.siguiente
                    return contador
                else: 
                    auxiliar = auxiliar.siguiente
        return None
    
    def ObtenerCantidadDeLineas(self, producto):
        
        auxiliar = self.cabeza
        while auxiliar !=None:
                if( auxiliar.NombreProducto == producto):
                    auxiliar = auxiliar.Lineas.cabeza
                    if(auxiliar is None):
                        return 0
                    contador = 1
                    while auxiliar.siguiente is not None:
                        contador+=1
                        auxiliar=auxiliar.siguiente
                    return contador
                else: 
                    auxiliar = auxiliar.siguiente
        return None


    def addListaComponentes(self, producto, i):
        contador=0
        auxiliar = self.cabeza
        while auxiliar != None:
            if(auxiliar.NombreProducto==producto):
                aux2 = auxiliar.Componentes.cabeza
                while aux2!=None: 
                    if (i==contador):
                        return aux2.componente
                    else: 
                        aux2 = aux2.siguiente
                        contador+=1
            else:
                auxiliar = auxiliar.siguiente 

                

        pass
    
    def addLineas(self,producto,i):
        contador=0
        auxiliar = self.cabeza
        while auxiliar != None:
            if(auxiliar.NombreProducto==producto):
                aux2 = auxiliar.Lineas.cabeza
                while aux2!=None: 
                    if (i==contador):
                        return aux2.Linea
                    else: 
                        aux2 = aux2.siguiente
                        contador+=1
            else:
                auxiliar = auxiliar.siguiente 

    def isNumero(self,caracter):
        if ((ord(caracter) >= 48 and ord(caracter) <= 57)):
            return True
        else:
            return False

    
    def Componentes(self,texto):
        listado = GestorListaComponentesUtil()
        estado = 0
        lexema=''
        for x in texto:
            if (estado==0):
                if (ord(x)==76):
                    lexema=''
                    estado = 1
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass
            elif(estado==1):
                if (self.isNumero(x)==True):
                    lexema+=x
                    estado = 2
            elif(estado==2):
                if (self.isNumero(x)==True):
                    lexema+=x
                elif(ord(x)==67 ):
                    lexema=''
                    lexema=''
                    estado = 4
                elif(ord(x)==80):
                    estado = 3
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass
            elif(estado==3):
                if (ord(x)==67):
                    lexema = ''
                    lexema = ''
                    estado = 4
            elif(estado==4):
                if(self.isNumero(x)==True):
                    lexema+=x
                    estado = 5
            elif(estado==5):
                if(self.isNumero(x)==True):
                    lexema+=x
                elif(ord(x)==76):
                    listado.InsertarComponenteUtil(lexema)
                    lexema = ''
                    estado = 1
                elif(ord(x)==37):
                    listado.InsertarComponenteUtil(lexema)
        return listado   

    def Lineas(self,texto):

        listado2 = GestorLineaElaboracion()
        estado = 0
        lexema=linea=componente=''
        for x in texto:
            if (estado==0):
                if (ord(x)==76):
                    lexema=''
                    estado = 1
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass
            elif(estado==1):
                if (self.isNumero(x)==True):
                    lexema+=x
                    estado = 2
            elif(estado==2):
                if (self.isNumero(x)==True):
                    lexema+=x
                elif(ord(x)==67 ):
                    listado2.InsertarLineaElaboracion(lexema)
                    lexema=''
                    lexema=''
                    estado = 4
                elif(ord(x)==80):
                    estado = 3
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass
            elif(estado==3):
                if (ord(x)==67):
                    listado2.InsertarLineaElaboracion(lexema)
                    lexema = ''
                    lexema = ''
                    estado = 4
            elif(estado==4):
                if(self.isNumero(x)==True):
                    lexema+=x
                    estado = 5
            elif(estado==5):
                if(self.isNumero(x)==True):
                    lexema+=x
                elif(ord(x)==76):
                    lexema = ''
                    estado = 1
        return listado2
