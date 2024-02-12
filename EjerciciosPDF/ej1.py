#! /usr/bin/env python3
# Escribir un programa que pregunte al usuario su renta anual 
# y muestre por pantalla el tipo impositivo que le corresponde
''' 
Renta                   Tipo impositivo

    Menos de 10000          5%
    Entre 10000 y 20000     15%
    Entre 2000 y 35000      20%
    Entre 35000 y 60000     30%
    Más de 60000            45%
'''

PORCENTAJES = [0.05,   #Menos de 10000
                0.15,   #Entre 10000 y 20000
                0.2,    #Entre 20000 y 35000
                0.3,    #Entre 35000 y 60000
                0.45    #Más de 60000 
                ]

renta = int(input("Indica tu renta anual: "))

if (renta < 10000):
    print("Tu tipo es del ",PORCENTAJES[0]*100,"%")
elif (10000 < renta < 20000):
    print("Tu tipo es del ",PORCENTAJES[1]*100,"%")
elif (20000 < renta < 35000):
    print("Tu tipo es del ",PORCENTAJES[2]*100,"%")
elif (35000 < renta < 60000):
    print("Tu tipo es del ",PORCENTAJES[3]*100,"%")
elif (renta > 60000):
    print("Tu tipo es del ",PORCENTAJES[4]*100,"%")
    