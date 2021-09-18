#imports tkinter

from GestorSimulacion import GestorSimulacion
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
from NodoSimpleProductos import *
from GestorListasLineas import *
from GestorListaProductos import *
from GestorSimulacion import *


class Gestor:

    def __init__(self):
        self.cabeza=None
    
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
                Lista1= GestorListaLineas()
                Lista2 = GestorListaProductos()
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
                        Lista1.InsertarListaLineas(int(NumLinea), int(cantComponentes), int(TiempoEnsamble))
                elif elemento.tag == "ListadoProductos":
                    for x in elemento:
                        for ele in x:
                            if ele.tag=="nombre":
                                nombreProducto = ele.text
                            elif ele.tag=="elaboracion":
                                elaboracionProducto= ele.text
                        Lista2.InsertarListaProductos(nombreProducto,elaboracionProducto)
            self.InsertarMaquina(cantidadLineas, Lista1, Lista2)


    def CargarArchivoSimulacion(self):
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
                Lista1= GestorSimulacion()
                Lista2 = GestorListaProductos()
                if elemento.tag == "Nombre":
                    nombre = elemento.text
                ##for para listas de produccion
                if elemento.tag == "ListadoProductos":
                    for x in elemento:
                        if x.tag == "Producto":
                            Producto = x.text
                            Lista2.InsertarListaProductos(Producto)
                Lista1.InsertarSimulacion(nombre,Lista2)

                



