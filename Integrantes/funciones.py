from General.clearConsole import *
from Integrantes.roles import*

def mostrarListaIntegrantes(ListaIntegrantes):
     # Encabezados
        print(f"{'ID':<5}{'Nombre':<20}{'Rol':<15}{'Tareas':<10}")
        print("-" * 50)

        for integrante in ListaIntegrantes:
            id_ = integrante[0]
            nombre = integrante[1]
            rol = integrante[2]
            tareas = len(integrante[3])  # cantidad de tareas asignadas

            print(f"{id_:<5}{nombre:<20}{rol:<15}{tareas:<10}")


def ver_integrantes(ListaIntegrantes):
    clearConsole()
    print("[Menu Principal > Integrantes > *Ver Integrantes*]")
    print()
    if len(ListaIntegrantes) == 0:
        input("No hay integrantes registrados")
    elif len(ListaIntegrantes) > 0:
        mostrarListaIntegrantes(ListaIntegrantes)
        input("\nPresione cualquier tecla para continuar...")
    

#! TODO: COMPLETAR LOS PASOS RESTANTES & AGREGAR SUBMENU y CRUD para creacion y gestion de Roles
def agregar_integrante(ListaIntegrantes, ListaRoles):
    clearConsole()
    print("[Menu Principal > Integrantes > *Agregar Integrantes*]")
    print()
    
    if len(ListaIntegrantes)==0:
        id=1
    else: 
        id = ListaIntegrantes[len(ListaIntegrantes)-1][0]+1 
    
    inProgress=True
    p1,p2= True,False
    
    while p1:
        clearConsole()
        print("[Menu Principal > Integrantes > *Agregar Integrantes*]")
        print()
        nombre_integrante = input("Ingrese el nombre del integrante: ")
        if nombre_integrante== "":
            print("")
            input("[ERROR] El nombre ingresado no puede estar vacio")
        elif nombre_integrante[0].strip().isdigit(): 
            print("")
            input("[ERROR] El nombre ingresado no puede empezar con un número")
        else: 
            p1 = False
            p2 = True

    while p2 and inProgress:
        clearConsole()
        print("[Menu Principal > Integrantes > *Agregar Integrantes*]")
        print()
        print(f"Nombre del Integrante {nombre_integrante}")
        print("")
        if len (ListaRoles)==0:
            input("No hay roles existentes, por favor agregue un rol")
            return
        elif len(ListaRoles)>0:
            mostrarListaRoles(ListaRoles)
            rol = int(input("Asignele el id del rol al nuevo integrante: "))

            for rol_item in ListaRoles:
                if rol_item[0] == rol:
                    nuevo_integrante = [id,nombre_integrante,rol_item[1],[]]
                    ListaIntegrantes.append(nuevo_integrante)
            
            p2 = False

            print("")
            print("Nuevo integrante añadido con éxito ")
            print("ID del integrante:",nuevo_integrante[0])
            print("Nombre:",nuevo_integrante[1])
            print("Rol:",nuevo_integrante[2])
            input("Presione enter para continuar...")



def editar_integrante(ListaIntegrantes, ListaRoles):
    clearConsole()
    print("[Menu Principal > Integrantes > *Editar Integrantes*]")
    print()
    
    if len(ListaIntegrantes) == 0:
        input("No hay integrantes registrados")
    
    else:
        mostrarListaIntegrantes(ListaIntegrantes)
        print()

        member_id = input("Ingrese ID del integrante a editar: ")

        while member_id.isdigit() == False:
            print("[ERROR] Debe ingresar un número")
            member_id = input("Ingrese ID del integrante a editar: ")

        member_id = int(member_id)

        posicion = -1

        for i in range(len(ListaIntegrantes)):
            if ListaIntegrantes[i][0] == member_id:
                posicion = i

        if posicion != -1:
            print("")
            print("1. Cambiar Nombre")
            print("2. Cambiar rol")
            opcion = input("Seleccione una opcion: ")
            
            clearConsole()
            if opcion == "1":
                editarNombre = input("Ingrese el nuevo nombre del integrante: ")
                ListaIntegrantes[posicion][1] = editarNombre

            elif opcion == "2":
                mostrarListaRoles(ListaRoles)
                editarRol = input("Ingrese el ID del nuevo rol: ")

                while editarRol.isdigit() == False:
                    print("[ERROR] Debe ingresar un número")
                    editarRol = input("Ingrese el ID del nuevo rol: ")

                editarRol = int(editarRol)

                rolEncontrado = False

                for rol in ListaRoles:
                    if rol[0] == editarRol:
                        ListaIntegrantes[posicion][2] = rol[1]
                        rolEncontrado = True

                if rolEncontrado == False:
                    print("El rol no existe")

            else:
                print("Número inválido")
        else:
            print("El integrante ingresado no existe")         



def eliminar_integrante(ListaIntegrantes):
    clearConsole()
    print("[Menu Principal > Integrantes > *Eliminar Integrante*]")
    print()

    if len(ListaIntegrantes) == 0:
        input("No hay integrantes registrados")
    else:
        mostrarListaIntegrantes(ListaIntegrantes)
        print()

        idIngresado = input("Ingrese el ID del integrante a eliminar: ")

        while idIngresado.isdigit() == False:
            print("[ERROR] Debe ingresar un número")
            idIngresado = input("Ingrese el ID del integrante a eliminar: ")

        idIngresado = int(idIngresado)

        posicion = -1

        for i in range(len(ListaIntegrantes)):
            if ListaIntegrantes[i][0] == idIngresado:
                posicion = i

        if posicion != -1:
            del ListaIntegrantes[posicion]
            print("Integrante eliminado correctamente")
            print()
            mostrarListaIntegrantes(ListaIntegrantes)

        else:
            print("El integrante con el ID ingresado no existe")








    