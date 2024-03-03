class Componente:
    def __init__(self):
        self.__nombre=""
        self.__referencia=0
    def ingresarNombre(self,no):
        self.__nombre=no
    def verNombre(self):
        return self.__nombre
    def ingresarReferencia(self,ref):
        self.__referencia=ref
    def verReferencia(self):
        return self.__referencia
class Resistencias(Componente):
    def __init__(self):
        Componente.__init__(self)
        self.__capacidad=0
    def ingresarCapacidad(self,ca):
        self.__capacidad=ca
    def verCapacidad(self):
        return self.__capacidad
class capacitores(Componente):
    def __init__(self):
        Componente.__init__(self)
        self.__tipo=""
    def ingresarTipo (self,ti):
        self.__tipo=ti
    def verTipo(self):
        return self.__tipo
class Amplificadores(Componente):
    def __init__(self):
        Componente.__init__(self)
        self.__numerodepatas=0
        self.__codigo=0
    def ingresarPatas (self,pa):
        self.__numerodepatas=pa
    def verPatas(self):
        return self.__numerodepatas
    def ingresarCodigo (self,co):
        self.__codigo=co
    def verCodigo(self):
        return self.__codigo
class Persona:
    def __init__(self):
        self.__nombre=""
        self.__tip=0
        self.__estacion="monitor"
    def ingresarNombre(self,pa):
        self.__nombre=pa
    def verNombre(self):
        return self.__nombre
    def ingresarTip(self,ti):
        self.__tip=ti
    def verTip(self):
        return self.__tip

class Sistema:
    def __init__(self):
        self.__Bioinstrumentacion={}
        self.__componentes={}
    def Almacenamiento(self,ob):
        self.__componentes[ob.verReferencia()]=ob
    def PrestamoBio(self,p,v):
        self.__Bioinstrumentacion[v.verTip()]=p
    def prestarmo(self,c,cap="", tipo="", patas=0,codigo=0):
        for i in self.__componentes:
            de=self.__componentes[i]
            com=de.verNombre()
            if c=="Resistencia":
                if com=="Resistencia":
                    if de.verCapacidad()==cap:
                        del self.__componentes[i]
                        return de
            elif c=="Capacitor":
                if com=="Capacitor":
                    if de.verTipo()==tipo:
                        del self.__componentes[i]
                        return de
            elif c=="Amplificador":
                if com=="Amplificador":
                    if de.verPatas()==patas and de.verCodigo()==codigo:
                        del self.__componentes[i]
                        return de
    def verificar(self,c,cap=0, tipo="", patas=0,codigo=0):
        for i in self.__componentes:
            de=self.__componentes[i]
            com=de.verNombre()
            B=False
            if c=="Resistencia":
                if com=="Resistencia":
                    if de.verCapacidad()==cap:
                        B=True
                        return B
            elif c=="Capacitor":
                if com=="Capacitor":
                    if de.verTipo()==tipo:
                        B=True
                        return B
            elif c=="Amplificador":
                if com=="Amplificador":
                    if de.verPatas()==patas and de.verCodigo()==codigo:
                        B=True
                        return B
    def valueError(self,var):
            try:
                int(var)
                v = True
            except ValueError:
                v = False
            return v
    def verificarReferencia(self,c):
        return c in self.__componentes
    def biocomp(self):
        lis=[]
        for i in self.__Bioinstrumentacion:
            com=self.__Bioinstrumentacion[i]
            compo=com.verNombre()
            lis.append(compo)
        return lis
    def almacenin(self):
        lis=[]
        for i in self.__componentes:
            com=self.__componentes[i]
            compo=com.verNombre()
            lis.append(compo)
        return lis
