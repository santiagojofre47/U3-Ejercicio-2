from ManejadorRamos import manejadorRamo
from ManejadorFlores import ManejadorFlores
from claseMenu import Menu

if __name__ == '__main__':
    objetoMenu = Menu()
    UnmanejadorRamos = manejadorRamo()
    UnManejadorFlor = ManejadorFlores()
    UnManejadorFlor.leerArchivo()
    objetoMenu.mostrarMenu(UnManejadorFlor, UnmanejadorRamos)
    