from General.clearConsole import*


def login():
    inicio=False
    superUsuarios = {"Candela": "1234", "Sofia": "2345"}
    basicoUsuarios = {"Federico":"1234"}

    while inicio==False:
        usuario=input("Ingrese el nombre de usuario: ")
        contraseña=input("Ingrese la contraseña: ")

        if usuario in superUsuarios:

            if superUsuarios[usuario] == contraseña:
                input("¡Bienvenido! ")
                inicio=True
                return False        # Devuelve False para indicar que no es un usuario básico
                clearConsole()
            
            else:
                input("Contraseña incorrecta ")
                clearConsole()

        elif usuario in basicoUsuarios:

            if basicoUsuarios[usuario] == contraseña:
                input("¡Bienvenido! ")
                inicio=True
                return True
                
            else:
                input("Contraseña incorrecta ")
                clearConsole()
                
        else:
            input("El usuario ingresado no existe ")
            clearConsole()