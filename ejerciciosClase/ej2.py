#! /usr/bin/env python3
# Preguntar sobre 2 diferentes (limite 20)
# Al terminar de preguntar mostrar una gráfico de barras
cont = 1
contA = 0
contB = 0
while cont <= 20:
    print("Dato #", cont)
    opc = input("¿Prefiere la opción A o B? (* Para salir) ")
    if opc == "*":
        cont = 21
    elif opc == "a":
        contA+=1
    elif opc == "b":
        contB+=1
    else:
        print("Opción no permitida :(")
    cont+=1
porCientoA = round(float(contA / (cont-1)),4) * 100
porCientoB = round(float(contB / (cont-1)),4) * 100
print("Opción A","(",porCientoA,"% ): ")
for x in range(contA):
    print("/",end="")
print("\n")
print("Opción B","(",porCientoB,"% ): ")
for x in range(contB):
    print("/",end="")
print("\n")