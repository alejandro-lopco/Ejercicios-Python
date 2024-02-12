#! /usr/bin/env python3
# Diccionario de alumnos
#   DNI: [dicc datos]
#   claves diccionario datos: [nombre,apellido,edad,curso,notas (3 mínimo)]
"""   MENU: 
        1 - nuevo alumno
        2 - Eliminar alumno
        3 - Consultar notas por alumno
        4 - Consultar nota curso 
        5 - Saliendo del programa
"""
def menu():
    print('1 - Nuevo alumno')
    print('2 - Eliminar alumno')
    print('3 - Consultar notas por alumno')
    print('4 - Consultar nota curso')
    print('5 - Salir del programa')
    global opc
    opc = int(input('Escoga la opción que desee: '))
    return opc
def listCursos():
    global cursos
    cursos = []
    for x in alumnos:
        rep = alumnos[x]['curso']
        if rep in cursos:
            continue
        else:
            cursos.append(rep)
    print(cursos)
def addAlumno():
    print("---Nuevo Alumno---")
    newKey = input("Introduce el DNI: ")
    newName = input("Introduce el nombre: ")
    newSurname = input("Introduce el apellido: ")
    newAge = input("Introduce la edad: ")
    newClass = input("Introduce el curso: ")
    newGrades = input("Introduce 3 notas separadas de un espacio: ")
    addData = {
        newKey: {
        'nombre':newName,
        'apellido':newSurname,
        'edad':newAge,
        'curso':newClass,
        'notas':newGrades
        }
    }
    alumnos.update(addData)
def notasAlumno():
    print("---Consultar notas por alumno---")
    search = input("Introduce el DNI del alumno")
    if (search in alumnos):
        print('Alumno: ',alumnos[search]['nombre'])
        print('Nota 1: ',alumnos[search]['notas'][0])
        print('Nota 2: ',alumnos[search]['notas'][1])
        print('Nota 3: ',alumnos[search]['notas'][2])
    else:
        print('No se encuentra el alumno')
def notasCurso():
    search = input("Introduce el nombre del curso: ")
    if (search in cursos):
        for x in alumnos:
            if (alumnos[x]['curso'] == search):
                print("Nombre: ",alumnos[x]['nombre'])
                print("Edad: ",alumnos[x]['edad'])
                print("Nota 1: ",alumnos[x]['notas'][0])
                print("Nota 2: ",alumnos[x]['notas'][1])
                print("Nota 3: ",alumnos[x]['notas'][2])
                print("---------------------------------")
            else:
                continue
    else:
        print("Curso no encontrado")            
alumnos = {
    '12345678A': {
        'nombre':'Alejandro',
        'apellido':'López Corral',
        'edad':19,
        'curso':'2º ASIR',
        'notas':[7,5,9]
    },
    '98765432B': {
        'nombre':'Marina',
        'apellido':'Manini Ramirez',
        'edad':19,
        'curso':'2º Fotografía',
        'notas':[10,9,8]
    },
    '11111111C': {
        'nombre':'Joan',
        'apellido':'Martinez Sancho',
        'edad':19,
        'curso':'2º DAM',
        'notas':[10,6,5]
    },
    '22222222D': {
        'nombre':'Martín',
        'apellido':'Zapata Rodriguez',
        'edad':19,
        'curso':'2º Sonido',
        'notas':[7,6,9]
    },
    '33333333E': {
    'nombre':'Pepe',
    'apellido':'Oviedo López',
    'edad':23,
    'curso':'2º Sonido',
    'notas':[9,5,6]
    }
}
menu()
match opc:
    case 1:
        addAlumno()
        menu()
    case 2:
        print("---Eliminar Alumno---")
        search = input("Introduce el DNI del alumno que vaya a borrar")
        del(alumnos[search])
        menu()
    case 3:
        notasAlumno()
        menu()
    case 4:
        print("---Consultar notas por curso---")
        listCursos()
        notasCurso()
        menu()
    case 5:
        print("---SALIENDO DEL PROGRAMA---")
