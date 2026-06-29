"""CRUD interactivo de roles persistidos en archivo plano."""

from General.clearConsole import clearConsole
from General.formato import imprimir_tabla, imprimir_titulo
from General.persistencia import (
    RUTA_ROLES_TXT,
    crear_rol_txt,
    eliminar_rol_txt,
    modificar_rol_txt,
)
from General.utilidades import buscar_posicion_por_id
from General.validaciones import pedir_confirmacion


def imprimirMenuRoles(ListaRoles, credencial, ListaUsuarios=None):
    activo = True
    while activo:
        clearConsole()
        print("\033[33m[Menú principal > Personal > Roles]\033[0m\n")
        print("1. Ver roles")
        if credencial["clearance"] >= 3:
            print("2. Crear rol")
            print("3. Editar rol")
            print("4. Eliminar rol")
        print("0. Volver")
        opcion = input("• Seleccione una opción: ").strip()

        if opcion == "1":
            ver_roles(ListaRoles)
        elif opcion == "2" and credencial["clearance"] >= 3:
            crear_roles(ListaRoles)
        elif opcion == "3" and credencial["clearance"] >= 3:
            editar_rol(ListaRoles)
        elif opcion == "4" and credencial["clearance"] >= 3:
            eliminar_rol(ListaRoles, ListaUsuarios)
        elif opcion == "0":
            activo = False
        else:
            input("\033[31m[ERROR] Opción inválida.\033[0m")


def crear_roles(ListaRoles):
    clearConsole()
    print("\033[33m[Menú principal > Personal > Roles > Crear]\033[0m\n")
    nombre = input("• Nombre del nuevo rol (0 para cancelar): ").strip()
    if nombre == "0":
        return False
    try:
        nuevo = crear_rol_txt(ListaRoles, nombre, RUTA_ROLES_TXT)
    except (TypeError, ValueError, OSError) as error:
        input(f"\033[31m[ERROR] {error}\033[0m")
        return False
    input(f"[ÉXITO] Rol {nuevo[1]} creado con ID {nuevo[0]}.")
    return True


def editar_rol(ListaRoles):
    clearConsole()
    if len(ListaRoles) == 0:
        input("No hay roles registrados.")
        return False
    mostrarListaRoles(ListaRoles)
    valor = input("• ID del rol a editar (0 para cancelar): ").strip()
    if valor == "0":
        return False
    if not valor.isdigit():
        input("\033[31m[ERROR] El ID debe ser un número.\033[0m")
        return False
    nombre = input("• Nuevo nombre: ").strip()
    try:
        resultado = modificar_rol_txt(
            ListaRoles, int(valor), nombre, RUTA_ROLES_TXT
        )
    except (TypeError, ValueError, OSError) as error:
        input(f"\033[31m[ERROR] {error}\033[0m")
        return False
    if not resultado:
        input("\033[31m[ERROR] El rol no existe.\033[0m")
        return False
    input("[ÉXITO] Rol actualizado.")
    return True


def eliminar_rol(ListaRoles, ListaUsuarios=None):
    clearConsole()
    if len(ListaRoles) == 0:
        input("No hay roles registrados.")
        return False
    mostrarListaRoles(ListaRoles)
    valor = input("• ID del rol a eliminar (0 para cancelar): ").strip()
    if valor == "0":
        return False
    if not valor.isdigit():
        input("\033[31m[ERROR] El ID debe ser un número.\033[0m")
        return False
    posicion = buscar_posicion_por_id(ListaRoles, int(valor))
    if posicion == -1:
        input("\033[31m[ERROR] El rol no existe.\033[0m")
        return False

    nombre_rol = ListaRoles[posicion][1]
    if ListaUsuarios is not None:
        rol_en_uso = any(
            relacion.get("rol") == nombre_rol
            for datos in ListaUsuarios.values()
            for relacion in datos.get("projects", [])
        )
        if rol_en_uso:
            input("\033[31m[ERROR] No se puede eliminar un rol asignado.\033[0m")
            return False

    if not pedir_confirmacion(f"¿Eliminar el rol {nombre_rol}? (s/n): "):
        input("[CANCELADO] No se realizaron cambios.")
        return False
    try:
        eliminar_rol_txt(ListaRoles, int(valor), RUTA_ROLES_TXT)
    except OSError as error:
        input(f"\033[31m[ERROR] {error}\033[0m")
        return False
    input("[ÉXITO] Rol eliminado.")
    return True


def mostrarListaRoles(ListaRoles):
    imprimir_titulo("Lista de Roles")
    imprimir_tabla(
        [
            {"titulo": "ID", "min": 4, "peso": 1},
            {"titulo": "Nombre del rol", "min": 20, "peso": 4},
        ],
        [[rol[0], rol[1]] for rol in ListaRoles],
    )


def ver_roles(ListaRoles, mode=True):
    clearConsole()
    if len(ListaRoles) == 0:
        input("No hay roles registrados.")
        return
    mostrarListaRoles(ListaRoles)
    if mode:
        input("Presione Enter para continuar.")
