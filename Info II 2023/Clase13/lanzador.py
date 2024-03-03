from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog 
from PyQt5.uic import loadUi 
from PyQt5.QtWidgets import QMessageBox 
import sys

class Ventana_Ppal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("menu.ui",self)
        self.setup()

    def setup(self):
        self.boton_ingresar.clicked.connect(self.on_click_ingreso)
        self.boton_salir.clicked.connect(self.on_click_salir)

    def recibirInfo(self,datos):
        nombre = datos[0]
        cedula = datos[1]
        resultado = self.__controlador.ingresarUsuario(nombre,cedula)
        print("Resultado "+ nombre +str (cedula))
        QMessageBox.information(self,"Mensaje de alerta",resultado)
        self.show()
 
    def on_click_ingreso(self):
        print("dentro dle slot")
        ventIngr =  Ventana_Ingreso(self)
        ventIngr.show()
        self.hide()

    def on_click_salir(self):
        print("dentro del slot de la función salir")
        self.close()

    def setControlador(self,c):
        self.__controlador = c


class Ventana_Ingreso(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        loadUi("ingresar.ui",self)
        self.__ventana_padre=parent
        self.setup()

    def setup(self):
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)

    def opcion_aceptar(self):
        print("Dentro de la funcion aceptar ")
        n=self.nombre.text()
        c=self.cedula.text()
        datos = [n,c]
        self.__ventana_padre.recibirInfo(datos)
        self.__ventana_padre.show()
             
    def opcion_cancelar(self):
        self.__ventana_padre.show()                
        print("Dentro de la opcion cancelar ")    

 



    
    