from General.clearConsole import *

def mostrarListaTareas(ListaTareas):
    print(f"{'ID':<5}{'Nombre':<20}{'Fecha Inicio':<15}{'Fecha Final':<15}")
    print("-" * 55)
    
    for tarea in ListaTareas:
        id_tarea = tarea[0]
        nombre = tarea[1]
        fecha_inicio = tarea[2]
        fecha_final = tarea[3]
        
        print(f"{str(id_tarea)[0:4]:<5}{str(nombre)[0:20]:<25}{str(fecha_inicio):<15}{str(fecha_final):<15}")
        
    print("")

def ver_tareas(ListaTareas):
    clearConsole()
    print("[Menu Tareas > Ver Tareas]")
    print()
    if len(ListaTareas) == 0:
        print()
        input("No hay tareas registradas.")
    else:
        mostrarListaTareas(ListaTareas)
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
        print(nueva_tarea)
        input("[EXITO] Tarea creada exitosamente.")
    else:
        input("Operacion cancelada.")


def editar_tarea(ListaTareas):
    on = True
    
    if len(ListaTareas) == 0:
        clearConsole()
        print("[Menu Tareas > *Editar Tareas*]")
        print()
        input("No hay tareas registradas.")
    else:
        while on:   
            p1 = True
            p2 = False
            clearConsole()
            print("[Menu Tareas > Editar *Tareas*]")
            mostrarListaTareas(ListaTareas)
            #* Que_tarea? [POSICION]
            posicion = 0
            isTaskReal = False
            task_id = input("Ingrese ID de la tarea a editar\nIngrese 0 para vover atras: ")
            if task_id == "":
                print()
                input("[ERROR] El id no puede estar vacio")
            elif task_id.isdigit() == False:
                print()
                input("[ERROR] El id debe ser un numero")
            elif task_id == "0":
                on = False
                print()
                print("Volviendo al menu")
                input("Ingrese enter para continuar...")
            elif task_id.isdigit() == True and task_id != "":
                task_id = int(task_id)
                for item in ListaTareas:
                        if item[0] == task_id:
                            posicion = task_id - 1
                            isTaskReal = True
                            p1 = True

                while p1 and isTaskReal:
                    #* Menu con variables de ESA tarea (1. Cambiar Nombre - 2. Cambiar fecha de inicio - 3. Cambiar fecha final - 4. Nuevo estado de la tarea)
                    id = ListaTareas[posicion][0]
                    editarNombre = ListaTareas[posicion][1]
                    editarFechaInicio = ListaTareas[posicion][2]
                    editarFechaFinal = ListaTareas[posicion][3]

                    clearConsole()
                    print("[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Tareas*]")
                    print()
                    print("1. Cambiar Nombre")
                    print("2. Cambiar fecha de inicio")
                    print("3. Cambiar fecha final")
                    print("4. Cambiar el estado de la tarea")
                    print("0. Volver")
                    print("")
                    opcion = input("Seleccione una opcion")
                    
                    if opcion == "1":
                        clearConsole()
                        editarNombre=input("Ingrese el nuevo nombre de la tarea: ")
                        p1 = False
                        p2 = True

                    elif opcion == "2":
                        clearConsole()
                        editarFechaInicio=input("Ingrese la nueva fecha de inicio: ")
                        p1 = False
                        p2 = True

                    elif opcion == "3":
                        clearConsole()
                        editarFechaFinal=input("Ingrese la nueva fecha final: ")
                        p1 = False
                        p2 = True
                    
                    #elif opcion == "4": 
                    #    clearConsole()
                    #   editarEstado=input("Ingrese el nuevo estado de la tarea: ")
                    #   ListaTareas[posicion][5] = editarEstado
                    elif opcion == "0":
                        p1 = False
                        print("cancelando operacion...")
                        input("Ingrese enter para continuar...")
                    else:
                        input("[ERROR] Número inválido")

                    tarea_editada = [id,editarNombre,editarFechaInicio,editarFechaFinal]
                   

                while p2 and isTaskReal:
                    clearConsole()
                    print("[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Tareas*]")
                    print()
                    print(f"Nombre de la tarea: {editarNombre}")
                    print(f"Fecha de Inicio: {editarFechaInicio}")
                    print(f"Fecha Final: {editarFechaFinal}")
                    #print(f"Estado: {editarEstado}")
                    print()
                    opcion = input("¿Desea guardar los cambios? (s/n): ")
                    if opcion.lower() == "s":
                        ListaTareas[posicion] = tarea_editada
                        print()
                        input("Tarea editada exitosamente. Ingrese cualquier opcion para continuar.")
                        p2 = False
                        
                    elif opcion.lower() == "n":
                        print()
                        input("Tarea no guardada. Ingrese cualquier opcion para continuar.")
                        p2 = False

                    elif opcion == "":
                        print("opcion invalida")
                        input("ingrese cualquier opcion para continuar: ")    
                    else:
                        print("opcion invalida")
                        input("ingrese cualquier opcion para continuar: ")  

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
        id = input("Ingrese el ID de la tarea a eliminar: ")
        isTaskReal = False
        if id == "":
            print()
            input("[ERROR] El id no puede estar vacio")
        elif id.isdigit() == False:
            print()
            input("[ERROR] El id debe ser un numero")
        elif id.isdigit() == True and id != "":
            id = int(id)
            for item in ListaTareas:
                if item[0] == id:
                    isTaskReal = True
            if isTaskReal:
                del ListaTareas[id-1]
            else:
                input("[ERROR] La tarea con el ID ingresado no existe")  