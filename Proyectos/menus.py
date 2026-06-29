"""Menu principal de proyectos."""

from General.clearConsole import clearConsole
from General.persistencia import RUTA_DATOS_JSON, guardar_datos_json
from Proyectos.funciones import (
    crear_proyecto,
    editar_proyecto,
    eliminar_proyecto,
    seleccionar_proyecto,
)


def imprimirMenuProyectos(ListaProyectos, ListaUsuarios, credencial):
    activo = True
    while activo:
        clearConsole()
        print("\033[33m[Menu principal > Proyectos]\033[0m\n")
        print("1. Ver y seleccionar proyectos")
        if credencial["clearance"] >= 2:
            print("2. Crear proyecto")
            print("3. Editar proyecto")
            print("4. Eliminar proyecto")
        print("0. Volver")
        opcion = input("• Seleccione una opcion: ").strip()

        if opcion == "1":
            seleccionar_proyecto(ListaProyectos, ListaUsuarios, credencial)
        elif opcion == "2" and credencial["clearance"] >= 2:
            crear_proyecto(ListaProyectos, ListaUsuarios, credencial)
        elif opcion == "3" and credencial["clearance"] >= 2:
            editar_proyecto(ListaProyectos, ListaUsuarios, credencial)
        elif opcion == "4" and credencial["clearance"] >= 2:
            eliminar_proyecto(ListaProyectos, ListaUsuarios)
        elif opcion == "0":
            activo = False
            continue
        else:
            input("\033[31m[ERROR] Opcion invalida.\033[0m")
            continue

        guardar_datos_json(RUTA_DATOS_JSON, ListaProyectos, ListaUsuarios)
