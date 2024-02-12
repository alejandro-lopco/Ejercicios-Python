#! /usr/bin/env python3
# Cambio de dividas mediante la integración gráfica de YAD en Linux Bash
import os

DOLAR       = 1.08
YEN         = 159.44
RUBLO       = 97.45
DIRHAM      = 10.82
PARGENTINO  = 892.90

os.system("yad --entry --title='Cambio Divisas' --text='Indique cantidad en €:' --center --width=250 > x.tmp")
os.system("yad --entry --title='Cambio Divisas' --text='Indique la moneda de la que quiere cambio:' --center --width=250 > y.tmp")

fileDinero = open('x.tmp','r')
fileMoneda = open('y.tmp','r') 

dinero = int(fileDinero.readline())
moneda = str(fileMoneda.readline()).strip()

print(dinero)
print(moneda)

if moneda   == 'dolar':
    res = dinero * DOLAR
elif moneda == 'yen':
    res = dinero * YEN
elif moneda == 'rublo':
    res = dinero * RUBLO
elif moneda == 'dirham':
    res = dinero * DIRHAM
elif moneda == 'peso argentino':
    res = dinero * PARGENTINO
else:
    print("Moneda no reconocida")
    fileDinero.close()
    fileMoneda.close()

    os.system("rm x.txt")
    os.system("rm y.txt")
    exit()


textVar = str(dinero)+'->'+str(res)

os.environ['strResultado'] = textVar

os.system("yad --info --title='Cambio Divisas' --text=${strResultado} --center --width=250")

fileDinero.close()
fileMoneda.close()

os.system("rm x.tmp")
os.system("rm y.tmp")