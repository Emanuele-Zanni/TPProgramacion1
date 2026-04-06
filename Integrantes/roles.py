from General.clearConsole import*

def imprimirMenuRoles(ListaRoles):
    clearConsole()
    print("[Menu Principal > Ver personal > *Roles*]")
    print()  
    print("1. Crear rol: ")
    print("2. Editar rol: ")  
    print("3. Eliminar rol: ")   
    opcion_rol=int(input("Ingrese la opción deseada: "))

def crear_rol(ListaRoles):
    clearConsole()
    print("[Menu Principal > Integrantes > *Crear Rol*]")
    print()
    id = len(ListaRoles) + 1
    rol=input("Ingrese el nombre del rol: ")

    #* Enum

    nuevo_rol = [id, rol]
    
    ListaRoles.append(nuevo_rol)

def editar_rol(ListaRoles):
    clearConsole()
    print("[Menu principal > Integrantes > *Editar Rol*]")
    print()
    #isRolReal = False
    #rol=int(input("Ingrese el rol a editar: "))

def eliminar_rol(ListaRoles): 
    clearConsole()
    print("[Menu principal > Integrantes > *Eliminar Rol*]")
    print()
    if len(ListaRoles) == 0:
        print("No hay roles asignados.")
        return
    elif len(ListaRoles) > 0:
        for rol in ListaRoles:
            print()
            id = int(input("Ingrese el ID del rol a eliminar: "))