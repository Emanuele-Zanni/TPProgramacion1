from General.clearConsole import *

def ver_proyectos(ListaProyectos):
    clearConsole()
    print("[Menu Principal > Proyectos > *Ver Proyectos*]")
    print()       
    if len(ListaProyectos) == 0:
        print("No hay proyectos registrados.")
        return
    elif len(ListaProyectos) > 0:
        for proyecto in ListaProyectos:
            print(proyecto)

def seleccionar_proyecto(ListaProyectos):
    clearConsole()
    print("[Menu principal > Proyectos > *Seleccionar Proyectos*]")
    print()
    
    id = int(input("ingrese el ID del proyecto a seleccionar: "))
    posicion = id - 1
    for posicion in range(len(ListaProyectos)):
        if len(ListaProyectos) == 0:
            print("no hay proyectos registrados")
            
        elif id - 1 != ListaProyectos[posicion]:
            if posicion == len(ListaProyectos) - 1:    
                print("el proyecto ingresado no existe")
            
        elif id - 1 == ListaProyectos[posicion]:
            print("proyecto seleccionado: ", ListaProyectos[posicion])
            return ListaProyectos[posicion]

def crear_proyecto(ListaProyectos):
    clearConsole()
    print("[Menu Principal > Proyectos > *Crear Proyectos*]")
    print()
    id = len(ListaProyectos) + 1
    nombreProyecto=input("Ingrese el nombre del proyecto: ")
    tareas = []
    FechaInicio=input("Ingrese la fecha de inicio del proyecto: ")
    FechaFinal=input("Ingrese la fecha de finalizacion del proyecto: ")
    Estado=input("Ingrese el estado del proyecto: ")
    #* Enum

    nuevo_proyecto = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]
    
    ListaProyectos.append(nuevo_proyecto)
    
    #* ListaProyectos = [[id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]]

    # return nuevo_proyecto


def editar_proyecto(ListaProyectos):
    clearConsole()
    print("[Menu principal > Proyectos > *Editar Proyectos*]")
    print()
    #* Que proyecto? [POSICION]
    posicion = 0
    isProjectReal = False
    project_id = int(input("Ingrese ID del proyecto a editar: "))
    for item in ListaProyectos:
            if item[0] == project_id:
                posicion = project_id - 1
                isProjectReal = True

    if isProjectReal:
        #* Menu con variables de ESE proyecto (1. Cambiar Nombre - 2. Cambiar fecha de inicio - 3. Cambiar fecha final - 4. Nuevo estado del proyecto)
        print("1. Cambiar Nombre")
        print("2. Cambiar fecha de inicio")
        print("3. Cambiar fecha final")
        print("4. Cambiar el estado del proyecto")
        opcion = input("Seleccione una opcion")
        
        if opcion == "1":
            editarNombre=input("Ingrese el nuevo nombre del proyecto: ")
            ListaProyectos[posicion][1] = editarNombre
        elif opcion == "2":
            editarFechaInicio=input("Ingrese la nueva fecha de inicio: ")
            ListaProyectos[posicion][3] = editarFechaInicio
        elif opcion == "3":
            editarFechaFinal=input("Ingrese la nueva fecha final: ")
            ListaProyectos[posicion][4] = editarFechaFinal
        elif opcion == "4": 
            editarEstado=input("Ingrese el nuevo estado del proyecto: ")
            ListaProyectos[posicion][5] = editarEstado
        else:
            print("Número inválido")

        # proyecto_editado = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]

    else:
        print("El proyecto ingresado no existe")


def eliminar_proyecto(ListaProyectos):
    clearConsole()
    print("[Menu principal > Proyectos > *Eliminar Proyectos*]")
    print()
    #* Aca falta agregar validacion de input NO numerico para que no rompa (y conversor de texto a num)
    id = int(input("Ingrese el ID del proyecto a eliminar: "))
    isProjectReal = False

    for item in ListaProyectos:
        if item[0] == id:
            isProjectReal = True

    if isProjectReal:
        del ListaProyectos[id-1]
        #* Aca falta funcion para reacomodar el ID de TODOS los elementos de la lista para que no haya saltos
        #* (Es opcional esto) 
    else:
        print("El proyecto con el ID ingresado no existe")      
