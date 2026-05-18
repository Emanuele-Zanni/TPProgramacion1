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
                print(f"{id_:<5}{nombre[:20]+ '...':<25}{str(tareas)[:10]+ '...':<15}{inicio:<12}{fin:<12}{estado:<10}")
           
            elif  len(str(tareas)) > 10:
                print(f"{id_:<5}{nombre:<25}{str(tareas)[:10]+ '...':<15}{inicio:<12}{fin:<12}{estado:<10}")
            
            elif len(nombre) > 20:
                print(f"{id_:<5}{nombre[:20]+ '...':<25}{str(tareas):<15}{inicio:<12}{fin:<12}{estado:<10}")
           
            else:
                print(f"{id_:<5}{nombre:<25}{str(tareas):<15}{inicio:<12}{fin:<12}{estado:<10}")
        print("")
    

def ver_proyectos(ListaProyectos):
    clearConsole()
    print("[Menu Principal > Proyectos > *Ver Proyectos*]")
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
            print("[Menu principal > Proyectos > *Seleccionar Proyectos*]")
            print()
            input("No hay proyectos registrados.")
        else:
            while p1 and inProgress:
                clearConsole()
                print("[Menu principal > Proyectos > *Seleccionar Proyectos*]")
                print()
                mostrarListaProyectos(ListaProyectos)
                id = input("ingrese el ID del proyecto a seleccionar (0 para cancelar): ")
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
                            input("[ERROR] El ID ingresado no pertenece a ningun proyecto")
               
                elif id == "":
                    print("")
                    input("[ERROR] El id no puede estar vacio")

                else:
                    print("")
                    input("[ERROR] El ID ingresado debe ser un numero")
                        
            if isProjectReal:
                on = True
                while on:
                    clearConsole()
                    print("[Menu principal > Proyectos > *Proyecto Seleccionado*]")
                    print() 
                    print(f"=== {proyecto[1]} ===")
                    print(f"ID: {proyecto[0]} | Status: {proyecto[5]} | Fecha Inicio/Final: {proyecto[3]} - {proyecto[4]}")
                    print("")

                    if credencial["clearance"] == 1:
                        print("1. Ver tarea")
                        print("?. Seleccionar tarea (WIP)")
                        print("0. Volver atras")
                        opcion=input("Seleccione una opcion: ")
                        if opcion=="1":
                            ver_tareas(proyecto[2])
                        elif opcion=="0":
                            on=False
                        else:
                            input("Opcion invalida. Intente nuevamente.")
                    else:
                        print("1. Ver tarea")
                        print("2. Crear tarea")
                        print("3. Editar tarea")
                        print("4. Eliminar tarea")
                        print("0. Volver atras")
                        opcion=input("Seleccione una opcion: ")
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
                            input("Opcion invalida. Intente nuevamente.")
    

def crear_proyecto(ListaProyectos):
    clearConsole()
    print("[Menu Principal > Proyectos > *Crear Proyectos*]")
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
        print("[Menu Principal > Proyectos > *Crear Proyectos*]")
        print()
        nombreProyecto=input("• Ingrese el nombre del proyecto (0 para cancelar): ")  
        if nombreProyecto == "":
            print("")
            input("[ERROR] El nombre ingresado no puede estar vacio") 
        elif nombreProyecto == "0":
            inProgress = False
            print()
            print("Operacion cancelada")
            input("Ingrese enter para continuar...")
        else:
            p1 = False
            p2 = True

    while p2 and inProgress: 
        clearConsole()
        print("[Menu Principal > Proyectos > *Crear Proyectos*]")
        print()
        print(f"Nombre del Proyecto: {nombreProyecto}")
        FechaInicio=inputFecha(nombreProyecto,"Inicio")
        if FechaInicio == "":
            print("")
            input("[ERROR] La fecha ingresada no puede estar vacia") 
        elif FechaInicio == "0":
            inProgress = False
            print()
            print("Operacion cancelada")
            input("Ingrese enter para continuar...")
        else:
            p2 = False
            p3 = True
    
    while p3 and inProgress:
        
        print("[Menu Principal > Proyectos > *Crear Proyectos*]")
        print()
        print(f"Nombre del Proyecto: {nombreProyecto}")
        print(f"Fecha de Inicio: {FechaInicio}")
        FechaFinal=inputFecha(nombreProyecto,"Final", FechaInicio)
        if FechaFinal < FechaInicio:
            print("")
            input("[ERROR] La fecha final no puede ser anterior a la fecha de inicio")
        elif FechaFinal == "0":
            inProgress = False
            print()
            print("Operacion cancelada")
            input("Ingrese enter para continuar...")
        else:
            Estado = "Activo"
            p3 = False

    if inProgress:

        #? Type Proyecto = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]
        nuevo_proyecto = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]
        
        ListaProyectos.append(nuevo_proyecto)
        clearConsole()
        print("[Menu Principal > Proyectos > *Crear Proyectos*]")
        print()
        print(f"ID: {id}")
        print(f"Nombre del Proyecto: {nombreProyecto}")
        print(f"Fecha de Inicio: {FechaInicio}")
        print(f"Fecha de Finalizacion: {FechaFinal}")
        print()
        input("[EXITO] Proyecto creado exitosamente.")

