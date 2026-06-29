"""Acceso y registro de usuarios de la aplicacion."""

from General.clearConsole import clearConsole
from General.logica import autenticar, crear_integrante_logica
from General.validaciones import validar_password, validar_usuario


def obtenerProximoIdUsuario(usuarios):
    return max(
        (datos.get("id", 0) for datos in usuarios.values()), default=0
    ) + 1


def menuAcceso(usuarios, listaRoles):
    while True:
        clearConsole()
        print("\033[33m[Menu de acceso]\033[0m\n")
        print("1. Iniciar sesion")
        print("2. Registrarse")
        opcion = input("• Ingrese una opcion: ").strip()
        if opcion == "1":
            return login(usuarios)
        if opcion == "2":
            return signUp(usuarios, listaRoles)
        input("\033[31m[ERROR] Opcion invalida. Presione Enter.\033[0m")


def login(usuarios):
    while True:
        clearConsole()
        print("\033[33m[Menu de acceso > Iniciar sesion]\033[0m\n")
        usuario = input("• Usuario: ").strip().lower()
        if usuario == "":
            input("\033[31m[ERROR] El usuario no puede estar vacio.\033[0m")
            continue
        if usuario not in usuarios:
            input("\033[31m[ERROR] El usuario no existe.\033[0m")
            continue

        password = input("• Contrasena: ").strip()
        if password == "":
            input("\033[31m[ERROR] La contrasena no puede estar vacia.\033[0m")
            continue
        if not autenticar(usuarios, usuario, password):
            input("\033[31m[ERROR] Contrasena incorrecta.\033[0m")
            continue

        print(f"\nSesion iniciada correctamente. Bienvenido/a {usuario}.")
        input("Presione Enter para continuar.")
        return {
            "user": usuario,
            "clearance": usuarios[usuario]["clearance"],
        }


def signUp(usuarios, listaRoles, isAdmin=False, menuLoop=True):
    clearConsole()
    print("\033[33m[Menu de acceso > Registro]\033[0m\n")
    try:
        usuario = validar_usuario(input("• Nuevo usuario: "))
        if usuario in usuarios:
            raise ValueError("El usuario ya existe.")
        password = validar_password(input("• Contrasena: "))
        confirmacion = input("• Repita la contrasena: ").strip()
        if confirmacion != password:
            raise ValueError("Las contrasenas no coinciden.")

        clearance = 1
        if isAdmin:
            texto_clearance = input("• Nivel de acceso (0 a 3): ").strip()
            if not texto_clearance.isdigit() or int(texto_clearance) not in range(4):
                raise ValueError("El nivel de acceso debe estar entre 0 y 3.")
            clearance = int(texto_clearance)

        crear_integrante_logica(usuarios, usuario, password, clearance)
    except (TypeError, ValueError) as error:
        input(f"\033[31m[ERROR] {error}\033[0m")
        return None

    input("[EXITO] Usuario registrado correctamente.")
    return {
        "user": usuario,
        "clearance": usuarios[usuario]["clearance"],
    }
