# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Resistencia:
  def __init__(self):
    self.__serial_R=0
    self.__capacidad=0
  
  def verSerial_R(self):
    return self.__serial_R
  def verCapacidad(self):
    return self.__capacidad
  def asignarSerial_r(self,sr):
    self.__serial_R=sr
  def asignarCapacidad(self,c):
    self.__capacidad=c

class Capacitadores:
  def __init__(self):
    self.__serial_C=0
    self.__tipoCap=""
    self.__cajon=""
  
  def verSerial_C(self):
    return self.__serial_C
  def vertipoCap(self):
    return self.__tipoCap
  def verCajon(self):
    return self.__cajon  
  def asignarSerial_C(self,sc):
    self.__serial_C=sc
  def asignarCajon(self,cj):
    self.__cajon=cj
  def asignarTipoCap(self,tc):
    self.__tipoCap=tc  

class AmpliOpera:
  def __init__(self):
    self.__serial_amp=0
    self.__num_patas=0
    self.__codigo=0
  
  def verSerial_C(self):
    return self.__serial_amp
  def ver_num_patas(self):
    return self.__num_patas
  def verCodigo(self):
    return self.__codigo
  def asignarSerial_amp(self,sa):
    self.__serial_amp=sa
  def asignar_num_patas(self,np):
    self.__num_patas=np
  def asignarCodigo(self,ca):
    self.__codigo=ca 

  def __init__(self):
    self.__cedula=0
    self.__nombre=""
    
  def verCedula(self):
    return self.__cedula 
  def verNombre(self):
    return self.__nombre  
  def asignarCedula(self,Cc):
    self.__cedula=Cc
  def asignarNoimbre(self,n):
    self.__nombre=n

class EstacioBio:
  def __init__(self):
    self.__nom_monitor=""
    self.__tip_monitor=0
    self.__equipos=" modulo principal y generador de señales "
    self.__equiPrestados_bio={}    

  def ver_tip_monitor_bio(self):
    return self.__tip_monitor
  def verEquipos_bio(self):
    return self.__equipos
  def verEquiPrestados_bio(self):
    return self.__equiPrestados_bio 
  def asignar_nom_monitor_bio(self,m):
    self.__monitor=m
  def asignar_tip_monitor_bio(self,t):
      self.__tip_monitor=t
  def asignarEquiPrestados_bio(self,eq):
    self.__equiPrestados_bio       

class EstacionMoni:
  def __init__(self):
    self.__nom_monitor_central=""
    self.__cedula_monitor_central=0
    
    self.__equipos_moni=" computador central "
    self.__equiPrestados_moni={}    

  def verMonitor_central(self):
    return self.__monitor_central
  def verEquipos_moni(self):
    return self.__equipos_moni
  def verEquiPrestados_moni(self):
    return self.__equiPrestados_moni
  def asignar_nom_monitor_central(self,mc):
    self.__monitor_central=mc  
  def asignar_cedula_monitor_central(self,cm):
      self.__cedula_monitor_central=cm
  def asignarEquiPrestados_moni(self,eq):
    self.__equiPrestados_moni=eq


  def __init__(self):
    self.__monitor_control=None
    self.__equipos_control=" computador y modulo de señales "

  def verMonitor(self):
    return self.__monitor_control
  def verEquipos(self):
    return self.__equipos_control
  def asignarMonitor_control(self,mt):
    self.__monitor_control=mt     
  
class Sistema:
  def __init__(self):
    self.__resistencias={}
    self.__cap_ceramicos={}
    self.__cap_electro={}
    self.__ampli_opera={}

  def verResistencias(self):
    return self.__resistencias 
  def ingresar_resistencia(self,r):
    self.__resistencias[r.verSerial_R]=r
  def ingresar_cap_ceramicos(self,cc):
    self.__cap_ceramicos[cc.verSerial_C]=cc
  def ingresar_cap_electro(self,ce):
    self.__cap_electro[ce.verSerial_C]=ce
  def ingresar_ampli_opera(self,ao):
   self.__ampli_opera[ao.verSerial_C]=ao


def main():
  sis=Sistema()   
  esMon=EstacionMoni()
  esBio=EstacioBio()
  esMon.asignar_nom_monitor_central(input("ingrese el nombre del monitor central: "))
  esMon.asignar_cedula_monitor_central(int(input("ingrese cedula del monitor central: ")))
  esBio.asignar_nom_monitor_bio(input("ingrese el nombre del monitor de Bioinstrumentacion:  "))
  esBio.asignar_tip_monitor_bio(int(input("ingrese el numero de tip del monitor de Bioinstrumentacion: ")))
  
  
  while True:
    opc=int(input("1-ingresar inventario \n2-prestar componente \n "))
    if opc== 1:
      print('elija el tipo de componente a ingresar:')
      opc1=int(input("1-resistencia \n2-capacitador ceramico \n3-capacitador electrolitico \n4-amplificador operativo\n"))
      if opc1==1:
        r=Resistencia()
        r.asignarSerial_r(int(input("ingrese el numero de serial del componente: ")))
        cap=int(input("ingrese la capacidad en unidades de ohm:"))
        if cap < 100 or cap > 1000000:

          print(" capacidad fuera de rango, VERIFIQUE QUE ESTE EN UNIDADES DE OMH! \n intente nuevamente. ")
          continue 
        else: 
            r.asignarCapacidad(cap)
        sis.ingresar_resistencia(r)  
        
      if opc1==2:
          capa=Capacitadores()
          capa.asignarSerial_C(int(input("ingrese el numero de serial del componente: ")))
          capa.asignarTipoCap(" Ceramico ")
          cajon=(str(input("ingrese el numero de cajon (c1,c2,c3): ")))
          if cajon != "c1" and cajon != "c2" and cajon != "c3":
              print(" INGRESE UNA UBICACION CORRECTA!!, intente nuevamente. ")
          else: 
              capa.asignarCajon(cajon)
          sis.ingresar_cap_ceramicos(capa)
          
      if opc1==3:
          capa=Capacitadores()
          capa.asignarSerial_C(int(input("ingrese el numero de serial del componente: ")))
          capa.asignarTipoCap(" Electrolitico ")
          cajon=(str(input("ingrese el numero de cajon (c1,c2,c3): ")))
          if cajon != "c1" and cajon != "c2" and cajon != "c3":
              print(" INGRESE UNA UBICACION CORRECTA!!, intente nuevamente. ")
          else: 
              capa.asignarCajon(cajon)
          sis.ingresar_cap_electro(capa)
          
      if opc1==4:
          amp=AmpliOpera()
          amp.asignarSerial_amp(int(input("ingrese el numero de serial del componente: ")))
          amp.asignar_num_patas(int(input("ingrese el numoero de patas del componente: ")))
          amp.asignarCodigo(int(input("ingrese el codigo del amplificador: ")))
          sis.ingresar_ampli_opera(amp)
          
    if opc== 2:
        opc2=int(input("ingrese la estacion a la que pertenece: \n1-Bioinstrumentacion \n2-Central \n"))
        if opc2==1:
            tip=int(input("ingrese el numero de TIP del monitor a cargo: "))
            w=esBio.ver_tip_monitor_bio()
            if tip !=w:
                print("TIP invalida!!, intente nuevamente.")
            else:
                l=int(input(" Que componente desea prestar: \n1-Resistencia. \n2-Capacitador. \n3-Ampificador operacional.\n"))
                if l==1:
                    
                    
                        
                    
                    
        
        
          
          
    
        
        
        



if __name__ == '__main__':
  main()        

