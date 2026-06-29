from General.clearConsole import*
from Stats.funciones import*


def imprimirMenuStats(ListaProyectos, ListaUsuarios, ListaRoles):
    activo=True
    while activo:
        clearConsole()
        print("\033[33m[Menu principal > *Stats*]\033[0m")
        print("")
        print("1. Ver Stats de proyectos")
        print("2. Ver Stats de integrantes")
        print("3. Ver Stats de roles")
        print("4. Ver resumen ejecutivo")
        print("0. Volver al menu principal")
        
        opcion=input("Selecione una opcion: ")
        if opcion == "1":
            ver_StatsProyectos(ListaProyectos, ListaUsuarios)
        
        elif opcion == "2":
            ver_StatsIntegrantes(ListaUsuarios, ListaProyectos)
        
        elif opcion == "3":
            ver_StatsRoles(ListaRoles, ListaUsuarios)

        elif opcion == "4":
            ver_StatsTotal(ListaProyectos, ListaUsuarios, ListaRoles)
                    
        elif opcion == "0":
                activo=False
                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
        else:
            print()
            input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
