def validacionRoles(ListaRoles,valor):
    try:
        if valor == "":
            print()
            input("[ERROR] El nombre del rol no puede estar vacio")
            return valor,False
        elif valor.lower() in [rol[1].lower() for rol in ListaRoles]:
            print()
            input("[ERROR] El rol ingresado ya existe")
            return valor,False
        else:
            return valor,True
    except ValueError:
        if valor == None:
            print()
            input("[ERROR] El ID ingresado no puede estar vacio")
            return valor,False
        elif valor.isdigit() == False:
            print()
            input("[ERROR] El ID ingresado no es un numero")
            return valor,False
        else:
            print()
            input("[ERROR] El ID ingresado no existe")
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
            input("[ERROR] El ID ingresado no existe")
            return valor,False
        else:
            print()
            input("exito")
            return valor,True
    except ValueError:
        pass
