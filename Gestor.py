#imports tkinter
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
from NodoSimpleLineas import *



class Gestor:

    def __init__(self):
        self.cabeza = None

    def InsertarMaquina(self, cantidad, ListaLineas, ListaProductos):
        nuevo = NodoGeneralMaquina(cantidad, ListaLineas, ListaProductos, None)
        if self.cabeza is None: 
            self.cabeza = nuevo
        else: 
            auxiliar = self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar= auxiliar.siguiente
            auxiliar.siguiente = nuevo

    def InsertarListaLineas(self,numero, cantidadComponentes, tiempoEnsamblaje):
        nuevo = NodoSimpleLineas(numero, cantidadComponentes,tiempoEnsamblaje)
        if self.cabeza is None:
            self.cabeza=nuevo
        else:
            auxiliar = self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar = auxiliar.siguiente
            auxiliar.siguiente = nuevo
        


    def InsertarListaProductos(self, Nombre, elaboracion):
        nuevo = NodoSimpleProductos(Nombre, elaboracion)
        if self.cabeza is None:
            self.cabeza= nuevo
        else:
            auxiliar = self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar = auxiliar.siguiente
            auxiliar.siguiente=nuevo


    def CargarArchivoConfig(self):
        Tk().withdraw()
        archivo = filedialog.askopenfilenames(initialdir="./Archivos entrada", title="Seleccione un archivo",filetypes=(("Archivos XML",".xml"),("ALL files",".txt")))
        if archivo is None:
            print('No se selecciono ni un archivo\n')
            return None
        else:
            rutaConfig = archivo
            tree = ET.parse(rutaConfig)
            root = tree.getroot()




