class Flor:
    __Numero = None
    __Nombre = None
    __Color = None
    __Descripcion = None

    def __init__(self, numero = None, nombre = None, color = None, descripcion = None):
        self.__Numero = numero
        self.__Nombre = nombre
        self.__Color = color
        self.__Descripcion = descripcion

    def getNumero(self):
        return self.__Numero    

    def getNombre(self):
        return self.__Nombre
            

    def __str__(self):
        return 'Numero de flor: {} Nombre: {} Color: {} Descripcion: {}' .format(self.__Numero, self.__Nombre, self.__Color, self.__Descripcion)
