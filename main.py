
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
from Stats.menu import*
from Stats.funciones import*


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
mainMenu=True

#? ListaProyectos = ["id","nombreProyecto","tareas","FechaIncio", "FechaFinal", "EstadoProyecto"]
#? ListaTareas = ["id","nombre","integranteAsignados","fechaInicio","FechaFinal","estadoTarea"]

#! ListaTareas Version 2.0
#! ListaTareas = ["id","titulo","descripcion","integranteAsignados","fechaInicio","FechaFinal","estadoTarea"]

#? ListaIntegrantes= [["id","nombre","rol","TareasAsignadas"]]
#? ListaRoles= [["id","rol"]]
#? ListaUsuarios= ["Usuario", "Contraseña"]

#* Datos Mockeados
subHeaders = ["password","clearance","rol","tareas"]
listaNombres = ["candela","emanuele","eze"]
listaContraseñas = ["1234","5555","123"]
listaNivelesAcceso = [3,3,3] #? 0 Invitado?, 1 Miembro, 2 Manager, 3 SuperAdmin
listaRolesUsuarios = ["Desarrollador","Desarrollador","QA"]
listaTareasAsignadas = [[],[],[]]

#* Menuda diccionario por comprension chaval
#* Explicacion de esta lista... (agregar)
ListaUsuarios = {
    nombre: dict(zip(subHeaders, [contraseña, acceso]))
    for nombre, contraseña, acceso in zip(listaNombres, listaContraseñas, listaNivelesAcceso)
}

for usuario, rol, tareas in zip(listaNombres, listaRolesUsuarios, listaTareasAsignadas):
    ListaUsuarios[usuario]["rol"] = rol
    ListaUsuarios[usuario]["tareas"] = tareas

date = datetime.now()

ListaProyectos = [[1, 'Proyecto 1', [], date, date, 'Activo'],
                  [2, 'Proyecto 2', [], date, date, 'Activo'],
                  [3, 'Proyecto 3', [], date, date, 'Activo'],
                  [4, 'Proyecto 4', [], date, date, 'Activo']]

#ListaTareas = []

# ListaIntegrantes= [[1,"Emanuele","Desarrollador",[]],
#                    [2,"Ezequiel","QA",[]],
#                    [3,"Rodolfo","QA",[]],
#                    [4,"Candela","Desarrollador",[]],
#                    [5,"Francisco","QA",[]]]

ListaRoles= [[1, "Desarrollador"],
            [2, "QA"]]

ListaStats= []


# ListaProyectos = []
# ListaTareas = []
# ListaIntegrantes= []
# ListaRoles=[]

#! Main  ----------------------
while app:
    #? Descomentar credencial hardcodeada y comentar credencial con "login()" para MODO DEV
    credencial = {'user': 'ADMIN', 'clearance': 2}
    # credencial = menuAcceso(ListaUsuarios,ListaRoles)

 
    mainMenu = True
    while mainMenu:
        clearConsole()
        print("\033[33m[*Menu Principal*]\033[0m")
        print("")
        print("1. Proyectos")
        print("2. Personal")
        print("3. Stats (WIP)")
        print("4. Cerrar sesión")
        print("0. Cerrar Programa")
        Opcion=input("Selecione una opcion: ")
        if Opcion=="1": #* Ver Proyectos
            imprimirMenuProyectos(ListaProyectos, credencial)            
        elif Opcion=="2": #* Ver Personal
            imprimirMenuIntegrantes(ListaUsuarios, ListaRoles, credencial)
        elif Opcion=="3": #* Stats
            imprimirMenuStats(ListaProyectos, ListaIntegrantes, ListaRoles)
        elif Opcion=="4":
            mainMenu = False
        elif Opcion=="0": #* Cerrar el programa
            app=False
            mainMenu=False
        else: 
            print("")
            input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
