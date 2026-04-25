from General.clearConsole import *

def ver_tareas(ListaTareas):
    clearConsole()
    print("[Menu Tareas > Ver Tareas]")
    print()
    if len(ListaTareas) == 0:
        print()
        input("No hay tareas registradas.")
    else:
        for tarea in ListaTareas:
            print(tarea)
        print()
        input("Ingrese cualquier opcion para continuar" )

def crear_tarea(ListaTareas):
    clearConsole()
    print("[Menu Tareas > Crear Tareas]")
    print()
    if len(ListaTareas) == 0:
        id = 1
    else:    
        id = ListaTareas[len(ListaTareas)-1][0]+1
    p1,p2,p3= True,False,False

    inProgress = True

    while p1 and inProgress:
        clearConsole()
        print("[Menu Principal > Proyectos > Seleccionar Proyectos > *Crear Tarea*]")
        print()
        nombreTarea=input("Ingrese el nombre de la tarea: ")
        if nombreTarea == "":
            print("")
            input("[ERROR] El nombre de la tarea no puede estar vacio")
        else:
            p1 = False
            p2 = True

    while p2 and inProgress:
        clearConsole()
        print("[Menu Principal > Proyectos > Seleccionar Proyectos > *Crear Tarea*]")
        print()
        print(f"Nombre de la tarea: {nombreTarea}")
        print()
        FechaInicio=input("Ingrese la fecha de inicio de la tarea: ")
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
        print("[Menu Principal > Proyectos > Seleccionar Proyectos > *Crear Tarea*]")
        print()
        print(f"Nombre de la tarea: {nombreTarea}")
        print(f"Fecha de Inicio: {FechaInicio}")
        print()
        FechaFinal=input("Ingrese la fecha de finalizacion de la tarea: ")
        if FechaFinal == "":
            print("")
            input("[ERROR] La fecha ingresada no puede estar vacia")
        elif FechaFinal.isdigit() == False:
            print("")
            input("[ERROR] La fecha ingresada debe ser un numero")
        else:
            p3 = False
            
    if inProgress:

        #? Type Proyecto = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]
        nueva_tarea = [id,nombreTarea,FechaInicio,FechaFinal]
        
        ListaTareas.append(nueva_tarea)
        print("")
        input("[EXITO] Tarea creada exitosamente.")
    else:
        input("Operacion cancelada.")


def editar_tarea(ListaTareas):
    if len(ListaTareas) == 0:
        clearConsole()
        print("[Menu Tareas > *Editar Tareas*]")
        print()
        input("No hay tareas registradas.")
    else:
        clearConsole()
        print("[Menu Tareas > Editar *Tareas*]")
        print()
        #* Que_tarea? [POSICION]
        posicion = 0
        isTaskReal = False
        task_id = input("Ingrese ID de la tarea a editar: ")
        if task_id == "":
            print()
            input("[ERROR] El id no puede estar vacio")
        elif task_id.isdigit() == False:
            print()
            input("[ERROR] El id debe ser un numero")
        elif task_id.isdigit() == True and task_id != "":
            task_id = int(task_id)
            for item in ListaTareas:
                    if item[0] == task_id:
                        posicion = task_id - 1
                        isTaskReal = True

            if isTaskReal:
                
                #* Menu con variables de ESA tarea (1. Cambiar Nombre - 2. Cambiar fecha de inicio - 3. Cambiar fecha final - 4. Nuevo estado de la tarea)
                print("1. Cambiar Nombre")
                print("2. Cambiar fecha de inicio")
                print("3. Cambiar fecha final")
                print("4. Cambiar el estado de la tarea")
                print("")
                opcion = input("Seleccione una opcion")
                
                if opcion == "1":
                    editarNombre=input("Ingrese el nuevo nombre del proyecto: ")
                    ListaTareas[posicion][1] = editarNombre
                elif opcion == "2":
                    editarFechaInicio=input("Ingrese la nueva fecha de inicio: ")
                    ListaTareas[posicion][3] = editarFechaInicio
                elif opcion == "3":
                    editarFechaFinal=input("Ingrese la nueva fecha final: ")
                    ListaTareas[posicion][4] = editarFechaFinal
                elif opcion == "4": 
                    editarEstado=input("Ingrese el nuevo estado de la tarea: ")
                    ListaTareas[posicion][5] = editarEstado
                else:
                    input("[ERROR] Número inválido")

                #tarea_editada = [id,editarNombre,editarFechaInicio,editarFechaFinal,editarEstado]
                #ListaTareas.append(tarea_editada)
            else:
                input("[ERROR] La tarea ingresada no existe")


def eliminar_tarea(ListaTareas):
    if len(ListaTareas) == 0:
        clearConsole()
        print("[Menu Tareas > *Eliminar Tareas*]")
        input("No hay tareas registradas.")
    else:
        clearConsole()
        print("[Menu Tareas > *Eliminar Tareas*]")
        print()
        id = int(input("Ingrese el ID de la tarea a eliminar: "))
        isTaskReal = False

        for item in ListaTareas:
            if item[0] == id:
                isTaskReal = True
        if isTaskReal:
            del ListaTareas[id-1]
        else:
            input("[ERROR] La tarea con el ID ingresado no existe")  