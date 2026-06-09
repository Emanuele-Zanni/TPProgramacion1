from General.clearConsole import *
from General.inputFecha import *
from Tareas.funciones import *
# from Proyectos.menus import imprimirMenuSeleccionarProyecto

def mostrarListaProyectos(ListaProyectos):
        print(f"{'ID':<5}{'Nombre':<25}{'Tareas':<15}{'Inicio':<12}{'Fin':<12}{'Estado':<10}")
        print("-" * 75)
        
        for proyecto in ListaProyectos:
            id_ = proyecto[0]
            nombre = proyecto[1]
            tareas = len(proyecto[2])  # cantidad de tareas en vez de []
            inicio = proyecto[3]
            fin = proyecto[4]
            estado = proyecto[5]
            
            if len(nombre) > 20 and len(str(tareas)) > 10:
                print(f"{id_:<5}{nombre[:20]+ '...':<25}{str(tareas)[:10]+ '...':<15}{inicio.strftime('%d/%m/%Y'):<12}{fin.strftime('%d/%m/%Y'):<12}{estado:<10}")
           
            elif  len(str(tareas)) > 10:
                print(f"{id_:<5}{nombre:<25}{str(tareas)[:10]+ '...':<15}{inicio.strftime('%d/%m/%Y'):<12}{fin.strftime('%d/%m/%Y'):<12}{estado:<10}")
            
            elif len(nombre) > 20:
                print(f"{id_:<5}{nombre[:20]+ '...':<25}{str(tareas):<15}{inicio.strftime('%d/%m/%Y'):<12}{fin.strftime('%d/%m/%Y'):<12}{estado:<10}")
           
            else:
                print(f"{id_:<5}{nombre:<25}{str(tareas):<15}{inicio.strftime('%d/%m/%Y'):<12}{fin.strftime('%d/%m/%Y'):<12}{estado:<10}")
        print("")
    

def ver_proyectos(ListaProyectos):
    clearConsole()
    print("\033[33m[Menu Principal > Proyectos > *Ver Proyectos*]\033[0m")
    print()       
    
    if len(ListaProyectos) == 0:
        input("No hay proyectos registrados.")
    elif len(ListaProyectos) > 0:
        mostrarListaProyectos(ListaProyectos)
        input("Ingrese cualquier opcion para continuar...")


def seleccionar_proyecto(ListaProyectos, credencial):
        isProjectReal = False
        p1 = True
        inProgress = True


        if len(ListaProyectos) == 0:
            clearConsole()
            print("\033[33m[Menu principal > Proyectos > *Seleccionar Proyectos*]\033[0m")
            print()
            input("No hay proyectos registrados.")
        else:
            while p1 and inProgress:
                clearConsole()
                print("\033[33m[Menu principal > Proyectos > *Seleccionar Proyectos*]\033[0m")
                print()
                mostrarListaProyectos(ListaProyectos)
                id = input("• Ingrese el ID del proyecto a seleccionar (0 para cancelar): ")
                if id.isdigit():
                    if id == "0":
                        inProgress = False
                        print()
                        input("Operacion cancelada")
                    else:    
                        id = int(id)
                        for project in ListaProyectos:
                            if project[0] == id:   
                                isProjectReal = True
                                proyecto = project
                                p1 = False
                        if not isProjectReal:
                            print()
                            input("\033[31m[ERROR] El ID ingresado no pertenece a ningun proyecto.\033[0m")
               
                elif id == "":
                    print("")
                    input("\033[31m[ERROR] El id no puede estar vacio.\033[0m")

                else:
                    print("")
                    input("\033[31m[ERROR] El ID ingresado debe ser un numero.\033[0m")
                        
            if isProjectReal:
                on = True
                while on:
                    clearConsole()
                    print("\033[33m[Menu principal > Proyectos > *Proyecto Seleccionado*]\033[0m")
                    print() 
                    mostrar_tarea_proyecto("proyecto", proyecto)
                    print("")

                    if credencial["clearance"] == 1:
                        print("1. Ver tarea")
                        print("?. Seleccionar tarea (WIP)")
                        print("0. Volver atras")
                        print()
                        opcion=input("• Seleccione una opcion: ")
                        if opcion=="1":
                            ver_tareas(proyecto[2])
                        elif opcion=="0":
                            on=False
                        else:
                            input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
                    else:
                        print("1. Ver tarea")
                        print("2. Crear tarea")
                        print("3. Editar tarea")
                        print("4. Eliminar tarea")
                        print("0. Volver atras")
                        print()
                        opcion=input("• Seleccione una opcion: ")
                        if opcion=="1":
                            ver_tareas(proyecto[2])
                        elif opcion=="2":
                            crear_tarea(proyecto[2])
                        elif opcion=="3":
                            editar_tarea(proyecto[2])
                        elif opcion=="4":
                            eliminar_tarea(proyecto[2])
                        elif opcion=="0":
                            on=False
                        else:
                            input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
    

