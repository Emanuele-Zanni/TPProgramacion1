from General.clearConsole import clearConsole
from General.formato import imprimir_tabla, imprimir_titulo


def mostrarListaIntegrantes(ListaUsuarios):
    imprimir_titulo("Lista de Integrantes")
    columnas = [
        {"titulo": "Usuario", "min": 18, "peso": 4},
        {"titulo": "Acceso", "min": 8, "peso": 1},
        {"titulo": "Proyectos", "min": 10, "peso": 1},
        {"titulo": "Tareas", "min": 8, "peso": 1},
    ]
    filas = []
    for usuario, datos in ListaUsuarios.items():
        clearance = datos.get("clearance", "")
        proyectos = datos.get("projects", [])
        cantidad_proyectos = len(proyectos)
        cantidad_tareas = sum(len(proyecto.get("tareas", [])) for proyecto in proyectos)
        filas.append([
            usuario.capitalize(),
            clearance,
            cantidad_proyectos,
            cantidad_tareas,
        ])
    imprimir_tabla(columnas, filas)
    

def ver_integrantes(ListaUsuarios):
    clearConsole()
    print("\033[33m[Menu Principal > Personal > *Ver Integrantes*]\033[0m")
    if len(ListaUsuarios) == 0:
        print()
        input("No hay integrantes registrados")
    else:
        mostrarListaIntegrantes(ListaUsuarios)
        print()
        input("Presione cualquier tecla para continuar...")


def editar_integrante(ListaUsuarios, ListaRoles):
    clearConsole()
    print("\033[33m[Menu Principal > Personal > *Editar Integrantes*]\033[0m")
    print()

    if len(ListaUsuarios) == 0:
        input("No hay integrantes registrados")
        return

    mostrarListaIntegrantes(ListaUsuarios)
    print()

    usuario = input("• Ingrese el usuario del integrante a editar: ").lower().strip()

    if usuario == "":
        input("\033[31m[ERROR] El usuario no puede estar vacio.\033[0m")
    elif usuario not in ListaUsuarios:
        input("\033[31m[ERROR] El integrante ingresado no existe.\033[0m")
    else:
        print()
        print("1. Cambiar nombre de usuario")
        print("2. Cambiar nivel de Acceso")
        print()
        opcion = input("• Seleccione una opción: ")

        if opcion == "1":
            nuevo_usuario = input("• Ingrese el nuevo nombre de usuario: ").lower().strip()

            if nuevo_usuario == "":
                input("\033[31m[ERROR] El usuario no puede estar vacio.\033[0m")
            elif nuevo_usuario in ListaUsuarios:
                input("\033[31m[ERROR] El usuario ingresado ya existe.\033[0m")
            elif nuevo_usuario[0].isdigit():
                input("\033[31m[ERROR] El usuario no puede empezar con un numero.\033[0m")
            else:
                ListaUsuarios[nuevo_usuario] = ListaUsuarios.pop(usuario)
                input("\033[92m[EXITO] Usuario editado correctamente.\033[0m")

        elif opcion == "2":
            nuevo_clearance = input("• Ingrese el nuevo nivel de acceso: ")

            if nuevo_clearance == "":
                input("\033[31m[ERROR] El nivel de acceso no puede estar vacio.\033[0m")
            elif nuevo_clearance.isdigit() == False:
                input("\033[31m[ERROR] El nivel de acceso debe ser un numero.\033[0m")
            else:
                ListaUsuarios[usuario]["clearance"] = int(nuevo_clearance)
                input("\033[92m[EXITO] Acceso editado correctamente.\033[0m")

        else:
            input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")


def eliminar_integrante(ListaUsuarios):
    clearConsole()
    print("\033[33m[Menu Principal > Personal > *Eliminar Integrante*]\033[0m")
    print()

    if len(ListaUsuarios) == 0:
        input("No hay integrantes registrados")
        return

    mostrarListaIntegrantes(ListaUsuarios)
    print()

    usuario = input("• Ingrese el usuario del integrante a eliminar: ").lower().strip()

    if usuario == "":
        input("\033[31m[ERROR] El usuario no puede estar vacio.\033[0m")
    elif usuario not in ListaUsuarios:
        input("\033[31m[ERROR] El integrante ingresado no existe.\033[0m")
    else:
        if len(ListaUsuarios[usuario].get("projects", [])) > 0:
            input("\033[31m[ERROR] No se puede eliminar un integrante asignado a proyectos.\033[0m")
            return
        del ListaUsuarios[usuario]
        input("\033[92m[EXITO] Integrante eliminado correctamente.\033[0m")
