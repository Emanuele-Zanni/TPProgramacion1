
#
#! Imports --------------------

from General.clearConsole import *
from Tareas.funciones import *
from Proyectos.funciones import *
from Integrantes.funciones import *
from Integrantes.menus import *
from Tareas.menus import *
from Proyectos.menus import *
from Integrantes.roles import*

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
#? ListaIntegrantes= [["id","nombre","rol","TareasAsignadas"]]
#? ListaRoles= [["id","rol"]]


#* Datos Mockeados
ListaProyectos = [[1, 'Proyecto 1', [], '1', '1', 'Activo?'],[2, 'Proyecto 2', [], '1', '1', 'Activo?'],[3, 'Proyecto 3', [], '1', '1', 'Activo?'],[4, 'Proyecto 4', [], '1', '1', 'Activo?']]
ListaTareas = []
ListaIntegrantes= []
ListaRoles=[]

# ListaProyectos = []
# ListaTareas = []
# ListaIntegrantes= []
# ListaRoles=[]

#! Main  ----------------------
while app:
    while mainMenuVar:
        clearConsole()
        print("[*Menu Principal*]")
        print("")
        print("1. Ver Proyectos")
        print("2. Ver Personal")
        print("3. Stats (WIP)")
        print("0. Cerrar Programa")
        Opcion=input("Selecione una opcion: ")
        if Opcion=="1": #* Ver Proyectos
            imprimirMenuProyectos(ListaProyectos)            
        elif Opcion=="2": #* Ver Personal
            imprimirMenuIntegrantes(ListaIntegrantes, ListaRoles)            
        elif Opcion=="3": #* Stats
            input("WIP...")
        
        elif Opcion=="0": #* Cerrar el programa
            app=False
            mainMenuVar=False

        else: 
            print("")
            input("[ERROR] Opcion invalida. Intente nuevamente.")