from General.clearConsole import *
from General.inputFecha import *
from General.mostrarTareasProyectos import *

def formatearDescripcion(texto, max_caracteres=76):
    texto = str(texto)
    return texto[:max_caracteres - 3] + "..." if len(texto) > max_caracteres else texto

def mostrarListaTareas(ListaTareas):
    print(f"{'ID':<5}{'Nombre':<25}{'Descripcion':<33}{'Fecha Inicio':<15}{'Fecha Final':<15}{'Estado':<15}")
    print("-" * 108)
    
    for tarea in ListaTareas:
        id_tarea = tarea[0]
        nombre = tarea[1]
        descripcion = tarea[2]
        fecha_inicio = tarea[3]
        fecha_final = tarea[4]
        estado = tarea[5]

        nombre_formateado = str(nombre)[:20] + "..." if len(str(nombre)) > 20 else str(nombre)
        descripcion_formateada = str(descripcion)[:28] + "..." if len(str(descripcion)) > 28 else str(descripcion)
        print(f"{str(id_tarea):<5}{nombre_formateado:<25}{descripcion_formateada:<33}{(fecha_inicio).strftime('%d/%m/%Y'):<15}{(fecha_final).strftime('%d/%m/%Y'):<15}{str(estado):<15}")

    print("")

def seleccionar_tarea():
    pass

