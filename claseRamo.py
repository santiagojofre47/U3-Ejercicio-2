from claseFlor import Flor

class Ramo:
    __Tamano = None
    __Flores = None

    def __init__(self, tamano):
        self.__Tamano = tamano
        self.__Flores = []

    def agregarFlor(self, unaFlor):
        if isinstance(unaFlor, Flor):
            self.__Flores.append(unaFlor)

    def getTamano(self):
        return self.__Tamano
    
    def getFlores(self):
        return self.__Flores

    def mostrarFlores(self):
        s = ''
        i = 0
        while i < len(self.__Flores):
            s+=str(self.__Flores[i])+'\n'
            i+=1
        print(s)
                           

    def __str__(self):
        s = 'Tamano de ramo: {}\nFlores:\n' .format(self.__Tamano)
        i = 0
        while i < len(self.__Flores):
            s+=str(self.__Flores[i])+'\n'
            i+=1
        return s    
