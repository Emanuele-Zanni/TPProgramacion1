
#
#! Imports --------------------

from General.clearConsole import *
from Tareas.funciones import *
from Proyectos.funciones import *
from Integrantes.funciones import *
from Integrantes.menus import *
from Tareas.menus import *
from Proyectos.menus import *

"""Tareas (Crear tareas, eliminar tareas
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

#? ListaProyectos = ["id","nombreProyecto","tareas","FechaIncio", "FechaFinal", "EstadoProyecto"]
#? ListaTareas = ["id","nombre","integranteAsignados","fechaInicio","FechaFinal","estadoTarea"]
#? ListaIntegrantes= ["id","nombre","rol","TareasAsignadas"]

ListaProyectos = []
ListaTareas = []
ListaIntegrantes= []

    


#! Imprimir Menus --------------------
# def imprimirMenuIntegrantes():
#     print("1. Ver integrantes")
#     print("2. Agregar integrante")
#     print("3. Editar integrante")
#     print("4. Eliminar integrante")
#     opcion=input("Seleccione una opcion: ")
#     if opcion=="1":
#         ver_integrantes()
#     elif opcion=="2":
#         agregar_integrante()
#     elif opcion=="3":
#         editar_integrante()
#     elif opcion=="4":
#         eliminar_integrante()
#     else:
#         print("Opcion invalida. Intente nuevamente.")
   

    
#! CRUDs --------------------

#* ------------------------------------------ PROYECTOS -----------------------------------------------

# def ver_proyectos():
#     if len(ListaProyectos) == 0:
#         print("No hay proyectos registrados.")
#         return
#     elif len(ListaProyectos) > 0:
#         for proyecto in ListaProyectos:
#             print(proyecto)



# def crear_proyecto():
#     id = len(ListaProyectos) + 1
#     nombreProyecto=input("Ingrese el nombre del proyecto: ")
#     tareas = []
#     FechaInicio=input("Ingrese la fecha de inicio del proyecto: ")
#     FechaFinal=input("Ingrese la fecha de finalizacion del proyecto: ")
#     Estado=input("Ingrese el estado del proyecto: ")
#     #* Enum

#     nuevo_proyecto = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]
    
#     ListaProyectos.append(nuevo_proyecto)
    
#     #* ListaProyectos = [[id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]]

#     # return nuevo_proyecto

# def editar_proyecto():
#     #* Que proyecto? [POSICION]
#     posicion = 0
#     isProjectReal = False
#     project_id = int(input("Ingrese ID del proyecto a editar: "))
#     for item in ListaProyectos:
#             if item[0] == project_id:
#                 posicion = project_id - 1
#                 isProjectReal = True

#     if isProjectReal:
#         #* Menu con variables de ESE proyecto (1. Cambiar Nombre - 2. Cambiar fecha de inicio - 3. Cambiar fecha final - 4. Nuevo estado del proyecto)
#         print("1. Cambiar Nombre")
#         print("2. Cambiar fecha de inicio")
#         print("3. Cambiar fecha final")
#         print("4. Cambiaar el estado del proyecto")
#         opcion = input("Seleccione una opcion")
        
#         if opcion == "1":
#             editarNombre=input("Ingrese el nuevo nombre del proyecto: ")
#             ListaProyectos[posicion][1] = editarNombre
#         elif opcion == "2":
#             editarFechaInicio=input("Ingrese la nueva fecha de inicio: ")
#             ListaProyectos[posicion][3] = editarFechaInicio
#         elif opcion == "3":
#             editarFechaFinal=input("Ingrese la nueva fecha final: ")
#             ListaProyectos[posicion][4] = editarFechaFinal
#         elif opcion == "4": 
#             editarEstado=input("Ingrese el nuevo estado del proyecto: ")
#             ListaProyectos[posicion][5] = editarEstado
#         else:
#             print("Número inválido")

#         # proyecto_editado = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]

#     else:
#         print("El proyecto ingresado no existe")


# def eliminar_proyecto():
#     #* Aca falta agregar validacion de input NO numerico para que no rompa (y conversor de texto a num)
#     id = int(input("Ingrese el ID del proyecto a eliminar: "))
#     isProjectReal = False

#     for item in ListaProyectos:
#         if item[0] == id:
#             isProjectReal = True

#     if isProjectReal:
#         del ListaProyectos[id-1]
#         #* Aca falta funcion para reacomodar el ID de TODOS los elementos de la lista para que no haya saltos
#         #* (Es opcional esto) 
#     else:
#         print("El proyecto con el ID ingresado no existe")      


#! -------------------------------------------INTEGRANTES-----------------------------------------------

#!ListaIntegrantes= ["id","nombre","rol","TareasAsignadas"]

def ver_integrantes(ListaIntegrantes):
    if len(ListaIntegrantes) == 0:
        print("No hay integrantes registrados")
        return
    elif len(ListaIntegrantes) > 0:
        for integrante in ListaIntegrantes:
            print(integrante)

def agregar_integrante(ListaIntegrantes):
    id = len(ListaIntegrantes) + 1
    nombre_integrante = input("Ingrese el nombre del integrante")
    rol = input("Ingrese el rol")
    #! Tareas asignadas???

    nuevo_integrante = [id,nombre_integrante,rol]

    ListaIntegrantes.append(nuevo_integrante)

def editar_integrante(ListaIntegrantes):
    posicion = 0
    isMemberReal = False
    member_id = int(input("Ingrese ID de la tarea a editar: "))
    for item in ListaIntegrantes:
            if item[0] == member_id:
                posicion = member_id - 1
                isMemberReal = True

    if isMemberReal:
        print("1. Cambiar Nombre")
        print("2. Cambiar rol")
        opcion = input("Seleccione una opcion")
        
        if opcion == "1":
            editarNombre=input("Ingrese el nuevo nombre del proyecto: ")
            ListaIntegrantes[posicion][1] = editarNombre
        elif opcion == "2":
            editarRol=input("Ingrese la nueva fecha de inicio: ")
            ListaIntegrantes[posicion][2] = editarRol
        else:
            print("Número inválido")

        # tarea_editada = [id,nombreTarea,tareas,FechaInicio,FechaFinal,Estado]

    else:
        print("El integrante ingresado no existe")


def eliminar_integrante(ListaIntegrantes):
    id = int(input("Ingrese el ID del integrante a eliminar: "))
    isMemberReal = False

    for item in ListaIntegrantes:
        if item[0] == id:
            isMemberReal = True

    if isMemberReal:
        del ListaIntegrantes[id-1]


    else:
        print("El integrante con el ID ingresado no existe")    


#! Menu Principal --------------------
while app:
    while mainMenuVar:
        clearConsole()
        print("[Menu Principal]")
        print("")
        print("1. Proyectos")
        print("2. Tareas")
        print("3. Integrantes")
        Opcion=input("Selecione una opcion: ")
        if Opcion=="1": #Proyectos
            imprimirMenuProyectos(ListaProyectos)
            input("Ingrese una opcion para continuar...")
            
        elif Opcion=="2": #Tareas
            imprimirMenuTareas(ListaTareas)
            
        elif Opcion=="3": #Integrantes
            imprimirMenuIntegrantes(ListaIntegrantes)
            input("Ingrese una opcion para continuar...")

        else: 
            input("Opcion invalida. Intente nuevamente.")