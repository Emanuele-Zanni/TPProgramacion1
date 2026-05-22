from General.clearConsole import*
from Stats.funciones import*


def imprimirMenuStats(ListaProyectos, ListaUsuarios, ListaRoles):
    activo=True
    while activo:
        clearConsole()
        print("[*Menu Stats*]")
        print("")
        print("1. Ver Stats de proyectos")
        print("2. Ver Stats de integrantes")
        print("3. Ver Stats de roles")
        print("4. Ver todas las stats")
        print("0. Volver al menu principal")
        
        opcion=input("Selecione una opcion: ")
        if opcion == "1":
            clearConsole()
            ver_StatsProyectos(ListaProyectos)
            input("Presione enter para continuar...")

        elif opcion == "2":
            clearConsole()
            ver_StatsIntegrantes(ListaUsuarios)
            input("Presione enter para continuar...")
        
        elif opcion == "3":
            clearConsole()
            ver_StatsRoles(ListaRoles)
            input("Presione enter para continuar...")
        
        elif opcion == "4":
            clearConsole()
            ver_StatsTotal(ListaProyectos, ListaUsuarios, ListaRoles)
            print()
            input("Presione enter para continuar...")
                    
        elif opcion == "0":
                activo=False
        else:
            print()
            input("Opcion invalida. Intente nuevamente.")
