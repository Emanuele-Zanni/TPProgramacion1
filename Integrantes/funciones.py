from General.clearConsole import *
from Integrantes.roles import *
from Database.usuarios import signUp


def mostrarListaIntegrantes(ListaUsuarios):
    print(f"{'Usuario':<20}{'Rol':<20}{'Acceso':<10}{'Tareas':<20}")
    print("-" * 70)

    for usuario, datos in ListaUsuarios.items():
        rol = datos.get("rol", "Ninguno")
        clearance = datos.get("clearance", "")
        tareas = str(datos.get("tareas", []))
        print(f"{usuario.capitalize():<20}{rol:<20}{clearance:<10}{tareas:<20}")


def ver_integrantes(ListaUsuarios):
    clearConsole()
    print("[Menu Principal > Personal > *Ver Integrantes*]")
    print()
    if len(ListaUsuarios) == 0:
        input("No hay integrantes registrados")
    else:
        mostrarListaIntegrantes(ListaUsuarios)
        input("\nPresione cualquier tecla para continuar...")


# def agregar_integrante(ListaUsuarios, ListaRoles):
#     signUp(ListaUsuarios, ListaRoles)


def editar_integrante(ListaUsuarios, ListaRoles):
    clearConsole()
    print("[Menu Principal > Personal > *Editar Integrantes*]")
    print()

    if len(ListaUsuarios) == 0:
        input("No hay integrantes registrados")
        return

    mostrarListaIntegrantes(ListaUsuarios)
    print()

    usuario = input("Ingrese el usuario del integrante a editar: ").lower().strip()

    if usuario == "":
        input("[ERROR] El usuario no puede estar vacio")
    elif usuario not in ListaUsuarios:
        input("[ERROR] El integrante ingresado no existe")
    else:
        print()
        print("1. Cambiar nombre de usuario")
        print("2. Cambiar rol")
        print("3. Cambiar nivel de Acceso")
        print()
        opcion = input("• Seleccione una opcion: ")

        if opcion == "1":
            nuevo_usuario = input("Ingrese el nuevo nombre de usuario: ").lower().strip()

            if nuevo_usuario == "":
                input("[ERROR] El usuario no puede estar vacio")
            elif nuevo_usuario in ListaUsuarios:
                input("[ERROR] El usuario ingresado ya existe")
            elif nuevo_usuario[0].isdigit():
                input("[ERROR] El usuario no puede empezar con un numero")
            else:
                ListaUsuarios[nuevo_usuario] = ListaUsuarios.pop(usuario)
                input("[EXITO] Usuario editado correctamente.")

        elif opcion == "2":
            if len(ListaRoles) == 0:
                input("No hay roles existentes, por favor agregue un rol")
                return

            mostrarListaRoles(ListaRoles)
            editarRol = input("Ingrese el ID del nuevo rol: ")

            if editarRol == "":
                input("[ERROR] El rol no puede estar vacio")
            elif editarRol.isdigit() == False:
                input("[ERROR] Debe ingresar un numero")
            else:
                editarRol = int(editarRol)
                rolEncontrado = False

                for rol in ListaRoles:
                    if rol[0] == editarRol:
                        ListaUsuarios[usuario]["rol"] = rol[1]
                        rolEncontrado = True

                if rolEncontrado:
                    input("[EXITO] Rol editado correctamente.")
                else:
                    input("[ERROR] El rol no existe")

        elif opcion == "3":
            nuevo_clearance = input("Ingrese el nuevo nivel de acceso: ")

            if nuevo_clearance == "":
                input("[ERROR] El nivel de acceso no puede estar vacio")
            elif nuevo_clearance.isdigit() == False:
                input("[ERROR] El nivel de acceso debe ser un numero")
            else:
                ListaUsuarios[usuario]["clearance"] = int(nuevo_clearance)
                input("[EXITO] Acceso editado correctamente.")

        else:
            input("[ERROR] Opcion invalida. Intente nuevamente.")


def eliminar_integrante(ListaUsuarios):
    clearConsole()
    print("[Menu Principal > Personal > *Eliminar Integrante*]")
    print()

    if len(ListaUsuarios) == 0:
        input("No hay integrantes registrados")
        return

    mostrarListaIntegrantes(ListaUsuarios)
    print()

    usuario = input("Ingrese el usuario del integrante a eliminar: ").lower().strip()

    if usuario == "":
        input("[ERROR] El usuario no puede estar vacio")
    elif usuario not in ListaUsuarios:
        input("[ERROR] El integrante ingresado no existe")
    else:
        del ListaUsuarios[usuario]
        input("[EXITO] Integrante eliminado correctamente.")
