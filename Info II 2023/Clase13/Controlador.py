from Modelo import BaseDatos
from lanzador import Ventana_Ppal
import sys
from PyQt5.QtWidgets import QApplication 

class Coordinador:
    #como el coordindor enlaza el modelo con la vista debe
    #tener acceso a objetos de ambas clases
    def __init__(self, vista, modelo):
        self.__mi_vista = vista  
        self.__mi_modelo = modelo  

    def ingresarUsuario(self,n,c):
        return self.__mi_modelo.ingresarUsuario(n,c)     

def main():
    app = QApplication(sys.argv)  
    mi_vista = Ventana_Ppal() 
    mi_modelo = BaseDatos()  
    mi_coordinador = Coordinador(mi_vista,mi_modelo)  #Puente entre vista y modelo
    mi_vista.setControlador(mi_coordinador)
    mi_vista.show() 
    sys.exit(app.exec_())   

if __name__ == '__main__':
    main()
     