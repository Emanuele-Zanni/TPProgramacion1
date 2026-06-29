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

#! Variables Principales --------------------

app=True
mainMenu=True

# ListaProyectos = []
# ListaTareas = []
# ListaIntegrantes= []
# ListaRoles=[]

#? ListaProyectos = ["id","nombreProyecto","tareas","FechaIncio", "FechaFinal", "EstadoProyecto","integrantes","ownerId"]
#? ListaTareas = ["id","nombre","integranteAsignados","fechaInicio","FechaFinal","estadoTarea"]

#! ListaTareas Version 2.0
#! ListaTareas = ["id","titulo","descripcion","integranteAsignados","fechaInicio","FechaFinal","estadoTarea"]

#? ListaIntegrantes= [["id","nombre","rol","TareasAsignadas"]]
#? ListaRoles= [["id","rol"]]
#? ListaUsuarios = {
#?     "usuario": {
#?         "id": int,
#?         "password": str,
#?         "clearance": int,
#?         "projects": [
#?             {
#?                 "projectId": int,
#?                 "rol": str,
#?                 "tareas": [int]
#?             }
#?         ]
#?     }
#? }

#! ========================== Datos Mockeados para TESTING / DEMO del Proyecto ==========================

#* Listas Mock de Usuarios (para conversion Lista => Diccionario por consigna del CHECKLIST) -------
subHeaders = ["id","password","clearance","projects"]
listaIdsUsuarios = [1,2,3]
listaNombres = ["candela","emanuele","eze"]
listaContraseñas = ["1234","5555","123"]
listaNivelesAcceso = [3,3,3] #? 0 Invitado?, 1 Miembro, 2 Manager, 3 SuperAdmin
listaProyectosUsuario = [
    [{"projectId": 1, "rol": "Desarrollador", "tareas": [1, 2]}],
    [{"projectId": 1, "rol": "Desarrollador", "tareas": [3]}],
    [{"projectId": 2, "rol": "QA", "tareas": []}]
]

#* Menuda diccionario por comprension chaval
ListaUsuarios = {
    nombre: dict(zip(subHeaders, [id_usuario, contraseña, acceso, proyectos]))
    for id_usuario, nombre, contraseña, acceso, proyectos in zip(
        listaIdsUsuarios,
        listaNombres,
        listaContraseñas,
        listaNivelesAcceso,
        listaProyectosUsuario
    )
}
#* ----------------------------------------------------------------------------------------------------

#* Mock Proyectos --------
mockDate = datetime.now()
ListaProyectos = [[1, 'Proyecto 1', [
                        [1,"nombreTarea","descTarea",mockDate,mockDate,"activo",[]],
                        [2,"nombreTarea","descTarea",mockDate,mockDate,"activo",[]],
                        [3,"nombreTareaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","descTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTareadescTarea",mockDate,mockDate,"activo",[1,2,3]],
                ], mockDate, mockDate, 'Activo',[], 1],
                  [2, 'Proyecto 2', [], mockDate, mockDate, 'Activo',[], 3],
                  [3, 'Proyecto 3', [], mockDate, mockDate, 'Activo',[], None],
                  [4, 'Proyecto 444444444444444444444444444444444444444', [], mockDate, mockDate, 'Activo',[], None]]

#* Mock Tareas ---------------

ListaTareas = []


ListaRoles= [[1, "Desarrollador"],
            [2, "QA"]]

ListaStats= []


#! Main  ----------------------
while app:
    #? Comentar la variable "credencial" que no se quiera utilizar para elegir entre modo NORMAL / DEV
    #* MODO NORMAL
    # credencial = menuAcceso(ListaUsuarios,ListaRoles)
    #* MODO DEV
    credencial = {'user': 'ADMIN', 'clearance': 4}


    mainMenu = True
    while mainMenu:
        clearConsole()
        print("\033[33m[*Menu Principal*]\033[0m")
        print("")
        print("1. Proyectos")
        print("2. Personal")
        print("3. Stats")
        print("4. Cerrar sesiÃ³n")
        print("0. Cerrar Programa")
        print()
        Opcion=input("â€¢ Selecione una opcion: ")
        if Opcion=="1": #* Ver Proyectos
            imprimirMenuProyectos(ListaProyectos, ListaUsuarios, credencial)            
        elif Opcion=="2": #* Ver Personal
            imprimirMenuIntegrantes(ListaUsuarios, ListaRoles, credencial)
        elif Opcion=="3": #* Stats
            imprimirMenuStats(ListaProyectos, ListaUsuarios, ListaRoles)
        elif Opcion=="4":
            mainMenu = False
        elif Opcion=="0": #* Cerrar el programa
            app=False
            mainMenu=False
        else: 
            print("")
            input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
