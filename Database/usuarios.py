from General.clearConsole import *
from Integrantes.roles import *


def obtenerProximoIdUsuario(usuarios):
    max_id = 0

    for datos_usuario in usuarios.values():
        usuario_id = datos_usuario.get("id")
        if isinstance(usuario_id, int) and usuario_id > max_id:
            max_id = usuario_id

    if max_id == 0:
        return 1

    return max_id + 1


def menuAcceso(usuarios, listaRoles):
    while True:
        clearConsole()
        print("""\033[33m[*Menu de Acceso*]\033[0m

1. Iniciar Sesion
2. Registrarse
 """)
        choice = input("â€¢ Ingrese una opcion: ")
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

        user = input("â€¢ Ingrese nombre de usuario: ").lower().strip()
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
        print()
        password = input("â€¢ Ingrese contraseÃ±a: ").strip()

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


def signUp(usuarios, listaRoles, isAdmin=False, menuLoop=True):
    clearance = 1
    inProgress = True
    p1, p2, p3, p4 = True, False, False, False

    while p1 and inProgress:
        clearConsole()
        print("\033[33m[Menu de Acceso > *Registrarse*]\033[0m")
        print()
        user = input("â€¢ Ingrese nombre de usuario: ").lower().strip()

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
        print()
        password = input("â€¢ Ingrese contraseÃ±a: ").strip()

        if password == "":
            print()
            input("\033[31m[ERROR] La contraseÃ±a no puede estar vacia.\033[0m")
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
        print(f"ContraseÃ±a: {hiddenPassword}")
        confirmPassword = input("â€¢ Confirme contraseÃ±a: ").strip()

        if password == "":
            print()
            input("\033[31m[ERROR] La contraseÃ±a no puede estar vacia.\033[0m")
        elif confirmPassword != password:
            print()
            input("\033[31m[ERROR] Las contraseÃ±as no coinciden.\033[0m")
        else:
            p3 = False
            p4 = True

    while p4 and inProgress:
        clearConsole()
        print("\033[33m[Menu de Acceso > *Registrarse*]\033[0m")
        print()
        print(f"Usuario: {user}")
        print(f"ContraseÃ±a: {hiddenPassword}")
        print()

        if isAdmin:
            clearance = input("â€¢ Ingrese el nivel de acceso del usuario: ")
            if clearance == "":
                print()
                input("\033[31m[ERROR] El nivel de acceso no puede estar vacio.\033[0m")
            elif clearance.isdigit() == False:
                print()
                input("\033[31m[ERROR] El nivel de acceso debe ser un numero.\033[0m")
            else:
                clearance = int(clearance)
                p4 = False
        else:
            p4 = False

    if inProgress:
        print()
        input("\033[92m[EXITO] Usuario registrado correctamente.\033[0m")
        nuevo_id = obtenerProximoIdUsuario(usuarios)
        usuarios[user] = {
            "id": nuevo_id,
            "password": password,
            "clearance": clearance,
            "projects": []
        }

        if menuLoop:
            resultado = menuAcceso(usuarios, listaRoles)
            print(f"signUp devuelve: {resultado}")
            return resultado
        else:
            resultado = {
                "user": user,
                "clearance": usuarios[user]["clearance"]
            }
            print(f"signUp devuelve: {resultado}")
            return resultado


# def singUp(usuarios, listaRoles):
#     return signUp(usuarios, listaRoles)
