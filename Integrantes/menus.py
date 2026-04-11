from Integrantes.funciones import *
from General.clearConsole import *
from Integrantes.roles import*



def imprimirMenuIntegrantes(ListaIntegrantes, ListaRoles):
    activo=True
    
    while activo:
        clearConsole()
        print("[Menu Principal > *Integrantes*]")
        print()
        print("1. Ver integrantes")
        print("2. Agregar integrante")
        print("3. Editar integrante")
        print("4. Eliminar integrante")
        print("5. Ver roles")
        print("0. Volver atras")
        opcion=input("Seleccione una opcion: ")
        if opcion=="1":
            clearConsole()
            ver_integrantes(ListaIntegrantes)
        elif opcion=="2":
            clearConsole()
            agregar_integrante(ListaIntegrantes)
        elif opcion=="3":
            clearConsole()
            editar_integrante(ListaIntegrantes)
        elif opcion=="4":
            clearConsole()
            eliminar_integrante(ListaIntegrantes)
        elif opcion=="5":
            clearConsole()
            imprimirMenuRoles(ListaRoles)
        elif opcion=="0":
           activo=False 
        else:
            print("Opcion invalida. Intente nuevamente.")
