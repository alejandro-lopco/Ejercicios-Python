#! /usr/bin/env python3
# Comprobar si la palabra que hemos introducido es palíndromo
# Palíndromo es cuando una palabra puede leerse igual por el principio y el final
input = list(input("Comprobador de palíndromos o capicuas: "))
palabra = list()
for x in input:
    if x == " ":
        continue
    else:
        palabra.append(x)
palabraRev = list()
for y in palabra[::-1]:
    palabraRev.append(y)
if palabra == palabraRev:
    print("Esta palabra es un palíndromo")
else:
    print("Esta palabra NO es un palíndromo")