from General.clearConsole import*

subHeaders = ["password","clearance"]
listaNombres = ["candela","emanuele","eze"]
listaContraseñas = ["1234","5555","123"]
listaNivelesAcceso = [3,3,3] #? 0 Invitado?, 1 Miembro, 2 Manager, 3 SuperAdmin

#* Menuda diccionario por comprension chaval
#* Explicacion de esta lista... (agregar)
usuarios = {
    nombre: dict(zip(subHeaders, [contraseña, acceso]))
    for nombre, contraseña, acceso in zip(listaNombres, listaContraseñas, listaNivelesAcceso)
}


def login():
    on=True
    p1,p2 = True,False
    isPasswordCorrect = False
    isUserReal = False

    while p1 and on:
       
        # user = ""
        # password = ""
        clearConsole()
        print("[Menu de Login]")
        print()

        user=input("• Ingrese nombre de usuario: ").lower()

        if user in usuarios:
            isUserReal = True
            p1=False
            p2=True
        # if usuarios.get(user) is not None:
        #     isUserReal = True
        #     print(isUserReal)
        else:
            print()
            input("[ERROR] El usuario ingresado no existe")

    while p2 and on:
        
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

            on = False
               
        elif isUserReal and isPasswordCorrect == False:  
                print()
                input("[ERROR] Contraseña incorrecta ") 
        