#no basico
def editar_proyecto(ListaProyectos):
    on = True
    
    if len(ListaProyectos) == 0:
        clearConsole()
        print("[Menu Proyectos > *Editar Proyectos*]")
        print()
        input("No hay proyectos registrados.")
    else:
        while on:   
            p1 = True
            p2 = False
            clearConsole()
            print("[Menu Proyectos > Editar *Proyectos*]")
            mostrarListaProyectos(ListaProyectos)
            #* Que_proyecto? [POSICION]
            posicion = 0
            isProjectReal = False
            project_id = input("Ingrese ID del proyecto a editar\nIngrese 0 para vover atras: ")
            if project_id == "":
                print()
                input("[ERROR] El id no puede estar vacio")
            elif project_id.isdigit() == False:
                print()
                input("[ERROR] El id debe ser un numero")
            elif project_id == "0":
                on = False
                print()
                print("Volviendo al menu")
                input("Ingrese enter para continuar...")
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
                    print("[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos*]")
                    print()
                    print("1. Cambiar Nombre")
                    print("2. Cambiar fecha de inicio")
                    print("3. Cambiar fecha final")
                    print("4. Cambiar el estado del proyecto")
                    print("0. Volver")
                    print("")
                    opcion = input("Seleccione una opcion")
                    
                    if opcion == "1":
                        while p4:    
                            clearConsole()
                            print("[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos(Nombre)*]")
                            print()
                            print(f" ===== Proyecto{id+1} ======") 
                            print(f"{"ID": <5}{"Nombre": <25}|{"Fecha de Inicio": <15}|{"Fecha Final": <15}|{"Estado": <15}")
                            print("---------------------------------------------------------------------------------")
                            if len(ListaProyectos[posicion][1]) > 20:
                                print(f"{ListaProyectos[posicion][0]:<5}{ListaProyectos[posicion][1][:20]+ '...':<25}{ListaProyectos[posicion][3]:<15}{ListaProyectos[posicion][4]:<15}{ListaProyectos[posicion][5]:<15}")
                            else:   
                                print(f"{ListaProyectos[posicion][0]:<5}{ListaProyectos[posicion][1]:<25}{ListaProyectos[posicion][3]:<15}{ListaProyectos[posicion][4]:<15}{ListaProyectos[posicion][5]:<15}")
                            print()
                            editarNombre=input("Ingrese el nuevo nombre del proyecto (0 para cancelar): ")
                            if editarNombre == "":
                                print("")
                                input("[ERROR] El nombre ingresado no puede estar vacio")
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
                            print("[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos(Fecha de Inicio)*]")
                            print()
                            print(f" ===== Proyecto{id+1} ======")  
                            print(f"{"ID": <5}{"Nombre": <25}|{"Fecha de Inicio": <15}|{"Fecha Final": <15}|{"Estado": <15}")
                            print("---------------------------------------------------------------------------------")
                            if len(ListaProyectos[posicion][1]) > 20:
                                print(f"{ListaProyectos[posicion][0]:<5}{ListaProyectos[posicion][1][:20]+ '...':<25}{ListaProyectos[posicion][3]:<15}{ListaProyectos[posicion][4]:<15}{ListaProyectos[posicion][5]:<15}")
                            else:   
                                print(f"{ListaProyectos[posicion][0]:<5}{ListaProyectos[posicion][1]:<25}{ListaProyectos[posicion][3]:<15}{ListaProyectos[posicion][4]:<15}{ListaProyectos[posicion][5]:<15}")
                            print()
                            editarFechaInicio=input("Ingrese la nueva fecha de inicio (0 para cancelar): ")
                            if editarFechaInicio == "":
                                print("")
                                input("[ERROR] La fecha ingresada no puede estar vacia")
                            elif editarFechaInicio.isdigit() == False:
                                print("")
                                input("[ERROR] La fecha ingresada debe ser un numero")
                            elif editarFechaInicio == "0":
                                p4 = False
                                input("Operacion cancelada...")
                            else:
                                p4 = False   
                                p1 = False
                                p2 = True
                            
                    elif opcion == "3":
                        while p4:   
                            clearConsole()
                            print("[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos(Fecha Final)*]")
                            print()
                            print(f" ===== Proyecto{id+1} ======") 
                            print(f"{"ID": <5}{"Nombre": <25}|{"Fecha de Inicio": <15}|{"Fecha Final": <15}|{"Estado": <15}")
                            print("---------------------------------------------------------------------------------")
                            if len(ListaProyectos[posicion][1]) > 20:
                                print(f"{ListaProyectos[posicion][0]:<5}{ListaProyectos[posicion][1][:20]+ '...':<25}{ListaProyectos[posicion][3]:<15}{ListaProyectos[posicion][4]:<15}{ListaProyectos[posicion][5]:<15}")
                            else:   
                                print(f"{ListaProyectos[posicion][0]:<5}{ListaProyectos[posicion][1]:<25}{ListaProyectos[posicion][3]:<15}{ListaProyectos[posicion][4]:<15}{ListaProyectos[posicion][5]:<15}")
                            print()
                            editarFechaFinal=input("Ingrese la nueva fecha final (0 para cancelar): ")
                            if editarFechaFinal == "":
                                print("")
                                input("[ERROR] La fecha ingresada no puede estar vacia")
                            elif editarFechaFinal.isdigit() == False:
                                print("")
                                input("[ERROR] La fecha ingresada debe ser un numero")
                            elif editarFechaFinal < editarFechaInicio:
                                print("")
                                input("[ERROR] La fecha final no puede ser anterior a la fecha de inicio")
                            elif editarFechaFinal == "0":
                                p4 = False
                                input("Operacion cancelada...")
                            else:
                                p4 = False   
                                p1 = False
                                p2 = True
                    
                    elif opcion == "4": 
                        clearConsole()
                        while p4:
                            clearConsole()
                            print("[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos(Estado)*]")
                            print()
                            print(f" ===== Proyecto{id+1} ======") 
                            print(f"{"ID": <5}{"Nombre": <25}|{"Fecha de Inicio": <15}|{"Fecha Final": <15}|{"Estado": <15}")
                            print("---------------------------------------------------------------------------------")
                            if len(ListaProyectos[posicion][1]) > 20:
                                print(f"{ListaProyectos[posicion][0]:<5}{ListaProyectos[posicion][1][:20]+ '...':<25}{ListaProyectos[posicion][3]:<15}{ListaProyectos[posicion][4]:<15}{ListaProyectos[posicion][5]:<15}")
                            else:   
                                print(f"{ListaProyectos[posicion][0]:<5}{ListaProyectos[posicion][1]:<25}{ListaProyectos[posicion][3]:<15}{ListaProyectos[posicion][4]:<15}{ListaProyectos[posicion][5]:<15}")
                            print()
                            print("1. Activo")
                            print("2. Inactivo")
                            editarEstado=input("Ingrese el nuevo estado del proyecto: ")
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
                            else:
                                print("Opcion invalida. Intente nuevamente.")
                                input("Ingrese cualquier opcion para continuar...")
                    elif opcion == "0":
                        p1 = False
                        print("cancelando operacion...")
                        input("Ingrese enter para continuar...")
                    else:
                        input("[ERROR] Número inválido")

                    proyecto_editado = [id,editarNombre,editarFechaInicio,editarFechaFinal,editarEstado]

                while p2 and isProjectReal:
                    clearConsole()
                    print("[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos*]")
                    print()
                    print(f"Nombre del proyecto: {editarNombre}")
                    print(f"Fecha de Inicio: {editarFechaInicio}")
                    print(f"Fecha Final: {editarFechaFinal}")
                    print(f"Estado: {editarEstado}")
                    print()
                    opcion = input("¿Desea guardar los cambios?\nsi == 1\nno == 0: ")
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
                input("[ERROR] El proyecto ingresado no existe")
   
                                                               
#no basico
def eliminar_proyecto(ListaProyectos):
    on = True
    while on:    
        clearConsole()
        print("[Menu principal > Proyectos > *Eliminar Proyectos*]")
        print()
        if len(ListaProyectos) == 0:
            input("No hay proyectos registrados.")
        
        else:
        
            #* Aca falta agregar validacion de input NO numerico para que no rompa (y conversor de texto a num)
            id = input("Ingrese el ID del proyecto a eliminar\ningrese 0 para cancelar: ")
            isProjectReal = False

            if id == "":
                print()
                print("[ERROR] El id no puede estar vacio")
                input("Ingrese enter para continuar...")
            elif id == "0":
                on = False
                print()
                print("Operacion cancelada")
                input("Ingrese enter para continuar...")
            else:
                id = int(id)
                for item in ListaProyectos:
                    if item[0] == id:
                        isProjectReal = True
                        ListaProyectos.remove(item)
                        input(f"'{item}' eliminado exitosamente")
                        on = False
                
                if isProjectReal == False:
                    print()
                    print("[ERROR] El proyecto con el ID ingresado no existe")  
                    input("Ingrese enter para continuar...")
        
        