def crear_proyecto(ListaProyectos):
    clearConsole()
    print("\033[33m[Menu Principal > Proyectos > *Crear Proyectos*]\033[0m")
    print()
    #* Variables para inicializar las flags para persistencia de inputs + validaciones
    inProgress = True
    p1,p2,p3 = True,False,False
    if len(ListaProyectos) == 0:
        id = 1
    else:    
        id = ListaProyectos[len(ListaProyectos)-1][0]+1
    tareas = []
    Estado = "Activo?" #* Hacer enum!

    while p1 and inProgress:
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > *Crear Proyectos*]\033[0m")
        print()
        nombreProyecto=input("• Ingrese el nombre del proyecto (0 para cancelar): ")  
        if nombreProyecto == "":
            print("")
            input("\033[31m[ERROR] El nombre ingresado no puede estar vacio.\033[0m") 
        elif nombreProyecto == "0":
            inProgress = False
            print()
            input("Operacion cancelada")
        else:
            p1 = False
            p2 = True

    while p2 and inProgress: 
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > *Crear Proyectos*]\033[0m")
        print()
        print(f"Nombre del Proyecto: {nombreProyecto}")
        FechaInicio=inputFecha("Inicio")
        if FechaInicio == "":
            print("")
            input("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m") 
        elif FechaInicio == "0":
            inProgress = False
            print()
            input("Operacion cancelada")
        elif FechaInicio == None:
            print("")
            input("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
        else:
            p2 = False
            p3 = True
    
    while p3 and inProgress:
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > *Crear Proyectos*]\033[0m")
        print()
        print(f"Nombre del Proyecto: {nombreProyecto}")
        print(f"Fecha de Inicio: {FechaInicio.strftime('%d/%m/%Y')}")
        FechaFinal=inputFecha("Final")
        if FechaFinal == None:
            print("")
            input("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
        elif FechaFinal < FechaInicio:
            print("")
            input("\033[31m[ERROR] La fecha final no puede ser anterior a la fecha de inicio.\033[0m")
        elif FechaFinal == "0":
            inProgress = False
            print()
            input("Operacion cancelada")
        else:
            Estado = "Activo"
            p3 = False

    if inProgress:

        #? Type Proyecto = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]
        nuevo_proyecto = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]
        
        ListaProyectos.append(nuevo_proyecto)
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > *Crear Proyectos*]\033[0m")
        print()
        print(f"ID: {id}")
        print(f"Nombre del Proyecto: {nombreProyecto}")
        print(f"Fecha de Inicio: {FechaInicio.strftime('%d/%m/%Y')}")
        print(f"Fecha de Finalizacion: {FechaFinal.strftime('%d/%m/%Y')}")
        print()
        input("[EXITO] Proyecto creado exitosamente.")

#no basico
def editar_proyecto(ListaProyectos):
    on = True
    
    if len(ListaProyectos) == 0:
        clearConsole()
        print("\033[33m[Menu Proyectos > *Editar Proyectos*]\033[0m")
        print()
        input("No hay proyectos registrados.")
    else:
        while on:   
            p1 = True
            p2 = False
            clearConsole()
            print("\033[33m[Menu Proyectos > *Editar Proyectos*]\033[0m")
            print()
            mostrarListaProyectos(ListaProyectos)
            #* Que_proyecto? [POSICION]
            posicion = 0
            isProjectReal = False
            project_id = input("• Ingrese ID del proyecto a editar (0 para vover cancelar): ")
            if project_id == "":
                print()
                input("\033[31m[ERROR] El id no puede estar vacio.\033[0m")
            elif project_id.isdigit() == False:
                print()
                input("\033[31m[ERROR] El id debe ser un numero.\033[0m")
            elif project_id == "0":
                on = False
                # print()
                # input("Volviendo al menu...")
                input("Operacion cancelada")
            elif project_id.isdigit() == True and project_id != "":
                project_id = int(project_id)
                for item in ListaProyectos:
                        if item[0] == project_id:
                            posicion = project_id - 1
                            isProjectReal = True
                            p1 = True

                while p1 and isProjectReal:
                    #* Menu con variables de ESA tarea (1. Cambiar Nombre - 2. Cambiar fecha de inicio - 3. Cambiar fecha final - 4. Nuevo estado de la tarea)
                    id = ListaProyectos[posicion][0]
                    editarNombre = ListaProyectos[posicion][1]
                    editarFechaInicio = ListaProyectos[posicion][3]
                    editarFechaFinal = ListaProyectos[posicion][4]
                    editarEstado = ListaProyectos[posicion][5]

                    clearConsole()
                    print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos*]\033[0m")
                    print()
                    print("1. Cambiar Nombre")
                    print("2. Cambiar fecha de inicio")
                    print("3. Cambiar fecha final")
                    print("4. Cambiar el estado del proyecto")
                    print("0. Volver")
                    print("")
                    opcion = input("• Seleccione una opcion:")
                    p4 = True

                    if opcion == "1":
                        while p4:    
                            clearConsole()
                            print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos(Nombre)*]\033[0m")
                            print()
                            mostrar_tarea_proyecto("proyecto", ListaProyectos[posicion])
                            editarNombre=input("• Ingrese el nuevo nombre del proyecto (0 para cancelar): ")
                            if editarNombre == "":
                                print("")
                                input("\033[31m[ERROR] El nombre ingresado no puede estar vacio.\033[0m")
                            elif editarNombre == "0":
                                p4 = False
                                input("Operacion cancelada...")
                            else:
                                p4 = False   
                                p1 = False
                                p2 = True
                    
                    elif opcion == "2":
                        while p4:  
                            clearConsole()
                            print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos(Fecha de Inicio)*]\033[0m")
                            print()
                            mostrar_tarea_proyecto("proyecto", ListaProyectos[posicion])
                            editarFechaInicio=inputFecha("Inicio")
                            if editarFechaInicio == "":
                                print("")
                                input("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m")
                            elif editarFechaInicio == None:
                                print("")
                                input("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
                            elif editarFechaInicio == "0":
                                p4 = False
                                input("Operacion cancelada...")
                            elif editarFechaInicio > editarFechaFinal:
                                print("")
                                input("\033[31m[ERROR] La fecha de inicio no puede ser posterior a la fecha final.\033[0m")
                            else:
                                p4 = False   
                                p1 = False
                                p2 = True
                            
                    elif opcion == "3":
                        while p4:   
                            clearConsole()
                            print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos(Fecha Final)*]\033[0m")
                            print()
                            mostrar_tarea_proyecto("proyecto", ListaProyectos[posicion])
                            editarFechaFinal=inputFecha("Final")
                            if editarFechaFinal == "":
                                print("")
                                input("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m")
                            elif editarFechaFinal == "0":
                                p4 = False
                                input("Operacion cancelada...")
                            elif editarFechaFinal == None:
                                print("")
                                input("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
                            elif editarFechaFinal < editarFechaInicio:
                                print("")
                                input("\033[31m[ERROR] La fecha final no puede ser anterior a la fecha de inicio.\033[0m")
                            else:
                                p4 = False   
                                p1 = False
                                p2 = True
                    
                    elif opcion == "4": 
                        clearConsole()
                        while p4:
                            clearConsole()
                            print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos(Estado)*]\033[0m")
                            print()
                            mostrar_tarea_proyecto("proyecto", ListaProyectos[posicion])
                            print("1. Activo")
                            print("2. Inactivo")
                            print()
                            editarEstado=input("• Ingrese el nuevo estado del proyecto: ")
                            ListaProyectos[posicion][4] = editarEstado
                            if editarEstado == "1":
                                editarEstado = "Activo"
                                ListaProyectos[posicion][4] = editarEstado
                                p4 = False
                                p1 = False
                                p2 = True
                            elif editarEstado == "2":
                                editarEstado = "Inactivo"
                                ListaProyectos[posicion][4] = editarEstado
                                p4 = False
                                p1 = False
                                p2 = True
                            elif opcion == "":
                                print("Opcion invalida. Intente nuevamente.")
                                input("Ingrese cualquier opcion para continuar...")
                            elif editarEstado == "0":
                                p4 = False
                                input("Operacion cancelada...")
                            else:
                                print("Opcion invalida. Intente nuevamente.")
                                input("Ingrese cualquier opcion para continuar...")
                    elif opcion == "0":
                        p1 = False
                        input("Operacion Cancelada...")
                    else:
                        input("\033[31m[ERROR] Número inválido.\033[0m")

                    proyecto_editado = [id,editarNombre,editarFechaInicio,editarFechaFinal,editarEstado]

                while p2 and isProjectReal:
                    clearConsole()
                    print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos*]\033[0m")
                    print()
                    print(f"Nombre del proyecto: {editarNombre}")
                    print(f"Fecha de Inicio: {editarFechaInicio.strftime('%d/%m/%Y')}")
                    print(f"Fecha Final: {editarFechaFinal.strftime('%d/%m/%Y')}")
                    print(f"Estado: {editarEstado}")
                    print()
                    opcion = input("¿Desea guardar los cambios? (1 = Si | 0 = No): ")
                    if opcion == "1":
                        ListaProyectos[posicion] = proyecto_editado
                        print()
                        input("Proyecto editado exitosamente. Ingrese cualquier opcion para continuar.")
                        p2 = False
                        
                    elif opcion == "0":
                        print()
                        input("Proyecto no guardado. Ingrese cualquier opcion para continuar.")
                        p2 = False

                    elif opcion == "":
                        print("opcion invalida")
                        input("ingrese cualquier opcion para continuar: ")    
                    else:
                        print("opcion invalida")
                        input("ingrese cualquier opcion para continuar: ")  

            else:
                input("\033[31m[ERROR] El proyecto ingresado no existe.\033[0m")
   
                                                               
#no basico
def eliminar_proyecto(ListaProyectos):
    on = True
    while on:    
        clearConsole()
        print("\033[33m[Menu principal > Proyectos > *Eliminar Proyectos*]\033[0m")
        print()
        if len(ListaProyectos) == 0:
            input("No hay proyectos registrados.")
        else:
            #* Aca falta agregar validacion de input NO numerico para que no rompa (y conversor de texto a num)
            id = input("• Ingrese el ID del proyecto a eliminar (0 para cancelar): ")
            isProjectReal = False

            if id == "":
                print()
                input("\033[31m[ERROR] El id no puede estar vacio.\033[0m")
            elif id == "0":
                on = False
                print()
                input("Operacion cancelada")
            else:
                id = int(id)
                for item in ListaProyectos:
                    if item[0] == id:
                        isProjectReal = True
                        p1 = True
                        while p1: 
                            clearConsole()
                            print("\033[33m[Menu principal > Proyectos > *Eliminar Proyectos*]\033[0m")
                            print()  
                            mostrar_tarea_proyecto("proyecto", item)
                            print()
                            opcion = input("¿Desea eliminar este proyecto? (1 = Si | 0 = No): ")
                            if opcion == "1":
                                ListaProyectos.remove(item)
                                input(f"'{item}' eliminado exitosamente")
                                p1 = False
                                on = False
                            elif opcion == "0":
                                p1 = False
                                on = False
                                print()
                                input("Operacion cancelada")
                            else:
                                print()
                                input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")

                if isProjectReal == False:
                    print()
                    input("\033[31m[ERROR] El proyecto con el ID ingresado no existe.\033[0m")
