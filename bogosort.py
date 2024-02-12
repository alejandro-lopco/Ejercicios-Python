import random
import time

LENGHT = 10
contador = 0
ordenado = False
lista = []

def check_sorted (list):
    for j in range(1, len(list)):
        if not list[j] > list[j - 1]:
            return False
    
    return True


for i in range(LENGHT):
    num = random.randint(0, 10000)
    lista.append(num)


print("Primera lista: ", lista)
start = time.time()

while not ordenado:

    ordenado = check_sorted(lista)

    if not ordenado:
        contador += 1
        random.shuffle(lista)
            
end = time.time()            
print('Resultado: ', lista)
print('Ciclos: ', contador)
print('Tiempo transcurrido: ', end-start, 's')