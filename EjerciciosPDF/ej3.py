#! /usr/bin/env python3
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
#Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada 
#asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por 
#pantalla las asignaturas que el usuario tiene que repetir.

asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
notas       = [None,None,None,None,None]

notas[0]    = float(input("Tu nota de matemáticas: "))
notas[1]    = float(input("Tu nota de física: "))
notas[2]    = float(input("Tu nota de química: "))
notas[3]    = float(input("Tu nota de historia: "))
notas[4]    = float(input("Tu nota de lengua: "))

if (notas[0] > 4.50):
    asignaturas.remove("Matemáticas")
if (notas[1] > 4.50):
    asignaturas.remove("Física")
if (notas[2] > 4.50):
    asignaturas.remove("Química")
if (notas[3] > 4.50):
    asignaturas.remove("Historia")
if (notas[4] > 4.50):
    asignaturas.remove("Lengua")

print("Debes repetir las siguientes asignaturas:")
for x in asignaturas:
    print("\t -",x,sep="")