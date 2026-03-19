from utils.clearConsole import *

""""Tareas (Crear tareas, eliminar tareas
asignar tareas, actualizar su estado (pendiente
en progreso, completada), registrar nuevas tareas)

Integrante (Búsqueda por integrante para ver las tareas
asignadas, estasdísticas de la cantidad de proyectos activos
porcentaje de tareas completadas, promedio de tareas por integrante)

Proyecto ()
"""
#! Variables --------------------

app=True
mainMenuVar=True

# ListaProyectos = ["id","nombreProyecto","tareas","FechaIncio", "FechaFinal", "EstadoProyecto"]
# ListaTareas = ["id","nombre","integranteAsignados","fechaInicio","FechaFinal","estadoTarea"]
# ListaIntegrantes= ["id","nombre","rol","TareasAsignadas"]

ListaProyectos = []
ListaTareas = []
ListaIntegrantes= []

    


#! Imprimir Menus --------------------
def imprimirMenuProyectos():
    clearConsole()
    print("1. Ver proyectos")
    print("2. Crear Proyecto")
    print("3. Editar Proyecto")
    print("4. Eliminar Proyecto")
    opcion=input("Seleccione una opcion: ")
    if opcion=="1":
        ver_proyectos()
    elif opcion=="2":
        crear_proyecto()
    elif opcion=="3":
        editar_proyecto()
    elif opcion=="4":
        eliminar_proyecto()
    else:
        print("Opcion invalida. Intente nuevamente.")

def imprimirMenuTareas():
    clearConsole()
    print("1. Ver tarea")
    print("2. Crear tarea")
    print("3. Editar tarea")
    print("4. Eliminar tarea")
    opcion=input("Seleccione una opcion: ")
    if opcion=="1":
        ver_tareas()
    elif opcion=="2":
        crear_tarea()
    elif opcion=="3":
        editar_tarea()
    elif opcion=="4":
        eliminar_tarea()
    else:
        print("Opcion invalida. Intente nuevamente.")
   


def imprimirMenuIntegrantes():
    clearConsole()
    print("1. Ver integrantes")
    print("2. Agregar integrante")
    print("3. Editar integrante")
    print("4. Eliminar integrante")
    opcion=input("Seleccione una opcion: ")
    if opcion=="1":
        ver_integrantes()
    elif opcion=="2":
        agregar_integrante()
    elif opcion=="3":
        editar_integrante()
    elif opcion=="4":
        eliminar_integrante()
    else:
        print("Opcion invalida. Intente nuevamente.")
   

    
#! CRUDs --------------------

def ver_proyectos():
    if len(ListaProyectos) == 0:
        print("No hay proyectos registrados.")
        return
    elif len(ListaProyectos) > 0:
        for proyecto in ListaProyectos:
            print(proyecto)



def crear_proyecto():
    id = len(ListaProyectos) + 1
    nombreProyecto=input("Ingrese el nombre del proyecto: ")
    Tareas = []
    FechaInicio=input("Ingrese la fecha de inicio del proyecto: ")
    FechaFinal=input("Ingrese la fecha de finalizacion del proyecto: ")
    Estado=input("Ingrese el estado del proyecto: ")
    #* Enum

    nuevo_proyecto = [id,nombreProyecto,Tareas,FechaInicio,FechaFinal,Estado]
    
    ListaProyectos.append(nuevo_proyecto)
    
    #* ListaProyectos = [[id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]]

    # return nuevo_proyecto

def editar_proyecto():
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
        print("4. Cambiaar el estado del proyecto")
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


def eliminar_proyecto():
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

# funciones de tareas

def ver_tareas():
    if len(ListaTareas) == 0:
         print("No hay tareas registradas.")
        
    elif len(ListaTareas) > 0:
        for tarea in ListaTareas:
            print(tarea)

def crear_tarea():
    id = len(ListaTareas) + 1
    nombreTarea=input("Ingrese el nombre de la tarea: ")
    FechaInicio=input("Ingrese la fecha de inicio de la tarea: ")
    FechaFinal=input("Ingrese la fecha de finalizacion de la tarea: ")
    Estado=input("Ingrese el estado de la tarea: ")
    #* Enum

    nueva_tarea = [id,nombreTarea,FechaInicio,FechaFinal,Estado]
    
    ListaTareas.append(nueva_tarea)
   
