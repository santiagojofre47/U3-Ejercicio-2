from ManejadorFlores import ManejadorFlores
from ManejadorRamos import manejadorRamo

class Menu:
    __opcion = None

    def mostrarMenu(self, unManejadorFlores, UnmanejadorRamos):
        if isinstance(unManejadorFlores, ManejadorFlores) and isinstance(UnmanejadorRamos, manejadorRamo):
            salir = False
            while not salir:
                print('\n')
                print('a- Vender un ramo')
                print('b- Mostrar nombre de las  flores mas pedidas de un ramo')
                print('c- Mostrar las flores de un tamano de ramo dado')
                print('d- Salir')
                self.__opcion = input('Ingrese una opcion: ')

                if self.__opcion.lower() == 'a':
                    self.EjecutarA(unManejadorFlores,UnmanejadorRamos)

                elif self.__opcion.lower() == 'b':
                    self.EjecutarB(unManejadorFlores, UnmanejadorRamos)

                elif self.__opcion.lower() == 'c':
                    self.EjecutarC(UnmanejadorRamos)

                elif self.__opcion.lower() == 'd':
                    salir = True
                    print('Cerrando menu...')

                else:
                    print('ERROR: opcion ingresada incorrecta!')
                    input('presione ENTER para continuar...')

    def EjecutarA(self, unManejadorFlores, UnmanejadorRamos):
        UnmanejadorRamos.venderRamo(unManejadorFlores)
    
    def EjecutarB(self, unManejadorFlores, UnmanejadorRamos):
        d = unManejadorFlores.getDiccionarioFlores()
        UnmanejadorRamos.mostrarTop(d)

    def EjecutarC(self, UnmanejadorRamos):
        tamano = input('Ingrese el tamano de un ramo: ')
        UnmanejadorRamos.mostrarFloresTamano(tamano)                

