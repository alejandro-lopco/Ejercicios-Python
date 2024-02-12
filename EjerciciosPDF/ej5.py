#! /usr/bin/env python3
#Escribir un programa que compruebe una contraseña
#Criterios: 
#   Al menos 1 letra entre [a-z] 
#   Al menos 1 número entre [0-9] 
#   Al menos 1 letra entre [A-Z] 
#   Al menos 1 carácter de los siguientes [$#@] 
#   Longitud mínima de la contraseña: 6 
#   Longitud máxima de la contraseña: 12 
 
#El programa verificará según los criterios marcados. 
#La respuesta debe ser “correcta” o “incorrecta” 

PASSWD = str(input("Indica la contraseña: "))
crit1 = False
crit2 = False
crit3 = False
crit4 = False
crit5 = False

for x in PASSWD:
    if (x.islower() is True):
        crit1 = True
    if (x.isnumeric() is True):
        crit2 = True
    if (x.isupper() is True):
        crit3 = True
    if (x is '$' or 
        x is '#' or
        x is '@'):
        crit4 = True

if (len(PASSWD) >= 6 and len(PASSWD) < 12):
    crit5 = True

if (crit1 is True and
    crit2 is True and
    crit3 is True and
    crit4 is True and
    crit5 is True):
    print('Correcta')
else:
    print('Incorrecta')