def ver_tareas(ListaTareas):
    if len(ListaTareas) == 0:
        print("No hay tareas registradas.")
        return
    elif len(ListaTareas) > 0:
        for tarea in ListaTareas:
            print(tarea)


def crear_tarea(ListaTareas):
    id = len(ListaTareas) + 1
    nombreTarea=input("Ingrese el nombre de la tarea: ")
    #! INTEGRANTES ASIGNADOS ???
    FechaInicio=input("Ingrese la fecha de inicio de la tarea: ")
    FechaFinal=input("Ingrese la fecha de la tarea:")
    Estado=input("Ingrese el estado de la tarea:")
    #* Enum

    nueva_tarea = [id,nombreTarea,FechaInicio,FechaFinal,Estado]
    
    ListaTareas.append(nueva_tarea) 

    input("Tarea Creada Exitosamente!")
    
    # ListaTareas = ["id","nombre","integranteAsignados","fechaInicio","FechaFinal","estadoTarea"]

    # return nueva_tarea


def editar_tarea(ListaTareas):
    #* Que_tarea? [POSICION]
    posicion = 0
    isTaskReal = False
    task_id = int(input("Ingrese ID de la tarea a editar: "))
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
            print("Número inválido")

        # tarea_editada = [id,nombreTarea,tareas,FechaInicio,FechaFinal,Estado]

    else:
        print("La tarea ingresada no existe")


def eliminar_tarea(ListaTareas):
    id = int(input("Ingrese el ID de la tarea a eliminar: "))
    isTaskReal = False

    for item in ListaTareas:
        if item[0] == id:
            isTaskReal = True

    if isTaskReal:
        del ListaTareas[id-1]


    else:
        print("La tarea con el ID ingresado no existe")  