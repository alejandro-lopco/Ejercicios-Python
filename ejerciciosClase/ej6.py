#! /usr/bin/env python3
#   Juego de dados

import random

DADOS_MAQUINA = random.randint(1,6)
dadosJugador = int(input("Escoga un número del 1 al 6: "))

if  not dadosJugador  >= 1 or not dadosJugador  <= 6:
    print("Número no permitido.")
    dadosJugador = input("Escoga un número del 1 al 6: ")

print("Número de la Máquina: ",DADOS_MAQUINA)
print("Tu número: ",dadosJugador)

if (DADOS_MAQUINA > dadosJugador):
    print("Gana la Máquina.")
elif (DADOS_MAQUINA < dadosJugador):
    print("Ganaste.")
else:
    print("Empate.")