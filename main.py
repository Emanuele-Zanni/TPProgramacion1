
#
#! Imports --------------------

from General.clearConsole import *
from Tareas.funciones import *
from Proyectos.funciones import *
from Integrantes.funciones import *
from Integrantes.menus import *
from Integrantes.roles import *
from Tareas.menus import *
from Proyectos.menus import *
from Integrantes.roles import*
from Database.usuarios import*

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
#? ListaUsuarios= ["Usuario", "Contraseña"]


#* Datos Mockeados
ListaProyectos = [[1, 'Proyecto 1', [], '1', '15', 'Activo'],
                  [2, 'Proyecto 2', [], '1', '20', 'Activo'],
                  [3, 'Proyecto 3', [], '1', '1', 'Activo'],
                  [4, 'Proyecto 4', [], '1', '13', 'Activo']]

#ListaTareas = []

ListaIntegrantes= [[1,"Emanuele","Desarrollador",[]],
                   [2,"Ezequiel","QA",[]],
                   [3,"Rodolfo","QA",[]],
                   [4,"Candela","Desarrollador",[]],
                   [5,"Francisco","QA",[]]]

ListaRoles= [[1, "Desarrollador"],
            [2, "QA"]]

# ListaProyectos = []
# ListaTareas = []
# ListaIntegrantes= []
# ListaRoles=[]

#! Main  ----------------------
while app:
    basico= login()
    clearConsole()
    while mainMenuVar:
        clearConsole()
        print("[*Menu Principal*]")
        print("")
        print("1. Proyectos")
        print("2. Personal")
        print("3. Stats (WIP)")
        print("4. Cerrar sesión")
        print("0. Cerrar Programa")
        Opcion=input("Selecione una opcion: ")
        if Opcion=="1": #* Ver Proyectos
            imprimirMenuProyectos(ListaProyectos, basico)            
        elif Opcion=="2": #* Ver Personal
            imprimirMenuIntegrantes(ListaIntegrantes, ListaRoles, basico)            
        elif Opcion=="3": #* Stats
            input("WIP...")
        elif Opcion=="0": #* Cerrar el programa
            app=False
            mainMenuVar=False
        elif Opcion=="4":
            clearConsole()
            basico= login()

        else: 
            print("")
            input("[ERROR] Opcion invalida. Intente nuevamente.")