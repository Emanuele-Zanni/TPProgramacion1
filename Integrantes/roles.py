from General.clearConsole import*


def imprimirMenuRoles(ListaRoles, basico):
    activo=True
    while activo:
        clearConsole()
        print("[Menu Principal > Ver personal > *Roles*]")
        print()  
        if basico==True:
            print("1. Ver roles")
            print("2. Crear rol ")
            print("3. Editar rol ")  
            print("4. Eliminar rol")  
            print("0. Volver")
            opcion_rol=input("Ingrese la opción deseada: ")

            if opcion_rol== "1":
                ver_roles(ListaRoles)
            
            elif opcion_rol == "2":
                crear_roles(ListaRoles)
                
            elif opcion_rol== "3":
                editar_rol(ListaRoles)
            
            elif opcion_rol== "4":
                eliminar_rol(ListaRoles)
            

            elif opcion_rol== "0": 
                activo=False
            
            elif opcion_rol=="":
                print()
                input("Opcion inválida")
            else:
                print()
                input("Número inválido")

        else:
            print("4. Ver roles")
            print("0. Volver")
            opcion_rol=input("Ingrese la opción deseada: ")
            
            if opcion_rol== "4":
                ver_roles(ListaRoles)

            elif opcion_rol== "0": 
                activo=False
            elif opcion_rol=="":
                print()
                input("Opcion inválida")
            else:
                print()
                input("Número inválido")

            
     

def crear_roles(ListaRoles):
    clearConsole()
    if len(ListaRoles) == 0:
        id = 1
    else:    
        id = ListaRoles[len(ListaRoles)-1][0]+1
    nuevo_rol=input("Ingrese el nombre del nuevo rol: ")
    nuevo_rol = [ id, nuevo_rol, []]
    ListaRoles.append(nuevo_rol)
    print(ListaRoles)
    input("Presione enter para continuar...")

def editar_rol(ListaRoles):
    clearConsole()
    if len(ListaRoles)==0:
        input("No hay roles registrados ")

    else:        
        print(ListaRoles)
        rol_id=int(input("Ingrese el ID del rol a editar: "))
        for i in range(len(ListaRoles)):
            if ListaRoles[i][0]==rol_id:
                nuevo_rol=input("Ingrese el nuevo nombre del rol: ")
                ListaRoles[i][1]= nuevo_rol
                input(ListaRoles)

def eliminar_rol(ListaRoles):
    clearConsole()
    if len(ListaRoles)==0:
        input("No hay roles registrados ")
    else:
        print(ListaRoles)
        rol_id=int(input("Elija el ID del Rol que desea eliminar: "))
        for i in range(len(ListaRoles)):
            if ListaRoles[i][0]==rol_id:
                ListaRoles.pop(i)
                input(ListaRoles)


def mostrarListaRoles(ListaRoles):
    print(f"{'ID':<5}{'Nombre del rol':<30}")
    print("-" * 20)
    
    for rol in ListaRoles:
        id_ = rol[0]
        nombre = rol[1]     
        print(f"{id_:<5}{nombre:<30}")
    
    print()



def ver_roles(ListaRoles):
    clearConsole()
    print("[Menu Principal > Integrantes > *Ver Roles*]")
    print()

    if len(ListaRoles) == 0:
        input("No hay roles asignados ")
        return
    elif len(ListaRoles) > 0:
        mostrarListaRoles(ListaRoles)
        input("\nPresione cualquier tecla para continuar...")
  


"""
def crear_roles(ListaRoles):
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
"""