import csv
import numpy as np
from claseFlor import Flor

class ManejadorFlores:
    __flores = None
    __cantidad = None
    __incremento = None
    __dimension = None

    def __init__(self, dimesion = 10, incremento = 5):
        self.__dimension = dimesion
        self.__incremento = incremento
        self.__cantidad = 0
        self.__flores = np.empty(self.__dimension,dtype = Flor)

    def agregarFlor(self, unaFlor):
        if self.__cantidad == self.__dimension:
            self.__dimension+=self.__incremento
            self.__flores.resize(self.__dimension)
        self.__flores[self.__cantidad] = unaFlor
        self.__cantidad+=1

    def getFlor(self, numero):
        objeto = None
        if self.__flores[numero-1].getNumero() == numero:
            objeto = self.__flores[numero-1]
        return objeto

    def leerArchivo(self):
        archivo = open('flores.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for fila in reader:
            unaFlor = Flor(int(fila[0]),fila[1],fila[2],fila[3])
            self.agregarFlor(unaFlor)
        archivo.close()
    
    def getDiccionarioFlores(self):
        flores = dict()
        for i in range(self.__cantidad):
            flores[self.__flores[i].getNombre()] = 0
        return flores    

    def __str__(self):
        s = ''
        i = 0
        while i < self.__cantidad:
            s += str(self.__flores[i])+'\n'
            i+=1
        return s       