def main():
    sis=Sistema()
    while True:
        monitor=Persona()
        bioin=Persona()
        tus=input("Por favor ingresar su TIP del monitor: ")
        tbio=input("Por favor ingresar su TIP del encargado en bioinstrumentación: ")
        d=sis.valueError(tus)
        d2=sis.valueError(tbio)
        if d==True and d2==True:
            nus=input("Por favor ingresar su nombre del monitor: ")
            nusb=input("Por favor ingresar su nombre del encargado en bioinstrumentación : ")
            monitor.ingresarNombre(nus)
            monitor.ingresarTip(tus)
            bioin.ingresarTip(tbio)
            bioin.ingresarNombre(nusb)
            while True:
                men1=input("""Por favor ingresar una de las siguientes opciones
                1.Almacenamiento de componentes electronicos
                2.Prestamo de componentes electricos 
                3.Ver Almacenamiento de Estaciones
                """)
                v=sis.valueError(men1)
                if v == True:
                    if int(men1)==1:
                        while True:
                            men2=input("""Por favor ingresar el tipo de componente que desea almacenar
                            1.Resistencia
                            2.Capacitor
                            3.Amplificador
                            """)
                            d=sis.valueError(men2)
                            if d ==True:
                                if int(men2)==1:
                                    while True:
                                        nr=input("Por favor ingresar la referencia: ")
                                        d=sis.valueError(nr)
                                        ban=sis.verificarReferencia(int(nr))
                                        if d== True and ban==False:
                                            nm="Resistencia"
                                            res=Resistencias()
                                            while True:
                                                cap=input("Por favor ingresar la capacidad en ohms: ")
                                                d1=sis.valueError(cap)
                                                if d1 ==True:
                                                    res.ingresarNombre(nm)
                                                    res.ingresarCapacidad(int(cap))
                                                    res.ingresarReferencia(int(nr))
                                                    sis.Almacenamiento(res)
                                                    print(res)
                                                    break
                                                else:
                                                    print("no es un valor númerico")
                                                    pass
                                            break
                                        else:
                                            pass
                                    break
                                elif int(men2)==2:
                                    while True:
                                        nr=input("Por favor ingresar la referencia: ")
                                        d=sis.valueError(nr)
                                        ban=sis.verificarReferencia(int(nr))
                                        if d== True and ban ==False:
                                            nm="Capacitor"
                                            capa=capacitores()
                                            while True:
                                                tip=input("""Por favor ingresar el tipo de capacitor
                                                1.Ceramico
                                                2.electrolíticos 
                                                """)
                                                d1=sis.valueError(tip)
                                                if d1 ==True:
                                                    if int(tip)==1:
                                                        t="Ceramico"
                                                        capa.ingresarTipo(t)
                                                        capa.ingresarNombre(nm)
                                                        capa.ingresarReferencia(int(nr))
                                                        sis.Almacenamiento(capa)
                                                        print(capa.verTipo())
                                                        break
                                                    elif int(tip)==2:
                                                        t="Electrolítico"
                                                        capa.ingresarTipo(t)
                                                        capa.ingresarNombre(nm)
                                                        capa.ingresarReferencia(int(nr))
                                                        sis.Almacenamiento(capa)
                                                        print(capa.verTipo())
                                                        break
                                                    else:
                                                        pass
                                                else:
                                                    print("No es una opción")
                                                    pass
                                            break
                                        else:
                                            pass 
                                    break
                                elif int(men2)==3:
                                    while True:
                                        nr=input("Por favor ingresar la referencia: ")
                                        d=sis.valueError(nr)
                                        ban=sis.verificarReferencia(int(nr))
                                        if d== True and ban ==False:
                                            nm="Amplificador"
                                            am=Amplificadores()
                                            while True:
                                                pat=input("Por favor ingresar el número de patas: ")
                                                cod=input("Por favor ingresar el codigo del amplificador: ")
                                                d1=sis.valueError(pat)
                                                d2=sis.valueError(cod)
                                                if d1 ==True and d2==True:
                                                    am.ingresarCodigo(int(cod))
                                                    am.ingresarNombre(nm)
                                                    am.ingresarPatas(int(pat))
                                                    am.ingresarReferencia(int(nr))
                                                    sis.Almacenamiento(am)
                                                    print(am)
                                                    break
                                                else:
                                                    print("No es un valor númerico")
                                                    pass
                                            break
                                        else:
                                            pass
                                    break
                                else:
                                    print("No es una de las opciones")
                                    pass
                            else:
                                pass
                    elif int(men1)==2:
                        while True:
                            est=input("""Por favor ingresar el puesto de trabajo
                                1.Bioinstrumentación
                                2.Teoria de Control
                                """)
                            d=sis.valueError(est)
                            if d==True:
                                if int(est)==1:
                                    while True:
                                        bus1=input("""Por favor seleccione la opción de componenente que necesita
                                        1.Resistencias
                                        2.Capacitores
                                        3.Amplificadores Operativos
                                        """)
                                        d1=sis.valueError(bus1)
                                        if d1==True:
                                            if int(bus1)==1:
                                                c="Resistencia"
                                                while True:
                                                    capa=input("Ingresar el valor de la capacidad en ohms: ")
                                                    d2=sis.valueError(capa)
                                                    if d2==True:
                                                        if int(capa) >= 100 and int(capa)<=10000000:
                                                            veri=sis.verificar(c,int(capa))
                                                            if veri==True:
                                                                comp=sis.prestarmo(c,int(capa))
                                                                sis.PrestamoBio(comp,bioin)
                                                                print(comp.verCapacidad())
                                                                break
                                                            else:
                                                                print("No existe en alamacenamiento")
                                                                break
                                                        else:
                                                            print("Valor no es el correcto")
                                                            pass    
                                                break
                                            elif int(bus1)==2:
                                                c="Capacitor"
                                                while True:
                                                    tipoc=input("""por favor ingresar el tipo de capacitor
                                                    1.Ceramico
                                                    2.Electrico
                                                    """)
                                                    d2=sis.valueError(tipoc)
                                                    if d2==True:
                                                        if int(tipoc)==1:
                                                            t="Ceramico"
                                                            veri=sis.verificar(c,0,t)
                                                            if veri==True:
                                                                print("2")
                                                                comp=sis.prestarmo(c,0,t)
                                                                sis.PrestamoBio(comp,bioin)
                                                                print(comp.verTipo())
                                                                break
                                                            else:
                                                                print("No hay componente")
                                                                break
                                                        elif int(tipoc)==2:
                                                            t="Electrolítico"
                                                            veri=sis.verificar(c,0,t)
                                                            if veri==True:
                                                                comp=sis.prestarmo(c,"",t)
                                                                sis.PrestamoBio(comp,bioin)
                                                                print(comp.verTipo())
                                                                break
                                                            else:
                                                                print("No hay componente")
                                                                break
                                                        else:
                                                            pass
                                                break        
                                            elif int(bus1)==3:
                                                c="Amplificador"
                                                while True:
                                                    cadpa=input("Por favor ingresar la cantidad de patas del amplificador: ")
                                                    cod=input("Por favor ingresar el código del amplificador: ")
                                                    d1=sis.valueError(cadpa)
                                                    d2=sis.valueError(cod)
                                                    if d2==True and d1==True:
                                                        veri=sis.verificar(c,0,"",int(cadpa),int(cod))
                                                        if veri==True:
                                                            comp=sis.prestarmo(c,0,"",int(cadpa),int(cod))
                                                            sis.PrestamoBio(comp,bioin)
                                                            print(comp)
                                                            break
                                                        else:
                                                            break
                                                    else:
                                                        pass
                                                break
                                    break
                                else:
                                    print("No es una opción")
                                    pass     
                    elif int(men1)==3:
                        while True:
                            men3=input("""Por favor ingresar una opción
                            1.Ver Almacenamiento de Bionintrumentación
                            2.Ver Almacenamiento de Monitor""")
                            d=sis.valueError(men3)
                            if d==True:
                                if int(men3)==1:
                                    res=sis.biocomp()
                                    print(res)
                                    break
                                elif int(men3)==2:
                                    res=sis.almacenin()
                                    print(res)
                                    break
                                else:
                                    pass
                            else:
                                pass 
                    elif int(men1)==4:

                        else:
                            print("""No es una opción del menu""") 
                            pass 
                else:
                    print("""Por favor ingresar un valor númerico y que pertenezca a las opciones
                    """)
                    pass
        else:
            print("""No es un valor númerico
            """)
            pass             
if __name__=='__main__':
    main()