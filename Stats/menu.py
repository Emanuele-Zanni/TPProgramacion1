from General.clearConsole import*
from Stats.funciones import*


def imprimirMenuStats(ListaProyectos, ListaIntegrantes, ListaRoles):
    activo=True
    while activo:
        clearConsole()
        print("[*Menu Stats*]")
        print("")
        print("1. Ver Stats de proyectos")
        print("2. Ver Stats de integrantes")
        print("3. Ver Stats de roles")
        print("0. Volver al menu principal")
        
        opcion=input("Selecione una opcion: ")
        
        if opcion == "1":
            input(f"Cantidad de proyectos: {ver_StatsProyectos(ListaProyectos)}")

        elif opcion == "2":
            input(f"Cantidad de integrantes: {ver_StatsIntegrantes(ListaIntegrantes)}")

        elif opcion == "3":
            input(f"Cantidad de roles: {ver_StatsRoles(ListaRoles)}")

        elif opcion == "0":
                activo=False
        else:
            print()
            input("Opcion invalida. Intente nuevamente.")
