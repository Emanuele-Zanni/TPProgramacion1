from General.clearConsole import*
from Integrantes.validaciones import *

def imprimirMenuRoles(ListaRoles, credencial):
    activo=True
    while activo:
        clearConsole()
        print("\033[33m[Menu Principal > Personal > *Roles*]\033[0m")
        print()  
        if credencial["clearance"] < 2:
            print("1. Ver roles")
            print("0. Volver")
            opcion_rol=input("• Ingrese la opción deseada: ")
            
            if opcion_rol== "1":
                ver_roles(ListaRoles)

            elif opcion_rol== "0": 
                activo=False
            elif opcion_rol=="":
                print()
                input("Opcion inválida")
            else:
                print()
                input("Número inválido")

        elif credencial["clearance"] < 3:
            pass

         #!Clearance Admin
        else:
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

            
def crear_roles(ListaRoles):
    if len(ListaRoles) == 0:
        id = 1
    else:    
        id = ListaRoles[len(ListaRoles)-1][0]+1

    p1 = True
    while p1:
        clearConsole()
        print("[Menu Principal > Personal > Roles > *Crear Rol*]")
        print()
        nuevo_rol=input("• Ingrese el nombre del nuevo rol: ").strip()
        if nuevo_rol == "":
            print()
            input("[ERROR] El nombre del rol no puede estar vacio")
        elif nuevo_rol.lower() in [rol[1].lower() for rol in ListaRoles]:
            print()
            input("[ERROR] El rol ingresado ya existe")
        else:
            p1 = False


    nuevo_rol = [id, nuevo_rol]
    ListaRoles.append(nuevo_rol)
    print(ListaRoles)
    input("Presione enter para continuar...")

def editar_rol(ListaRoles):
    clearConsole()
    if len(ListaRoles)==0:
        input("No hay roles registrados ")

    else:
        clearConsole()
        print("[Menu Principal > Personal > Rol > *Editar Rol*]")
        print()
        mostrarListaRoles(ListaRoles)
        try:
            rol_id=int(input("• Ingrese el ID del rol a editar: "))
            for i in range(len(ListaRoles)):
                if ListaRoles[i][0]==rol_id:
                    clearConsole()
                    print("[Menu Principal > Personal > Rol > *Editar Rol*]")
                    print()
                    # ver_roles([ListaRoles[i]],False)
                    mostrarListaRoles([ListaRoles[i]])
                    print()
                    nuevo_rol = input("• Ingrese el nuevo nombre del rol: ")
                    nuevo_rol,isValid = validacionRoles(ListaRoles,nuevo_rol) #? Nueva forma de validar

                    if isValid:
                        ListaRoles[i][1]= nuevo_rol
                        clearConsole()
                        print("[Menu Principal > Personal > *Crear Rol*]")
                        print()
                        ver_roles([ListaRoles[i]],False)
                        input("[Exito] Rol actualizado exitosamente")
        except ValueError:
            print()
            input("[ERROR] El ID ingresado no existe")
        
def eliminar_rol(ListaRoles):
    clearConsole()
    if len(ListaRoles)==0:
        input("No hay roles registrados ")
    else:
        mostrarListaRoles(ListaRoles)
        rol_id = None
        try:
            rol_id=int(input("Elija el ID del Rol que desea eliminar: "))
            rol_id,isValid = validacionRolesInt(ListaRoles,rol_id)
        except ValueError:
            #! discutir con el profesor la posibilidad de NO USAR TRY/EXCEPT y utilizar al estrategia mas optima correspondiente para este caso
            isValid = False
            print()
            input("[ERROR] El ID debe ser un numero")

        if isValid:
            for i in range(len(ListaRoles)):
                if ListaRoles[i][0]==rol_id:
                    ListaRoles.pop(i)

                    print()
                    input("[EXITO] Rol eliminado exitosamente")
                    break


def mostrarListaRoles(ListaRoles):
    print(f"{'ID':<5}{'Nombre del rol':<30}")
    print("-" * 20)
    
    for rol in ListaRoles:
        id = rol[0]
        nombre = rol[1]     
        print(f"{id:<5}{nombre:<30}")
    
    print()



def ver_roles(ListaRoles,mode=True):
    clearConsole()
    print("\033[33m[Menu Principal > Personal > Roles > *Ver Roles*]\033[0m")
    print()

    if len(ListaRoles) == 0:
        input("No hay roles asignados ")
        return
    elif len(ListaRoles) > 0:
        mostrarListaRoles(ListaRoles)

        #* mode se usa para determinar si la funcion ver_roles debe detener la ejecucion del codigo con un input o no
        #* True (default) = Lo detiene || {cualquierOtroValor} = No lo detiene
        if mode:
            input("\nPresione cualquier tecla para continuar...")
