from Integrantes.funciones import *
from General.clearConsole import *



def imprimirMenuIntegrantes(ListaIntegrantes):
    clearConsole()
    print("[Menu Principal > *Integrantes*]")
    print()
    print("1. Ver integrantes")
    print("2. Agregar integrante")
    print("3. Editar integrante")
    print("4. Eliminar integrante")
    opcion=input("Seleccione una opcion: ")
    if opcion=="1":
        ver_integrantes(ListaIntegrantes)
    elif opcion=="2":
        agregar_integrante(ListaIntegrantes)
    elif opcion=="3":
        editar_integrante(ListaIntegrantes)
    elif opcion=="4":
        eliminar_integrante(ListaIntegrantes)
    else:
        print("Opcion invalida. Intente nuevamente.")