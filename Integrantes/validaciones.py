def validacionRoles(ListaRoles,valor):
    try:
        if valor == "":
            print()
            input("\033[31m[ERROR] El nombre del rol no puede estar vacio.\033[0m")
            return valor,False
        elif valor.lower() in [rol[1].lower() for rol in ListaRoles]:
            print()
            input("\033[31m[ERROR] El rol ingresado ya existe.\033[0m")
            return valor,False
        else:
            return valor,True
    except ValueError:
        if valor == None:
            print()
            input("\033[31m[ERROR] El ID ingresado no puede estar vacio.\033[0m")
            return valor,False
        elif valor.isdigit() == False:
            print()
            input("\033[31m[ERROR] El ID ingresado no es un numero.\033[0m")
            return valor,False
        else:
            print()
            input("\033[31m[ERROR] El ID ingresado no existe.\033[0m")
            return valor,False
        
def validacionRolesInt(ListaRoles,valor):
    try:
        # if valor == None:
        #     print()
        #     input("[ERROR] El ID ingresado no puede estar vacio")
        #     return valor,False
        if valor in ListaRoles[0]:
            return valor,True
        if valor not in ListaRoles[0]:
            print()
            input("\033[31m[ERROR] El ID ingresado no existe.\033[0m")
            return valor,False
        else:
            print()
            input("exito")
            return valor,True
    except ValueError:
        pass
