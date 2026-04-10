from Integrantes.funciones import *
from General.clearConsole import *
from Integrantes.roles import*



<<<<<<< HEAD
def imprimirMenuIntegrantes(ListaIntegrantes,ListaRoles):
    clearConsole()
    print("[Menu Principal > *Integrantes*]")
    print()
    print("1. Ver integrantes")
    print("2. Agregar integrante")
    print("3. Editar integrante")
    print("4. Eliminar integrante")
    print("5. Gestionar roles")
    opcion=input("Seleccione una opcion: ")
    if opcion=="1":
        ver_integrantes(ListaIntegrantes)
    elif opcion=="2":
        agregar_integrante(ListaIntegrantes)
    elif opcion=="3":
        editar_integrante(ListaIntegrantes)
    elif opcion=="4":
        eliminar_integrante(ListaIntegrantes)
    elif opcion=="5":
        imprimirMenuRoles(ListaRoles)
    else:
        print("Opcion invalida. Intente nuevamente.")
=======
def imprimirMenuIntegrantes(ListaIntegrantes):
    activo=True
    
    while activo:
        clearConsole()
        print("[Menu Principal > *Integrantes*]")
        print()
        print("1. Ver integrantes")
        print("2. Agregar integrante")
        print("3. Editar integrante")
        print("4. Eliminar integrante")
        print("0. Volver atras")
        opcion=input("Seleccione una opcion: ")
        if opcion=="1":
            ver_integrantes(ListaIntegrantes)
        elif opcion=="2":
            agregar_integrante(ListaIntegrantes)
        elif opcion=="3":
            editar_integrante(ListaIntegrantes)
        elif opcion=="4":
            eliminar_integrante(ListaIntegrantes)
        elif opcion=="0":
           activo=False 
        else:
            print("Opcion invalida. Intente nuevamente.")
>>>>>>> 1abf464305aacaba8085f5ba1e5d4bab5d0e6f1e
