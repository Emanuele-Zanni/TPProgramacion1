"""Punto de entrada de la aplicación de seguimiento de proyectos."""

from Database.usuarios import menuAcceso
from General.clearConsole import clearConsole
from General.persistencia import (
    RUTA_DATOS_JSON,
    RUTA_ROLES_TXT,
    cargar_datos_json,
    cargar_roles_txt,
    guardar_datos_json,
    guardar_roles_txt,
)
from Integrantes.menus import imprimirMenuIntegrantes
from Proyectos.menus import imprimirMenuProyectos
from Stats.menu import imprimirMenuStats


USUARIOS_INICIALES = {
    "admin": {
        "id": 1,
        "password": "1234",
        "clearance": 3,
        "projects": [],
    },
    "manager": {
        "id": 2,
        "password": "5555",
        "clearance": 2,
        "projects": [],
    },
    "integrante": {
        "id": 3,
        "password": "123",
        "clearance": 1,
        "projects": [],
    },
}
ROLES_INICIALES = [[1, "Desarrollador"], [2, "QA"]]


def cargar_sistema():
    """Carga memoria desde disco y crea datos mínimos en la primera ejecución."""
    datos = cargar_datos_json(RUTA_DATOS_JSON)

    roles = cargar_roles_txt(RUTA_ROLES_TXT)
    if len(datos["usuarios"]) == 0:
        datos["usuarios"] = {
            nombre: {
                "id": valores["id"],
                "password": valores["password"],
                "clearance": valores["clearance"],
                "projects": valores["projects"][:],
            }
            for nombre, valores in USUARIOS_INICIALES.items()
        }
        guardar_datos_json(
            RUTA_DATOS_JSON, datos["proyectos"], datos["usuarios"]
        )
    if len(roles) == 0:
        roles.extend([rol[:] for rol in ROLES_INICIALES])
        guardar_roles_txt(RUTA_ROLES_TXT, roles)
    return datos["proyectos"], datos["usuarios"], roles


def guardar_sistema(proyectos, usuarios, roles):
    guardar_datos_json(RUTA_DATOS_JSON, proyectos, usuarios)
    guardar_roles_txt(RUTA_ROLES_TXT, roles)


def ejecutar():
    try:
        proyectos, usuarios, roles = cargar_sistema()
    except (ValueError, OSError) as error:
        print(f"\033[31m[ERROR] No se pudo iniciar la aplicación: {error}\033[0m")
        return
    aplicacion_activa = True

    while aplicacion_activa:
        credencial = menuAcceso(usuarios, roles)
        sesion_activa = True

        while sesion_activa:
            clearConsole()
            print("\033[33m[Menú principal]\033[0m\n")
            print("1. Proyectos")
            print("2. Personal")
            print("3. Estadísticas")
            print("4. Cerrar sesión")
            print("0. Cerrar programa")
            opcion = input("• Seleccione una opción: ").strip()

            try:
                if opcion == "1":
                    imprimirMenuProyectos(proyectos, usuarios, credencial)
                    guardar_sistema(proyectos, usuarios, roles)
                elif opcion == "2":
                    imprimirMenuIntegrantes(
                        usuarios, roles, credencial, proyectos
                    )
                    guardar_sistema(proyectos, usuarios, roles)
                elif opcion == "3":
                    imprimirMenuStats(proyectos, usuarios, roles)
                elif opcion == "4":
                    guardar_sistema(proyectos, usuarios, roles)
                    sesion_activa = False
                elif opcion == "0":
                    guardar_sistema(proyectos, usuarios, roles)
                    sesion_activa = False
                    aplicacion_activa = False
                else:
                    input("\033[31m[ERROR] Opción inválida. Presione Enter.\033[0m")
            except OSError as error:
                input(f"\033[31m[ERROR] No se pudo persistir la operación: {error}\033[0m")


if __name__ == "__main__":
    ejecutar()
