#! /usr/bin/env python3
# Escribir un programa que añada un espacio delante de cada letra mayúscula, excepto la primera. 
# También debe cambiar la mayúscula por una minúscula, excepto la primera
texto = str(input("Indica el texto: "))
res = texto[0]

for x in texto[1:]:
    if (x.isupper() is True):
        x = " " + x
        res += x
    else:
        res += x

print(res)