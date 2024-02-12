#! /usr/bin/env python3
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de
#su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede
#elegir un ingrediente además de la mozzarella y el tomate que están en todas las pizzas. Al final se
#debe mostrar por pantalla si la pizza elegida es vegetariana o no, y todos los ingredientes que lleva.

ingredientes = {
    'univ': [
        'Tomate',
        'Mozarella'
    ],
    'carn': [
        'Peperonni',
        'Pollo',
        'Carne Pícada',
        'Bacón'
    ],
    'vege': [
        'Pimiento Verde',
        'Pimiento Rojo',
        'Piña',
        '4 Quesos',
        'Huevo',
        'Perejil'
    ]
}

def addIngredientes(ingredientesLista,ingrediente):
    if (ingrediente in ingredientes['carn'] or
        ingrediente in ingredientes['univ'] or
        ingrediente in ingredientes['vege']):
        ingredientesLista.append(ingrediente)
    elif (ingrediente is '*'):
        print("Ha terminado su pizza.")

    else:
        print("Ingrediente no reconocido")

print("######Bienvenido a nuestra pizzeria######")

cliente = str(input("¿Es vegetariane (y/n)?"))
ingredientesCliente = [ingredientes['univ'][0],ingredientes['univ'][1]]

if (cliente is 'n'):
    print("----Escoga los ingredientes que desea----")
    print("---------------Ingredientes-------------")
    for x in ingredientes['univ']:
        print("\t",x)
    for x in ingredientes['carn']:
        print("\t",x)
    for x in ingredientes['vege']:
        print("\t",x)
elif (cliente is 'y'):
    print("----Escoga los ingredientes que desea----")
    print("---------------Ingredientes-------------")
    for x in ingredientes['univ']:
        print("\t",x)
    for x in ingredientes['vege']:
        print("\t",x)
else:
    print("Opción no reconocida.")

seleccionIngrediente = str(input("Indique un máximo de 4 ingredientes (* para salir): "))
addIngredientes(ingredientesCliente,seleccionIngrediente)
while (seleccionIngrediente != '*'):
    seleccionIngrediente = str(input("Indique el ingrediente que quiere (* para salir): "))
    addIngredientes(ingredientesCliente,seleccionIngrediente)

print("Los ingredientes que ha escogido son: ")
for x in ingredientesCliente:
    print("\t",x)