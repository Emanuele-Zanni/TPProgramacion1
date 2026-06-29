"""Menú principal de integrantes."""

from Database.usuarios import signUp
from General.clearConsole import clearConsole
from General.persistencia import RUTA_DATOS_JSON, guardar_datos_json
from Integrantes.funciones import (
    editar_integrante,
    eliminar_integrante,
    ver_integrantes,
)
from Integrantes.roles import imprimirMenuRoles


def imprimirMenuIntegrantes(
    ListaUsuarios, ListaRoles, credencial, ListaProyectos=None
):
    activo = True
    while activo:
        clearConsole()
        print("\033[33m[Menú principal > Personal]\033[0m\n")
        print("1. Ver integrantes")
        if credencial["clearance"] >= 2:
            print("2. Editar integrante")
            print("3. Gestionar roles")
        if credencial["clearance"] >= 3:
            print("4. Eliminar integrante")
            print("5. Registrar usuario")
        print("0. Volver")
        opcion = input("• Seleccione una opción: ").strip()

        modifico_usuarios = False
        if opcion == "1":
            ver_integrantes(ListaUsuarios)
        elif opcion == "2" and credencial["clearance"] >= 2:
            editar_integrante(ListaUsuarios, ListaRoles)
            modifico_usuarios = True
        elif opcion == "3" and credencial["clearance"] >= 2:
            imprimirMenuRoles(ListaRoles, credencial, ListaUsuarios)
        elif opcion == "4" and credencial["clearance"] >= 3:
            eliminar_integrante(ListaUsuarios)
            modifico_usuarios = True
        elif opcion == "5" and credencial["clearance"] >= 3:
            signUp(ListaUsuarios, ListaRoles, True, False)
            modifico_usuarios = True
        elif opcion == "0":
            activo = False
            continue
        else:
            input("\033[31m[ERROR] Opción inválida.\033[0m")
            continue

        if modifico_usuarios and ListaProyectos is not None:
            guardar_datos_json(
                RUTA_DATOS_JSON, ListaProyectos, ListaUsuarios
            )
