#! /usr/bin/env python3
# Bubble Sort en Python
import random
import time

def generacionNumeros(list,len):
    MAXIMO = 10000
    for x in range(len):
        num = random.randint(1,MAXIMO)
        if num not in list:
            list.append(num)
        else:
            x-=1
    return list

def bubbleSort(list):
    LONGITUD = len(list)
    for i in range(LONGITUD-1):
        for j in range(0, LONGITUD-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
            else:
                continue
    print(list)

cant = int(input("¿Como de larga quieres la lista? "))
listaVacia = []
listaDesordenada = generacionNumeros(listaVacia,cant)

print(listaDesordenada)
print('---Iniciando Bubble Sort---')

start = time.time()
bubbleSort(listaDesordenada)
end = time.time()
print('---Finalización Bubble Sort---')
print('Tiempo Transcurrido:',end-start, 'segundos')
