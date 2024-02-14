#! /usr/bin/env Python3
''' 
Crear una clase Fecha con los atributos
    - Días
    - Meses
    - Años
Con los siguientes métodos
    - validar():        Comprueba si la fecha es correcta
    - bisiesto():       Mostrará si el año es bisiesto
    - diasPasados():    Devolverá el ńumero de días que han transcurido entre 2 años
'''

import datetime

class fecha():
    def __init__(self,dias,meses,anyo) -> None:
        self.dias   = dias
        self.meses  = meses
        self.anyo   = anyo
    def __str__(self) -> str:
        print("Estamos en el año",self.anyo)
        print("Del mes",self.meses)
        print("En el día",self.dias)

    def validar(self) -> bool:
        DIAS_DEL_MES = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.meses < 1:
            return False
        if self.meses > 12:
            return False
        if self.dias > DIAS_DEL_MES[self.meses]:
            return False
        return True
    def bisiesto(self,anyo) -> bool:
        if anyo % 4 == 0:
            if anyo % 100 != 0 or anyo % 400 == 0:
                return True
    def diasPasados(self,inputAnyo) -> int:
        DIAS_ANYO = 365

        newAnyo     = int(inputAnyo)
        diffAnyos   = abs(self.anyo - newAnyo)
        cantDias    = DIAS_ANYO * diffAnyos

        for x in range(self.anyo,newAnyo):
            if self.bisiesto(x) == True:
                cantDias+=1

        return cantDias
    
miFecha = fecha(31,12,1900)

if miFecha.validar() == True:
    print("La fecha es correcta")
else:
    print("La fecha NO es correcta")

if miFecha.bisiesto(miFecha.anyo) == True:
    print("El año es bisiesto")
else:
    print("El año NO es bisiesto")

dist = miFecha.diasPasados(input("Indica el año que quieres: "))
print ("Han pasado",dist,"días ")