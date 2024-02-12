#! /usr/bin/env Python3
# Alejandro López Corral
#
# Generador y comprobador de contraseñas
#   Comprueba si
#       - Tiene mayusculas y minusculas
#       - Tiene números
#       - Tiene tiene simbolos especiales
#       - Tiene un mínimo de 10 caracteres

import random
import string

SIMBOLOS_ESPECIALES = string.punctuation
MINUSCULAS_ASCII    = string.ascii_lowercase
MAYUSCULAS_ASCII    = string.ascii_uppercase
DIGITOS_ASCII       = string.digits

def comprobacionContrasena (passwd: str):
    chkMinus    = False
    chkMayus    = False
    chkNum      = False
    chkEspecial = False
    chkCarac    = False
    for x in passwd:
        if x in SIMBOLOS_ESPECIALES:
            chkEspecial = True
        if x.isupper() == True:
            chkMayus = True
        if x.islower() == True:
            chkMinus = True
        if x.isnumeric() == True:
            chkNum = True
    if len(passwd) >= 10:
        chkCarac = True
    chkTotal = [chkMinus,chkMayus,chkNum,chkEspecial,chkCarac]
    return chkTotal
    
contrasena = input("Indice su contraseña: ")
chkLista = comprobacionContrasena(contrasena)

if chkLista[0] == False:
    print("No hay minúsculas")
    for x in contrasena:
        if x.isalpha() == True:
            contrasena += x.lower()
            break

if chkLista[1] == False:
    print("No hay mayusculas")
    cantAdd = random.randint(1,10)
    for x in range(cantAdd):
        contrasena += random.choice(MAYUSCULAS_ASCII)

if chkLista[2] == False:
    print("No hay números")
    cantAdd = random.randint(1,10)
    for x in range(cantAdd):
        contrasena += random.choice(DIGITOS_ASCII)
    
if chkLista[3] == False:
    print("No hay caracteres especiales")
    cantAdd = random.randint(1,10)
    for x in range(cantAdd):
        contrasena += random.choice(SIMBOLOS_ESPECIALES)

if chkLista[4] == False:
    print("Es demasiado corta")
    contrasena = contrasena.zfill(10)

print("Tu nueva contraseña: ",contrasena)