def editar_tarea():
    posicion = 0
    isTareaReal = False
    tarea_id = int(input("Ingrese ID de la tarea a editar: "))
    for item in ListaTareas:
            if item[0] == tarea_id:
                posicion = tarea_id - 1
                isTareaReal = True

    if isTareaReal:
        print("1. Cambiar nombre")
        print("2. Cambiar fecha de inicio")
        print("3. Cambiar fecha final")
        print("4. Cambiar estado")
        Opcion = input("ingrese la opcion que desea editar: ")

        if Opcion == "1":
            editarNombre=input("ingrese el nuevo nombre de la tarea: ")
            ListaTareas[posicion][1] = editarNombre
        elif Opcion == "2":
            editarFechaInicio=input("ingrese la nueva fecha de inicio: ")
            ListaTareas[posicion][2] = editarFechaInicio
        elif Opcion == "3":
            editarFechaFinal=input("ingrese la nueva fecha final: ")
            ListaTareas[posicion][3] = editarFechaFinal
        elif Opcion == "4":
            editarEstado=input("igrese el nuevo estado de la tarea: ")
            ListaTareas[posicion][4] = editarEstado
        else:
            print("opcion invalida")
    else:
        print("la tarea ingresada no existe")

def eliminar_tarea():
    #* Aca falta agregar validacion de input NO numerico para que no rompa (y conversor de texto a num)
    id = int(input("Ingrese el ID de la tarea a eliminar: "))
    isTareaReal = False

    for item in ListaTareas:
        if item[0] == id:
            isTareaReal = True
    if isTareaReal:
        del ListaTareas[id-1]
        #* Aca falta funcion para reacomodar el ID de TODOS los elementos de la lista para que no haya saltos
        #* (Es opcional esto) 
    else:
        print("La tarea con el ID ingresado no existe")

#funciones de integrantes

def ver_integrantes():
    if len(ListaIntegrantes) == 0:
        print("No hay integrantes registrados.")
        return
    elif len(ListaIntegrantes) > 0:
        for integrante in ListaIntegrantes:
            print(integrante)



def agregar_integrante():
    id = len(ListaIntegrantes) + 1
    nombre=input("Ingrese el nombre del integrante: ")
    tareaAsignada=input("Ingrese la tarea asignada al integrante: ")
    rol=input("Ingrese el rol del integrante: ")

    nuevo_integrante = [id,nombre,tareaAsignada,rol]

    ListaIntegrantes.append(nuevo_integrante)
    Estado=input("Ingrese el estado del proyecto: ")
    #* Enum

    nuevo_proyecto = [id,ListaIntegrantes,tareaAsignada,Estado]
    
    ListaProyectos.append(nuevo_proyecto)
    
    #* ListaProyectos = [[id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]]

    # return nuevo_proyecto

def editar_integrante():
    #* Que integrante? [POSICION]
    posicion = 0
    isIntegranteReal = False
    integrante_id = int(input("Ingrese ID del integrante a editar: "))
    for item in ListaIntegrantes:
            if item[0] == integrante_id:
                posicion = integrante_id - 1
                isIntegranteReal = True

    if isIntegranteReal:
        #* Menu con variables de ESE integrante (1. Cambiar Nombre - 2. Cambiar fecha de inicio - 3. Cambiar fecha final - 4. Nuevo estado del integrante)
        print("1. Cambiar Nombre")
        print("2. Tarea asignada")
        print("3. Rol")
        
        opcion = input("Seleccione una opcion")
        
        if opcion == "1":
            editarNombre=input("Ingrese el nuevo nombre del proyecto: ")
            ListaProyectos[posicion][1] = editarNombre
        elif opcion == "2":
            tareaAsignada=input("Ingrese la nueva tarea asignada: ")
            ListaProyectos[posicion][2] = tareaAsignada
        elif opcion == "3":
            rol=input("Ingrese el nuevo rol: ")
            ListaProyectos[posicion][3] = rol
       
        else:
            print("Número inválido")

        # proyecto_editado = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]

    else:
        print("El intagrante ingresado no existe")


def eliminar_integrante():
    #* Aca falta agregar validacion de input NO numerico para que no rompa (y conversor de texto a num)
    id = int(input("Ingrese el ID del integrante a eliminar: "))
    isIntegranteReal = False

    for item in ListaIntegrantes:
        if item[0] == id:
            isIntegranteReal = True
    if isIntegranteReal:
        del ListaIntegrantes[id-1]
        #* Aca falta funcion para reacomodar el ID de TODOS los elementos de la lista para que no haya saltos
        #* (Es opcional esto) 
    else:
        print("El integrante con el ID ingresado no existe")    


#! Menu Principal --------------------
while app:
    while mainMenuVar:
        clearConsole()
        print("Menu Principal: ")
        print("1. Proyectos")
        print("2. Tareas")
        print("3. Integrantes")
        Opcion=input("Selecione una opcion: ")
        if Opcion=="1": #Proyectos
            imprimirMenuProyectos()
            input("Ingrese una opcion para continuar...")
            
        elif Opcion=="2": #Tareas
            imprimirMenuTareas()
            input("Ingrese una opcion para continuar...")
        elif Opcion=="3": #Integrantes
            imprimirMenuIntegrantes()
            input("Ingrese una opcion para continuar...")2
            
        else: 
            print("Opcion invalida. Intente nuevamente.")