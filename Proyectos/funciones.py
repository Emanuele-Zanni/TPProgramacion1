from General.clearConsole import *
from Tareas.menus import *
# from Proyectos.menus import imprimirMenuSeleccionarProyecto

def ver_proyectos(ListaProyectos):
    clearConsole()
    print("[Menu Principal > Proyectos > *Ver Proyectos*]")
    print()       
    if len(ListaProyectos) == 0:
        input("No hay proyectos registrados.")
    elif len(ListaProyectos) > 0:
        for proyecto in ListaProyectos:
            print(proyecto)
        print("")
        input("Ingrese cualquier opcion para continuar...")


def seleccionar_proyecto(ListaProyectos):
    clearConsole()
    print("[Menu principal > Proyectos > *Seleccionar Proyectos*]")
    print()

    isProjectReal = False
    proyectoSeleccionado = ""
    if len(ListaProyectos) == 0:
        input("No hay proyectos registrados.")
    else:
        id = int(input("ingrese el ID del proyecto a seleccionar: "))
        for proyecto in ListaProyectos:
            if proyecto[0] == id:   
                isProjectReal = True

        if isProjectReal:
            clearConsole()
            print("[Menu principal > Proyectos > *Proyecto Seleccionado*]")
            print() 
            print(f"=== {proyecto[1]} ===")
            print(f"ID: {proyecto[0]} | Status: {proyecto[5]} | Fecha Inicio/Final: {proyecto[3]} - {proyecto[4]}")
            print("")
            for tarea in proyecto[2]:
                print(tarea)
            print("---")

            imprimirMenuTareas(proyecto[2])
        else:
            print("")
            input("[ERROR] El ID ingresado no pertenece a ningun proyecto")

        

def crear_proyecto(ListaProyectos):
    clearConsole()
    print("[Menu Principal > Proyectos > *Crear Proyectos*]")
    print()
    #* Variables para inicializar las flags para persistencia de inputs + validaciones
    inProgress = True
    p1,p2,p3 = True,False,False
    id = len(ListaProyectos) + 1
    tareas = []
    Estado = "Activo?" #* Hacer enum!

    while p1 and inProgress:
        clearConsole()
        print("[Menu Principal > Proyectos > *Crear Proyectos*]")
        print()
        nombreProyecto=input("Ingrese el nombre del proyecto: ")  
        if nombreProyecto == "":
            print("")
            input("[ERROR] El nombre ingresado no puede estar vacio") 
        else:
            p1 = False
            p2 = True

    while p2 and inProgress:
        clearConsole()
        print("[Menu Principal > Proyectos > *Crear Proyectos*]")
        print()
        print(f"Nombre del Proyecto: {nombreProyecto}")
        FechaInicio=input("Ingrese la fecha de inicio del proyecto: ")
        if FechaInicio == "":
            print("")
            input("[ERROR] La fecha ingresada no puede estar vacia") 
        elif FechaInicio.isdigit() == False:
            print("")
            input("[ERROR] La fecha ingresada debe ser un numero") 
        else:
            p2 = False
            p3 = True
    
    while p3 and inProgress:
        clearConsole()
        print("[Menu Principal > Proyectos > *Crear Proyectos*]")
        print()
        print(f"Nombre del Proyecto: {nombreProyecto}")
        print(f"Fecha de Inicio: {FechaInicio}")
        FechaFinal=input("Ingrese la fecha de finalizacion del proyecto: ")
        if FechaFinal == "":
            print("")
            input("[ERROR] La fecha ingresada no puede estar vacia") 
        elif FechaInicio.isdigit() == False:
            print("")
            input("[ERROR] La fecha ingresada debe ser un numero") 
        else:
            p3 = False

    if inProgress:

        #? Type Proyecto = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]
        nuevo_proyecto = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]
        
        ListaProyectos.append(nuevo_proyecto)
        print("")
        input("[EXITO] Proyecto creado exitosamente.")

#no basico
def editar_proyecto(ListaProyectos):
    clearConsole()
    print("[Menu principal > Proyectos > *Editar Proyectos*]")
    print()

    if len(ListaProyectos) == 0:
        input("No hay proyectos registrados.")
    else:
        #* Que proyecto? [POSICION]
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
            print("")
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
                print("")
                input("[ERROR] Número inválido")

            # proyecto_editado = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]

        else:
            print("")
            input("[ERROR] El proyecto ingresado no existe")

#no basico
def eliminar_proyecto(ListaProyectos):
    clearConsole()
    print("[Menu principal > Proyectos > *Eliminar Proyectos*]")
    print()

    if len(ListaProyectos) == 0:
        input("No hay proyectos registrados.")
    else:
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
            input("[ERROR] El proyecto con el ID ingresado no existe")      
