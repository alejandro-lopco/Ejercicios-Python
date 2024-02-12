#! /usr/bin/env python3
# Piramide o cuadrado de estrellas, con input de lineas
# Funciones
def triangulo(reps):
    pisos = reps
    for y in range(0,pisos):
        for x in range(reps,0,-1):
            print("★",end="")
        print("\n")
        reps-=1
def cuadrado(rep):
    pisos = rep
    for y in range(0,pisos):
        for x in range(0,rep):
            print("★",end="")
        print("\n")
# Inicio
opc = str("0")
while opc != "1" or "2":
    opc = str(input("Escoga la opción que quiera\n#1 Cuadrado\n#2 Triangulo\n Su opción: "))
    if opc == "1":
        print("Ha escogido el cuadrado")
        filas = int(input("¿Cuantas filas quieres? "))
        cuadrado(filas)
        print("Aquí tiene su cuadrado")
    elif opc == "2":
        print("Ha escogido el triangulo")
        filas = int(input("¿Cuantos pisos quieres? "))
        triangulo(filas)
        print("Aquí tiene su triangulo")
    else:
        print("Opción Incorrecta :(")
        break