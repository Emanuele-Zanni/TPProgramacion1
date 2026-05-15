from General.clearConsole import *
from General.inputFecha import *
from Tareas.menus import *
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


def seleccionar_proyecto(ListaProyectos):
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
                id = input("ingrese el ID del proyecto a seleccionar \ningrese 0 para cancelar: ")
                if id.isdigit():
                    if id == "0":
                        inProgress = False
                        print()
                        print("Operacion cancelada")
                        input("Ingrese enter para continuar...")
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
                    print("[ERROR] El id no puede estar vacio")
                    input("Ingrese enter para continuar...")

                else:
                    print("")
                    print("[ERROR] El ID ingresado debe ser un numero")
                    input("Ingrese enter para continuar...")
                        
            if isProjectReal:
                on = True
                while on:
                    clearConsole()
                    print("[Menu principal > Proyectos > *Proyecto Seleccionado*]")
                    print() 
                    print(f"=== {proyecto[1]} ===")
                    print(f"ID: {proyecto[0]} | Status: {proyecto[5]} | Fecha Inicio/Final: {proyecto[3]} - {proyecto[4]}")
                    print("")

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
        nombreProyecto=input("• Ingrese el nombre del proyecto\n• Ingrese 0 para cancelar: ")  
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
        elif FechaInicio.isdigit() == False:
            print("")
            input("[ERROR] La fecha ingresada debe ser un numero") 
        elif FechaInicio == "0":
            inProgress = False
            print()
            print("Operacion cancelada")
            input("Ingrese enter para continuar...")
        else:
            p2 = False
            p3 = True
    
    while p3 and inProgress:
        clearConsole()
        print("[Menu Principal > Proyectos > *Crear Proyectos*]")
        print()
        print(f"Nombre del Proyecto: {nombreProyecto}")
        print(f"Fecha de Inicio: {FechaInicio}")
        FechaFinal=inputFecha(nombreProyecto,"Final")
        if FechaFinal == "":
            print("")
            input("[ERROR] La fecha ingresada no puede estar vacia") 
        elif FechaFinal.isdigit() == False:
            print("")
            input("[ERROR] La fecha ingresada debe ser un numero") 
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
    clearConsole()
    print("[Menu principal > Proyectos > *Editar Proyectos*]")
    print()

    if len(ListaProyectos) == 0:
        input("No hay proyectos registrados.")
    else:
        #* Que proyecto? [POSICION]
        isProjectReal = False
        mostrarListaProyectos(ListaProyectos)
        print()
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
        
        