
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

#! Main  ----------------------
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