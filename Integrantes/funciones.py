from General.clearConsole import *
from Integrantes.roles import *
from Database.usuarios import signUp
from General.formato import imprimir_titulo


def mostrarListaIntegrantes(ListaUsuarios):
    imprimir_titulo("Lista de Integrantes")
    
    print(
        f"{'Usuario':<20}"
        f"{'Rol':<20}"
        f"{'Acceso':<10}"
        f"{'Tareas':<20}"
    )
    
    print("=" * 70)

    for usuario, datos in ListaUsuarios.items():
        rol = datos.get("rol", "Ninguno")
        clearance = datos.get("clearance", "")
        tareas = str(datos.get("tareas", []))

        print(
            f"{usuario.capitalize():<20}"
            f"{rol:<20}"
            f"{clearance:<10}"
            f"{tareas:<20}"
        )
    print("")
    

def ver_integrantes(ListaUsuarios):
    clearConsole()
    print("\033[33m[Menu Principal > Personal > *Ver Integrantes*]\033[0m")
    print()
    if len(ListaUsuarios) == 0:
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
        print("2. Cambiar rol")
        print("3. Cambiar nivel de Acceso")
        print()
        opcion = input("• Seleccione una opcion: ")

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
                input("[EXITO] Usuario editado correctamente.")

        elif opcion == "2":
            if len(ListaRoles) == 0:
                input("No hay roles existentes, por favor agregue un rol")
                return

            mostrarListaRoles(ListaRoles)
            editarRol = input("• Ingrese el ID del nuevo rol: ")

            if editarRol == "":
                input("\033[31m[ERROR] El rol no puede estar vacio.\033[0m")
            elif editarRol.isdigit() == False:
                input("\033[31m[ERROR] Debe ingresar un numero.\033[0m")
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
                    input("\033[31m[ERROR] El rol no existe.\033[0m")

        elif opcion == "3":
            nuevo_clearance = input("• Ingrese el nuevo nivel de acceso: ")

            if nuevo_clearance == "":
                input("\033[31m[ERROR] El nivel de acceso no puede estar vacio.\033[0m")
            elif nuevo_clearance.isdigit() == False:
                input("\033[31m[ERROR] El nivel de acceso debe ser un numero.\033[0m")
            else:
                ListaUsuarios[usuario]["clearance"] = int(nuevo_clearance)
                input("[EXITO] Acceso editado correctamente.")

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
        del ListaUsuarios[usuario]
        input("[EXITO] Integrante eliminado correctamente.")
