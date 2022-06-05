from claseRamo import Ramo
import operator
from ManejadorFlores import ManejadorFlores

class manejadorRamo:
    __lista = None

    def __init__(self):
        self.__lista = []

    def agregarRamo(self, unRamo):
        if isinstance(unRamo, Ramo):
            self.__lista.append(unRamo)

    def venderRamo(self, unManejadorFlores):
        es_entero = False
        incorrecto = True
        tamano = None
        while not es_entero:
            try:
                print('1- Ramo chico')
                print('2- Ramo mediano')
                print('3- Ramo grande')
                tamano = int(input('Seleccione un tamano de ramo: '))
            except ValueError:
                print('ERROR: no se ingreso un numero entero')
            else:
                es_entero = True

        while incorrecto:
            if tamano == 1:
                i = 0
                unRamo = Ramo('Chico')
                while i < 2:
                    print(unManejadorFlores)
                    numero = input('Seleccione el numero de flor: ')
                    assert numero.isdigit(), 'Debe ser un nuemero'
                    numero = int(numero)
                    flor = unManejadorFlores.getFlor(numero)
                    unRamo.agregarFlor(flor)
                    i+=1
                    incorrecto = False
                self.agregarRamo(unRamo)    
            elif tamano == 2:
                i = 0
                unRamo = Ramo('Mediano')
                while i < 3:
                    print(unManejadorFlores)
                    numero = input('Seleccione el numero de flor: ')
                    assert numero.isdigit(), 'Debe ser un nuemero'
                    numero = int(numero)
                    flor = unManejadorFlores.getFlor(numero)
                    unRamo.agregarFlor(flor)
                    i+=1
                    incorrecto = False
                self.agregarRamo(unRamo)    
            elif tamano == 3:
                i = 0
                unRamo = Ramo('Grande')
                while i < 4:
                    print(unManejadorFlores)
                    numero = input('Seleccione el numero de flor: ')
                    assert numero.isdigit(), 'Debe ser un nuemero'
                    numero = int(numero)
                    flor = unManejadorFlores.getFlor(numero)
                    unRamo.agregarFlor(flor)
                    i+=1
                    incorrecto = False
                self.agregarRamo(unRamo)    
            else:
                print('ERROR: tamano ingresado incorrecto!')   

    def mostrarFloresTamano(self, tamano):
        i = 0
        encontro = False
        print('Flores vendidas en ramos de tamano {}:\n' .format(tamano))
        while i < len(self.__lista):
            if self.__lista[i].getTamano().lower() == tamano.lower():
                self.__lista[i].mostrarFlores()
                encontro = True
                i+=1
            else:
                i+=1 
        if not encontro:
            print('ERROR: ramos de tamanio {} no encontrados!' .format(tamano))     
    
    def mostrarTop(self, un_diccionario):
        assert isinstance(un_diccionario, dict), "ERROR: Debe ser un diccionario!"
        print('=== LISTADO DE LAS FLORES MAS VENDIDAS ===')
        for ramo in self.__lista:
            for flores in ramo.getFlores():
                un_diccionario[flores.getNombre()]+= 1
        flores_sorted = sorted(un_diccionario.items(), key=operator.itemgetter(1), reverse=True)
        for name in enumerate(flores_sorted):
            print(name[1][0],'cantidad pedida:', un_diccionario[name[1][0]])   
    
    def __str__(self):
        s = ''
        i = 0
        while i < len(self.__lista):
            s+= str(self.__lista[i])+'\n'
            i+=1
        return s            