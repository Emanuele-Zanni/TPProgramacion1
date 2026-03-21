from General.clearConsole import *


def ver_integrantes(ListaIntegrantes):
    clearConsole()
    print("[Menu Principal > Integrantes > *Ver Integrantes*]")
    print()
    if len(ListaIntegrantes) == 0:
        print("No hay integrantes registrados")
        return
    elif len(ListaIntegrantes) > 0:
        for integrante in ListaIntegrantes:
            print(integrante)

def agregar_integrante(ListaIntegrantes):
    clearConsole()
    print("[Menu Principal > Integrantes > *Agregar Integrantes*]")
    print()
    
    if len(ListaIntegrantes)==0:
        id=1
    else: 
        id = ListaIntegrantes[len(ListaIntegrantes)-1][0]+1 
    
    nombre_integrante = input("Ingrese el nombre del integrante: ")
    rol = input("Ingrese el rol: ")
    #! Tareas asignadas???

    nuevo_integrante = [id,nombre_integrante,rol]

    ListaIntegrantes.append(nuevo_integrante)

def editar_integrante(ListaIntegrantes):
    clearConsole()
    
    if len(ListaIntegrantes)==0:
        print("No hay integrantes")
    
    else:
        print("[Menu Principal > Integrantes > *Editar Integrantes*]")
        print()
        posicion = 0
        isMemberReal = False
        member_id = int(input("Ingrese ID de la tarea a editar: "))
        for item in ListaIntegrantes:
                if item[0] == member_id:
                    posicion = member_id - 1
                    isMemberReal = True
        if isMemberReal:
            print("1. Cambiar Nombre")
            print("2. Cambiar rol")
            opcion = input("Seleccione una opcion")
            
            if opcion == "1":
                editarNombre=input("Ingrese el nuevo nombre del proyecto: ")
                ListaIntegrantes[posicion][1] = editarNombre
            elif opcion == "2":
                editarRol=input("Ingrese la nueva fecha de inicio: ")
                ListaIntegrantes[posicion][2] = editarRol
            else:
                print("Número inválido")

            # tarea_editada = [id,nombreTarea,tareas,FechaInicio,FechaFinal,Estado]

        else:
            print("El integrante ingresado no existe")


def eliminar_integrante(ListaIntegrantes):
    clearConsole()
    print("[Menu Principal > Integrantes > *Eliminar Integrante*]")
    print()
    id = int(input("Ingrese el ID del integrante a eliminar: "))
    isMemberReal = False

    for item in ListaIntegrantes:
        if item[0] == id:
            isMemberReal = True

    if isMemberReal:
        del ListaIntegrantes[id-1]


    else:
        print("El integrante con el ID ingresado no existe")    

    