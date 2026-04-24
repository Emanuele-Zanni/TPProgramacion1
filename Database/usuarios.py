from General.clearConsole import*

subHeaders = ["password","clearance"]
listaNombres = ["Candela","Emanuele"]
listaContraseñas = ["1234","5555"]
listaNivelesAcceso = [3,3] #? 0 Invitado?, 1 Miembro, 2 Manager, 3 SuperAdmin

#* Menuda diccionario por comprension chaval
#* Explicacion de esta lista... (agregar)
usuarios = {
    nombre: dict(zip(subHeaders, [contraseña, acceso]))
    for nombre, contraseña, acceso in zip(listaNombres, listaContraseñas, listaNivelesAcceso)
}


def login():
    on=True
    p1,p2 = True,False

    while on:
        isPasswordCorrect = False
        isUserReal = False
        # user = ""
        # password = ""
        clearConsole()
        print("[Menu de Login]")
        print()

        user=input("• Ingrese nombre de usuario: ")

        if user in usuarios:
            isUserReal = True
        # if usuarios.get(user) is not None:
        #     isUserReal = True
        #     print(isUserReal)

        clearConsole()
        print("[Menu de Login]")
        print()
        print(f"Usuario: {user}")
        password=input("• Ingrese contraseña: ")

        if usuarios.get(user, {}).get("password") == password:
            isPasswordCorrect = True

        if isUserReal and isPasswordCorrect:
            clearConsole()
            print("[Menu de Login]")
            print()
            print(f"Usuario: {user}")
            print(f"Contraseña: {password}")
            print()
            input(f"Sesion iniciada correctamente. ¡Bienvenid@ {user}!")

            inicio=True
            return True   
        elif isUserReal and isPasswordCorrect == False:  
                print()
                input("[ERROR] Contraseña incorrecta ") 
        else:
                print()
                input("[ERROR] El usuario ingresado no existe")