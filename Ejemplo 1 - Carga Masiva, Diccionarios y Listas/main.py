import os

usuario = 'admin'
password = 'admin'

diccionarioDatos = dict()
listaAFN = []
contadorAFD = 0

def menu():
    print('########## LOGIN ##########')
    ingresarUsuario = input("Ingresa el usuario: ")
    ingresarPassword = input("Ingresar la contraseña: ")

    if ingresarUsuario == usuario and ingresarPassword == password:
        print('\nBienvenido usuario administrador. \n')
        MenuPrincipal()

    else:
        print('\nUsuario o contraseña inválidos, por favor vuelva a intentarlo.\n')
        menu()


def MenuPrincipal():
    print('########## MENÚ PRINCIPAL ##########')
    print("\t1. Cargar archivo .afd")
    print("\t2. Cargar archivo .afn")
    print("\t3. Ayuda")
    print("\t4. Salir")
    print("##############################")

    while True:
        # Solicitamos un número al usuario para poder navegar en el menú
        opcionMenu = input("Insertar un número para la evaluación: ")
        if opcionMenu.isdigit():
            opcionMenu = int(opcionMenu)
            if opcionMenu == 1:
                cargarAFD(diccionarioDatos, contadorAFD)
            elif opcionMenu == 2:
                cargarAFN()
            elif opcionMenu == 3:
                print(
                    "Elder Anibal Pum Rojas\n201700761\nLenguajes Formales y de Programación 'P'")
                MenuPrincipal()
            elif opcionMenu == 4:
                print("\nRegresando al login.\n")
                menu()
            else:
                print("\nIngrese una opción válida por favor. \n")
        else:
            print("\nIngrese una opción válida por favor. \n")

def cargarAFD(diccionario, contador):
    print("\nHa seleccionado la opción #1.\n")
    path = input("\nIngrese el nombre del archivo: ")

    while True:
        nombre, extension = os.path.splitext(path)
        if extension == ".afd":
            nombreAFD = nombre
            break
        else:
            path = input("\nIngrese el nombre del archivo: ")

    with open(path, "r") as archivo:
        for linea in archivo:
            arrayDatos = linea.replace(",", " ").split()
            arrayNumeros = linea.replace("afd"," ").split()
            for i in range(len(arrayDatos)):
                diccionario[arrayNumeros[i]] = arrayDatos[i]
    print(diccionario)

def cargarAFN():
    print("\nHa seleccionado la opción #2.\n")
    path = input("\nIngrese el nombre del archivo: ")

    while True:
        nombre, extension = os.path.splitext(path)
        if extension == ".afn":
            nombreAFD = nombre
            break
        else:
            path = input("\nIngrese el nombre del archivo: ")

    with open(path, "r") as archivo:
        for lineaAFN in archivo:
            arrayAFN = lineaAFN.replace(","," ").split()
            for i in range(len(arrayAFN)):
                listaAFN.append(arrayAFN[i])
    print(arrayAFN)
    
menu()
