class Usuario:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = ""

    def getNombre(self):
        return self.__nombre
    def getCedula(self):
        return self.__cedula

    def setNombre(self, i):
        self.__nombre = i
    def setCedula(self, i):
        self.__cedula = i
    

class BaseDatos:
    def __init__(self):
        self.__lista_usuarios = {}

    def ingresarUsuario(self,n,c):# n y c son la variables nombre y cedula que llegan desde la vista al controlador y finalmente al modelo
        if self.validarUsuario(c) == True:
            return "El usuario ya existe"
        u = Usuario()
        u.setNombre(n)
        u.setCedula(c)
        self.__lista_usuarios[c]=u
        return "Usuario Ingresado"

    def validarUsuario(self,c):
        return c in self.__lista_usuarios