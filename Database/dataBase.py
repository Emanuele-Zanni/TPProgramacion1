from General.clearConsole import*
def login():
    inicio=False
    while inicio==False:
        usuarios = {"Candela": "1234"}

        usuario=input("Ingrese el nombre de usuario: ")
        contraseña=input("Ingrese la contraseña: ")

        if usuario in usuarios:

            if usuarios[usuario] == contraseña:
                input("¡Bienvenido! ")
                inicio=True
            else:
                input("Contraseña incorrecta ")
                clearConsole()
                
        else:
            input("El usuario ingresado no existe ")
            clearConsole()