def ver_tareas(ListaTareas):
    clearConsole()
    print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Ver Tareas*]\033[0m")
    print()
    if len(ListaTareas) == 0:
        input("No hay tareas registradas.")
    else:
        mostrarListaTareas(ListaTareas)
        input("Ingrese cualquier opcion para continuar" )

def crear_tarea(ListaTareas):
    clearConsole()
    print("\033[33m[Menu Tareas > Crear Tareas]\033[0m")
    print()
    if len(ListaTareas) == 0:
        id = 1
    else:    
        id = ListaTareas[len(ListaTareas)-1][0]+1
    p1,p2,p3= True,False,False

    inProgress = True

    while p1 and inProgress:
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > *Crear Tarea*]\033[0m")
        print()
        nombreTarea=input("• Ingrese el nombre de la tarea (0 para cancelar): ")
        if nombreTarea == "":
            print("")
            input("\033[31m[ERROR] El nombre de la tarea no puede estar vacio.\033[0m")
        elif nombreTarea == "0":
            p1 = False
            inProgress = False
            print("")
            input("Operacion cancelada...")
        else:
            p1 = False
            p2 = True

    while p2 and inProgress:
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > *Crear Tarea*]\033[0m")
        print()
        print(f"Nombre de la tarea: {nombreTarea}")
        print()
        descripcionTarea=input("• Ingrese la descripcion de la tarea (0 para cancelar): ")
        if descripcionTarea == "":
            print("")
            input("\033[31m[ERROR] El nombre de la tarea no puede estar vacio.\033[0m")
        elif descripcionTarea == "0":
            p2 = False
            inProgress = False
            print("")
            input("Operacion cancelada...")
        else:
            p2 = False
            p3 = True

    while p3 and inProgress:
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > *Crear Tarea*]\033[0m")
        print()
        print(f"Nombre de la tarea: {nombreTarea}")
        print(f"Descripcion de la tarea: {formatearDescripcion(descripcionTarea)}")
        print()
        FechaInicio=inputFecha("Inicio")
        if FechaInicio == "":
            print("")
            input("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m") 
        elif FechaInicio == None:
            print("")
            input("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
        elif FechaInicio == "0":
            p3 = False
            inProgress = False
            print("")
            input("Operacion cancelada...")
        else:
            p3 = False
            p4 = True
    
    while p4 and inProgress:
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > *Crear Tarea*]\033[0m")
        print()
        print(f"Nombre de la tarea: {nombreTarea}")
        print(f"Descripcion de la tarea: {formatearDescripcion(descripcionTarea)}")
        print(f"Fecha de Inicio: {FechaInicio.strftime('%d/%m/%Y')}")
        print()
        FechaFinal=inputFecha("Final")
        if FechaFinal == "0":
            p4 = False
            inProgress = False
            print("")
            input("Operacion cancelada...")
        elif FechaFinal == "":
            print("")
            input("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m")
        elif FechaFinal == None:
            print("")
            input("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
        elif FechaFinal < FechaInicio:
            print("")
            input("\033[31m[ERROR] La fecha final no puede ser anterior a la fecha de inicio.\033[0m")
        else:
            p4 = False
            EstadoTarea = "Activo"
    
    if inProgress:
        #? Type Proyecto = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]
        nueva_tarea = [id,nombreTarea,descripcionTarea,FechaInicio,FechaFinal,EstadoTarea]
        
        ListaTareas.append(nueva_tarea)
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > *Crear Tarea*]\033[0m")
        print("")
        print(f"Nombre de la tarea: {nombreTarea}")
        print(f"Descripcion de la tarea: {formatearDescripcion(descripcionTarea)}")
        print(f"Fecha de Inicio: {FechaInicio.strftime('%d/%m/%Y')}")
        print(f"Fecha de Finalizacion: {FechaFinal.strftime('%d/%m/%Y')}")
        print(f"Estado: {EstadoTarea}")
        print()
        input("[EXITO] Tarea creada exitosamente.")
    else:
        # input("Operacion cancelada.")
        pass


def editar_tarea(ListaTareas):
    on = True
    
    if len(ListaTareas) == 0:
        clearConsole()
        print("\033[33m[Menu Tareas > *Editar Tareas*]\033[0m")
        print()
        input("No hay tareas registradas.")
    else:
        while on:   
            p1 = True
            p2 = False
            clearConsole()
            print("\033[33m[Menu Tareas > Editar *Tareas*]\033[0m")
            print()
            mostrarListaTareas(ListaTareas)
            #* Que_tarea? [POSICION]
            posicion = 0
            isTaskReal = False
            task_id = input("• Ingrese ID de la tarea a editar (0 para cancelar): ")
            if task_id == "":
                print()
                input("\033[31m[ERROR] El id no puede estar vacio.\033[0m")
            elif task_id.isdigit() == False:
                print()
                input("\033[31m[ERROR] El id debe ser un numero.\033[0m")
            elif task_id == "0":
                on = False
                print()
                input("Operacion cancelada")
            elif task_id.isdigit() == True and task_id != "":
                task_id = int(task_id)
                for item in ListaTareas:
                        if item[0] == task_id:
                            posicion = task_id - 1
                            isTaskReal = True
                            p1 = True

                while p1 and isTaskReal:
                    p4 = True
                    #* Menu con variables de ESA tarea (1. Cambiar Nombre - 2. Cambiar fecha de inicio - 3. Cambiar fecha final - 4. Nuevo estado de la tarea)
                    id = ListaTareas[posicion][0]
                    editarNombre = ListaTareas[posicion][1]
                    editarDescripcion = ListaTareas[posicion][2]
                    editarFechaInicio = ListaTareas[posicion][3]
                    editarFechaFinal = ListaTareas[posicion][4]
                    editarEstado = ListaTareas[posicion][5]
                   
                    clearConsole()
                    print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Tareas*]\033[0m")
                    print()
                    mostrar_tarea_proyecto("tarea", ListaTareas[posicion])
                    print("1. Cambiar Nombre")
                    print("2. Cambiar fecha de inicio")
                    print("3. Cambiar fecha final")
                    print("4. Cambiar el estado de la tarea")
                    print("0. Volver")
                    print("")
                    opcion = input("• Seleccione una opcion:")
                    
                    if opcion == "1":
                        while p4:    
                            clearConsole()
                            print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Tareas(Nombre)*]\033[0m")
                            print()
                            mostrar_tarea_proyecto("tarea", ListaTareas[posicion])
                            editarNombre=input("• Ingrese el nuevo nombre de la tarea (0 para cancelar): ")
                            if editarNombre == "":
                                print("")
                                print("\033[31m[ERROR] El nombre ingresado no puede estar vacio\033[0m")
                                input("Ingrese cualquier opcion para continuar...")
                            elif editarNombre == "0":
                                p4 = False
                                input("Operacion cancelada")
                            else:
                                p4 = False   
                                p1 = False
                                p2 = True
                    
                    elif opcion == "2":
                        while p4:  
                            clearConsole()
                            print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Tareas(Fecha de Inicio)*]\033[0m")
                            print()
                            mostrar_tarea_proyecto("tarea", ListaTareas[posicion])
                            editarFechaInicio=inputFecha("Inicio")
                            if editarFechaInicio == "":
                                print("")
                                print("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m")
                                input("Ingrese cualquier opcion para continuar...")
                            elif editarFechaInicio == "0":
                                p4 = False
                                input("Operacion cancelada")
                            elif editarFechaInicio == None:
                                print("")
                                print("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
                                input("Ingrese cualquier opcion para continuar...")
                            elif editarFechaInicio > editarFechaFinal:
                                print("")
                                print("\033[31m[ERROR] La fecha de inicio no puede ser posterior a la fecha final.\033[0m")
                                input("Ingrese cualquier opcion para continuar...")
                            else:
                                p4 = False   
                                p1 = False
                                p2 = True
                            
                    elif opcion == "3":
                        while p4:   
                            clearConsole()
                            print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Tareas(Fecha Final)*]\033[0m")
                            print()
                            mostrar_tarea_proyecto("tarea", ListaTareas[posicion])
                            editarFechaFinal=inputFecha("Final")
                            if editarFechaFinal == "":
                                print("")
                                print("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m")
                                input("Ingrese cualquier opcion para continuar...")
                            elif editarFechaFinal == "0":
                                p4 = False
                                input("Operacion cancelada")
                            elif editarFechaFinal == None:
                                print("")
                                print("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
                                input("Ingrese cualquier opcion para continuar...")
                            elif editarFechaFinal < editarFechaInicio:
                                print("")
                                print("\033[31m[ERROR] La fecha final no puede ser anterior a la fecha de inicio.\033[0m")
                                input("Ingrese cualquier opcion para continuar...")
                            else:
                                p4 = False   
                                p1 = False
                                p2 = True
                    
                    elif opcion == "4": 
                        clearConsole()
                        while p4:
                            clearConsole()
                            print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Tareas(Estado)*]\033[0m")
                            print()
                            mostrar_tarea_proyecto("tarea", ListaTareas[posicion])
                            print("1. Activo")
                            print("2. Inactivo")
                            print()
                            editarEstado=input("• Ingrese el nuevo estado de la tarea: ")
                            ListaTareas[posicion][5] = editarEstado
                            if editarEstado == "1":
                                editarEstado = "Activo"
                                ListaTareas[posicion][5] = editarEstado
                                p4 = False
                                p1 = False
                                p2 = True
                            elif editarEstado == "2":
                                editarEstado = "Inactivo"
                                ListaTareas[posicion][5] = editarEstado
                                p4 = False
                                p1 = False
                                p2 = True
                            elif opcion == "":
                                print("Opcion invalida. Intente nuevamente.")
                                input("Ingrese cualquier opcion para continuar...")
                            else:
                                print("Opcion invalida. Intente nuevamente.")
                                input("Ingrese cualquier opcion para continuar...")
                    elif opcion == "0":
                        p1 = False
                        input("Operacion cancelada")
                    else:
                        input("\033[31m[ERROR] Número inválido.\033[0m")

                    tarea_editada = [id,editarNombre,editarDescripcion,editarFechaInicio,editarFechaFinal,editarEstado]
                   

                while p2 and isTaskReal:
                    clearConsole()
                    print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Tareas*]\033[0m")
                    print()
                    print(f"Nombre: {editarNombre}")
                    print(f"Descripcion: {formatearDescripcion(editarDescripcion)}")
                    print(f"Fecha de Inicio: {editarFechaInicio.strftime('%d/%m/%Y')}")
                    print(f"Fecha Final: {editarFechaFinal.strftime('%d/%m/%Y')}")
                    print(f"Estado: {editarEstado}")
                    print()
                    opcion = input("¿Desea guardar los cambios? (1 = Si | 0 = No): ")
                    if opcion == "1":
                        ListaTareas[posicion] = tarea_editada
                        print()
                        input("Tarea editada exitosamente. Ingrese cualquier opcion para continuar.")
                        p2 = False
                        
                    elif opcion == "0":
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
                input("\033[31m[ERROR] La tarea ingresada no existe.\033[0m")


def eliminar_tarea(ListaTareas):
    clearConsole()
    print("\033[33m[Menu Tareas > *Eliminar Tareas*]\033[0m")
    print()
    if len(ListaTareas) == 0:
        input("No hay tareas registradas.")
    else:
        on = True
        while on:
            id = input("• Ingrese el ID de la tarea a eliminar: ")
            isTaskReal = False
            if id == "":
                print()
                input("\033[31m[ERROR] El id no puede estar vacio.\033[0m")
            elif id.isdigit() == False:
                print()
                input("\033[31m[ERROR] El id debe ser un numero.\033[0m") 
            elif id == "0":
                on = False
                print()
                input("Operacion cancelada")
            else:
                id = int(id)
                for item in ListaTareas:
                    if item[0] == id:
                        isTaskReal = True
                if isTaskReal:
                    del ListaTareas[id-1]
                    on = False
                    print()
                    print("Tarea eliminada exitosamente. Ingrese cualquier opcion para continuar.")
                    input("Ingrese cualquier opcion para continuar...")
                else:
                    input("\033[31m[ERROR] La tarea con el ID ingresado no existe.\033[0m")
