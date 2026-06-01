from General.clearConsole import *
from Integrantes.roles import *


def menuAcceso(usuarios, listaRoles):
    while True:
        clearConsole()
        print("""\033[33m[*Menu de Acceso*]\033[0m

1. Iniciar Sesion
2. Registrarse
 """)
        choice = input("Ingrese una opcion: ")
        if choice == "1":
            return login(usuarios)
        elif choice == "2":
            return signUp(usuarios, listaRoles)
        else:
            input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")


def login(usuarios):
    on = True
    p1, p2 = True, False
    isPasswordCorrect = False
    isUserReal = False

    while p1 and on:
        clearConsole()
        print("\033[33m[Menu de Acceso > *Iniciar Sesion*]\033[0m")
        print()

        user = input("Ingrese nombre de usuario: ").lower().strip()
        if user == "":
            print()
            input("\033[31m[ERROR] El nombre de usuario no puede estar vacio.\033[0m")
        elif user in usuarios:
            isUserReal = True
            p1 = False
            p2 = True
        else:
            print()
            input("\033[31m[ERROR] El usuario ingresado no existe.\033[0m")

    while p2 and on:
        clearConsole()
        print("\033[33m[Menu de Acceso > *Iniciar Sesion*]\033[0m")
        print()
        print(f"Usuario: {user}")
        password = input("Ingrese contrasena: ").strip()

        if usuarios.get(user, {}).get("password") == password:
            isPasswordCorrect = True

            if isUserReal and isPasswordCorrect:
                clearConsole()
                print("\033[33m[Menu de Acceso > *Iniciar Sesion*]\033[0m")
                print()
                print(f"Usuario: {user}")
                print(f"Contrasena: {password}")
                print()
                input(f"Sesion iniciada correctamente. Bienvenid@ {user}!")

                on = False

                credencial = {
                    "user": user,
                    "clearance": usuarios[user]["clearance"]
                }
                return credencial
        elif password == "":
            print()
            input("\033[31m[ERROR] La contrasena no puede estar vacia.\033[0m")
        else:
            print()
            input("\033[31m[ERROR] Contrasena incorrecta.\033[0m")


def signUp(usuarios, listaRoles,isAdmin=False, menuLoop = True):
    clearance = 1
    inProgress = True
    p1, p2, p3, p4, p5 = True, False, False, False, False

    while p1 and inProgress:
        clearConsole()
        print("\033[33m[Menu de Acceso > *Registrarse*]\033[0m")
        print()
        user = input("• Ingrese nombre de usuario: ").lower().strip()

        if user == "":
            print()
            input("\033[31m[ERROR] El nombre de usuario no puede estar vacio.\033[0m")
        elif user in usuarios:
            print()
            input("\033[31m[ERROR] El usuario ingresado ya existe.\033[0m")
        elif user[0].isdigit():
            print()
            input("\033[31m[ERROR] El usuario no puede empezar con un numero.\033[0m")
        else:
            p1 = False
            p2 = True

    while p2 and inProgress:
        clearConsole()
        print("\033[33m[Menu de Acceso > *Registrarse*]\033[0m")
        print()
        print(f"Usuario: {user.capitalize()}")
        password = input("• Ingrese contraseña: ").strip()

        if password == "":
            print()
            input("\033[31m[ERROR] La contraseña no puede estar vacia.\033[0m")
        else:
            cant = len(password)
            hiddenPassword = "*" * cant

            p2 = False
            p3 = True

    while p3 and inProgress:
        clearConsole()
        print("\033[33m[Menu de Acceso > *Registrarse*]\033[0m")
        print()
        print(f"Usuario: {user.capitalize()}")
        print(f"Contraseña: {hiddenPassword}")
        confirmPassword = input("• Confirme contraseña: ").strip()

        if password == "":
            print()
            input("\033[31m[ERROR] La contraseña no puede estar vacia.\033[0m")
        elif confirmPassword != password:
            print()
            input("\033[31m[ERROR] Las contraseñas no coinciden.\033[0m")
        else:
            p3 = False
            p4 = True
    while p4 and inProgress:
        clearConsole()
        print("\033[33m[Menu de Acceso > *Registrarse*]\033[0m")
        print()
        print(f"Usuario: {user}")
        print(f"Contraseña: {hiddenPassword}")
        print()

        roles_disponibles = [[0, "Ninguno"]] + listaRoles
        mostrarListaRoles(roles_disponibles)
        rol = input("Asignele el id del rol al nuevo usuario: ")

        if rol == "":
            print()
            input("\033[31m[ERROR] El rol no puede estar vacio.\033[0m")
        elif rol.isdigit() == False:
            print()
            input("\033[31m[ERROR] El rol debe ser un numero.\033[0m")
        else:
            rol = int(rol)
            rolEncontrado = False

            for rol_item in roles_disponibles:
                if rol_item[0] == rol:
                    rolEncontrado = True
                    rol = rol_item[1]
                    break

            if rolEncontrado:
                p4 = False
                if isAdmin:
                    p5 = True
            else:
                print()
                input("\033[31m[ERROR] El rol ingresado no existe.\033[0m")
    while p5 and inProgress:
        clearConsole()
        print("\033[33m[Menu de Acceso > *Registrarse*]\033[0m")
        print()
        print(f"Usuario: {user}")
        print(f"Rol: {rol}")
        print()
        clearance = input("• Ingrese el nivel de acceso del usuario: ")
        if clearance == "":
            print()
            input("\033[31m[ERROR] El rol no puede estar vacio.\033[0m")
        elif clearance.isdigit() == False:
            print()
            input("\033[31m[ERROR] El rol debe ser un numero.\033[0m")
        else:
            clearance = int(clearance)
            p5 = False

    if inProgress:
        print()
        input("[EXITO] Usuario registrado correctamente.")
        usuarios[user] = {
            "password": password,
            "clearance": clearance,
            "rol": rol,
            "tareas": []
        }

        if menuLoop:
            menuAcceso(usuarios,listaRoles)
        else:
            return {
                "user": user,
                "clearance": usuarios[user]["clearance"]
            }


# def singUp(usuarios, listaRoles):
#     return signUp(usuarios, listaRoles)
