#imports tkinter

from GestorListasSimulaciones import  GestorListaSimulacion
from GestorSimulacion import GestorSimulacion
from GestorListaSimulacionIndividual import *
from NodoSimpleProductos import NodoSimpleProductos
from tkinter import filedialog, Tk
from tkinter.filedialog import *
from tkinter import * 
#import elementtree
from _elementtree import *
import xml.etree.cElementTree as ET
#imports clases
from NodoGeneralMaquina import NodoGeneralMaquina
from NodoSimpleLineas import *
from GestorListaSimulacionIndividual import *
from NodoSimpleProductos import *
from GestorListasLineas import *
from GestorListaProductos import *
from GestorSimulacion import GestorSimulacion
from GestorListaProductosSimular import *

class Gestor:
    Lista1 = GestorListaLineas()
    Lista2 = GestorListaProductos()
    Lista3= GestorSimulacion()
    Lista4 = GestorListaProductosSimular()
    ListaPadre = GestorSimulacion()
    def __init__(self):
        self.cabeza=None
        TamanoListaProductosMaquina=0
        TamanoListaProductosSimular=0
        self.cantComponentesGeneral=0 
    
    def InsertarMaquina(self, cantidad, ListaLineas, ListaProductos):
        nuevo = NodoGeneralMaquina(cantidad, ListaLineas, ListaProductos, None)
        if self.cabeza is None: 
            self.cabeza = nuevo
        else: 
            auxiliar = self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar= auxiliar.siguiente
            auxiliar.siguiente = nuevo


    def CargarArchivoConfig(self):
        global TamanoListaProductosMaquina
        global cantComponentesGeneral
        Tk().withdraw()
        archivo = filedialog.askopenfile(initialdir="./Archivos entrada", title="Seleccione un archivo",filetypes=(("Archivos XML",".xml"),("ALL files",".txt")))
        if archivo is None:
            print('No se selecciono ni un archivo\n')
            return None
        else:
            ##obtengo ruta del archivo
            rutaConfig = archivo
            tree = ET.parse(rutaConfig)
            root = tree.getroot()
            ## Objeto de la lista de Lineas
            
            for elemento in root:
                
                if elemento.tag == "CantidadLineasProduccion":
                    cantidadLineas = elemento.text
                ##for para listas de produccion
                if elemento.tag == "ListadoLineasProduccion":
                    for x in elemento:
                        for ele in x:
                            if ele.tag == "Numero":
                                NumLinea = ele.text
                            elif ele.tag == "CantidadComponentes":
                                cantComponentes = ele.text
                            elif ele.tag == "TiempoEnsamblaje":
                                TiempoEnsamble = ele.text
                        self.Lista1.InsertarListaLineas(int(NumLinea), int(cantComponentes), int(TiempoEnsamble))
                        if int(self.cantComponentesGeneral)<int(cantComponentes):
                            self.cantComponentesGeneral= cantComponentes
                elif elemento.tag == "ListadoProductos":
                    for x in elemento:
                        for ele in x:
                            if ele.tag=="nombre":
                                nombreProducto = ele.text
                            elif ele.tag=="elaboracion":
                                elaboracionProducto= ele.text
                        self.Lista2.InsertarListaProductos(nombreProducto,elaboracionProducto)
            self.TamanoListaProductosMaquina = len(self.Lista2.cabeza.NombreProducto)
            cantidadLineas = cantidadLineas.replace("\n",'')
            cantidadLineas = cantidadLineas.replace('\t','')
            self.InsertarMaquina(int(cantidadLineas), self.Lista1, self.Lista2)


    def CargarArchivoSimulacion(self):
        contador=0
        Tk().withdraw()
        archivo = filedialog.askopenfile(initialdir="./Archivos entrada", title="Seleccione un archivo",filetypes=(("Archivos XML",".xml"),("ALL files",".txt")))
        if archivo is None:
            print('No se selecciono ni un archivo\n')
            return None
        else:
            ##obtengo ruta del archivo
            rutaConfig = archivo
            tree = ET.parse(rutaConfig)
            root = tree.getroot()
            ## Objeto de la lista de Lineas
            
            for elemento in root:
                
                if elemento.tag == "Nombre":
                    nombre = elemento.text
                ##for para listas de produccion
                if elemento.tag == "ListadoProductos":
                    for x in elemento:
                        if x.tag == "Producto":
                            Producto = x.text
                            Producto = Producto.replace("\n","")
                            Producto = Producto.replace('\t','')
                            self.Lista4.InsertarProductoLista(Producto)
                            contador+=1
                self.TamanoListaProductosSimular = contador
                self.Lista3.InsertarSimulacion(nombre,self.Lista4)

    def addCombo(self, i ):
        valor = self.Lista2.AgregarCombo(i)
        return valor
    
    def addCombo2(self, i ):
        valor = self.Lista4.AgregarCombo(i)
        return valor

    def ComponenteMasGrande(self,producto,i):
        ExisteLinea=True
        contador=0
        componenteMayor = 0
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        if aux.Componente > componenteMayor:
            componenteMayor = aux.Componente
        while contador != i:
            if aux.Siguiente!=None:
                aux = aux.Siguiente
            else:
                ExisteLinea = False
            if ExisteLinea==True:
                if aux.Componente > componenteMayor:
                    componenteMayor = aux.Componente
                contador+=1
            else:
                contador+=1
        return componenteMayor



    def cantidadListaComponentes(self, textoCombo):
        
        cantidad = self.Lista2.ObtenerCantidadDeComponentes(textoCombo)
        if cantidad != None:
            return cantidad
        else:
            print("No retorno nada de la cantidad lista de componentes")
            return None

    def cantidadListaLineas(self, textoCombo):
        cantidad = self.Lista2.ObtenerCantidadDeLineas(textoCombo)
        if cantidad != None:
            return cantidad
        else:
            print("No retorno nada de la cantidad lista de Lineas")
            return None

    ## crea la lista prioridad
    def SimularProducto(self, Producto):
        
        ListaSimular = GestorListaSimulacion()
        contador=0
        aux = self.Lista2.cabeza
        while aux.NombreProducto != Producto:
            aux = aux.siguiente
        auxiliar1= aux.Lineas.cabeza
        auxiliar2= aux.Componentes.cabeza
        for x in range(self.Lista2.ObtenerCantidadDeComponentes(Producto)):
            
            while x!=contador:
                auxiliar1 = auxiliar1.siguiente
                auxiliar2 = auxiliar2.siguiente
                contador+=1
            valorline = auxiliar1.Linea
            valorCompo = auxiliar2.componente
            ListaSimular.InsertarEnSimularIndividual(valorline,valorCompo)
        self.ListaPadre.InsertarSimulacion(Producto, ListaSimular.Cabeza)
        ListaSimular.ColaImportancia(Producto)
        
        
    def DeterminarValoresIniciales(self,producto):
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        
        while aux is not None:
            aux.Ensamblado = False
            aux.ComponenteActual=0
            aux.Ensambla = False
            aux.LineaOcupada = False
            aux = aux.Siguiente
            
    

    def ObtenerComponenteActual(self,producto,posicion):
        contador=0
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        while contador != posicion:
            aux = aux.Siguiente
            contador+=1
        return aux.ComponenteActual
    
    def ObtenerComponenteEnsamblar(self,producto,posicion):
        contador=0
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        while contador != posicion:
            aux = aux.Siguiente
            contador+=1
        return aux.Componente
    
    def ObtenerLinea(self,producto,posicion):
        contador=0
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        while contador != posicion:
            aux = aux.Siguiente
            contador+=1
        return aux.Linea

    def DeclararComponenteActual(self,producto,posicion,agregado):
        contador=0
        Linea = self.RetornarLinea(producto,posicion)
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        
        while aux != None  :
            if aux.Linea == Linea:
                aux.ComponenteActual =  aux.ComponenteActual + agregado
            aux = aux.Siguiente

    def DeclararEnsamble(self,producto,posicion,valor):
        contador=0
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        while contador != posicion:
            aux = aux.Siguiente
            contador+=1
        aux.Ensambla = valor 

    def Ensambla(self,producto,posicion):
        contador=0
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        while contador != posicion:
            aux = aux.Siguiente
            contador+=1
        
        return aux.Ensambla

    def PuedeEnsamblar(self,producto,posicion):
        contador = 0
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        while contador != posicion:
            aux = aux.Siguiente 
            contador+=1
        if aux.Anterior is None or aux.Anterior.Ensamblado==True:
            return True
        else: 
            return False

    def CambiarEstadoEnsamblado(self, producto,posicion):
        contador=0
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        while contador != posicion:
            aux = aux.Siguiente 
            contador+=1
        aux.Ensamblado = True
     
    def Ensamblado(self,producto,posicion):
        contador=0
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        while contador != posicion:
            aux = aux.Siguiente
            contador+=1
        return aux.Ensamblado

    def LineaOcupada(self,producto,posicion):
        contador=0
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        while contador != posicion:
            aux = aux.Siguiente
            contador+=1
        return aux.LineaOcupada 
    
    def LineaOcupadaTrue(self,producto,linea):
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        while aux.Siguiente != None:
            if aux.Linea == linea:
                aux.LineaOcupada = True
            aux = aux.Siguiente
        if aux.Linea==linea:
            aux.LineaOcupada=True
    
    def LineaOcupadaFalse(self,producto,linea):
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        while aux.Siguiente != None:
            if aux.Linea == linea:
                aux.LineaOcupada = False
            aux = aux.Siguiente
        if aux.Linea==linea:
            aux.LineaOcupada=False
  
    def RetornarLinea(self,producto,posicion):
        contador=0
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        while contador != posicion:
            aux = aux.Siguiente
            contador+=1
        return aux.Linea 
    
    def RetornarComponente(self,producto,posicion):
        contador=0
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        while contador != posicion:
            aux = aux.Siguiente
            contador+=1
        return aux.Componente 

    def ExisteLinea(self,producto,linea):
        Existe = False
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        while aux.Linea != linea:
            if aux.Siguiente!=None:
                aux = aux.Siguiente
            else:
                
                    Existe = False
                    return False
        Existe=True
        if Existe==True:
            return True
                
    def ultimoNodoEnsamblado(self,producto):
        contador=0
        aux = self.ListaPadre.cabeza
        while aux.Nombre != producto:
            aux = aux.siguiente
        aux = aux.Productos
        posicion = self.cantidadListaComponentes(producto)
        for i in range(posicion-2):
            aux = aux.Siguiente
        return aux.Ensamblado

    def ObtenerTiempoEnsambleLinea(self,Linea):
        contador = 0
        aux= self.Lista1.cabeza
        while aux.Numero!=Linea:
            aux = aux.siguiente
        if Linea == aux.Numero:
            return aux.TiempoEnsamble
     
    def LineasRetornar(self,producto,texto):

        listado2 = GestorListaProductosSimular()
        estado = 0
        lexema=linea=componente=''
        for x in texto:
            if (estado==0):
                if (ord(x)==76):
                    lexema='Linea '
                    estado = 1
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass
            elif(estado==1):
                if (self.isNumero(x)==True):
                    lexema = ''
                    lexema+=x
                    estado = 2
            elif(estado==2):
                if (self.isNumero(x)==True):
                    lexema+=x
                elif(ord(x)==67 ):
                    listado2.InsertarLineaElaboracion(lexema)
                    lexema=''
                    lexema='Componente '
                    estado = 4
                elif(ord(x)==80):
                    estado = 3
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass
            elif(estado==3):
                if (ord(x)==67):
                    listado2.InsertarLineaElaboracion(lexema)
                    lexema = ''
                    lexema = 'Componente '
                    estado = 4
            elif(estado==4):
                if(self.isNumero(x)==True):
                    lexema+=x
                    estado = 5
            elif(estado==5):
                if(self.isNumero(x)==True):
                    lexema+=x
                elif(ord(x)==76):
                    lexema = 'Linea '
                    estado = 1
        return listado2

    def ComponentesRetornar(self,texto):
        listado = GestorListaComponentesUtil()
        estado = 0
        lexema=''
        for x in texto:
            if (estado==0):
                if (ord(x)==76):
                    lexema='Linea '
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
                    lexema='Componente '
                    estado = 4
                elif(ord(x)==80):
                    estado = 3
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass
            elif(estado==3):
                if (ord(x)==67):
                    lexema = ''
                    lexema = 'Componente '
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
                    lexema = 'Linea '
                    estado = 1
                elif(ord(x)==37):
                    listado.InsertarComponenteUtil(lexema)
        return listado 
        