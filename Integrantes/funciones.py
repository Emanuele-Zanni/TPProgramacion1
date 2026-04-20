from General.clearConsole import *


def ver_integrantes(ListaIntegrantes):
    clearConsole()
    print("[Menu Principal > Integrantes > *Ver Integrantes*]")
    print()
    if len(ListaIntegrantes) == 0:
        input("No hay integrantes registrados")
    elif len(ListaIntegrantes) > 0:
        for integrante in ListaIntegrantes:
            print(integrante)
        input("\nPresione cualquier tecla para continuar...")
    

#! TODO: COMPLETAR LOS PASOS RESTANTES & AGREGAR SUBMENU y CRUD para creacion y gestion de Roles
def agregar_integrante(ListaIntegrantes, ListaRoles):
    clearConsole()
    print("[Menu Principal > Integrantes > *Agregar Integrantes*]")
    print()
    
    if len(ListaIntegrantes)==0:
        id=1
    else: 
        id = ListaIntegrantes[len(ListaIntegrantes)-1][0]+1 
    
    inProgress=True
    p1,p2= True,False
    
    while p1:
        clearConsole()
        print("[Menu Principal > Integrantes > *Agregar Integrantes*]")
        print()
        nombre_integrante = input("• Ingrese el nombre del integrante: ")
        if nombre_integrante== "":
            print("")
            input("[ERROR] El nombre ingresado no puede estar vacio")
        elif nombre_integrante[0].strip().isdigit(): 
            print("")
            input("[ERROR] El nombre ingresado no puede empezar con un número")
        #! Hacer funcion auxiliar arriba de todo para hacer la comparacion, asignar el resultado a una variable y comparar esa varaible para
        #! ejecutar esto
        #* USAR LAMBDA ACA??????
        # elif nombre == otroNombrePreexistente:
        #     print("")
        #     input("[ERROR] El nombre ingresado ya esta siendo utilizado")
        else: 
            p1 = False
            p2 = True
    while p2 and inProgress:
        clearConsole()
        print("[Menu Principal > Integrantes > *Agregar Integrantes*]")
        print()
        print(f"Nombre del Integrante {nombre_integrante}")
        print("")
        if len (ListaRoles)==0:
            input("No hay roles existentes, por favor agregue un rol")
            return
        elif len(ListaRoles)>0:
            print(ListaRoles)
            rol = int(input("Asignele el id del rol al nuevo integrante: "))
            for i in range(len(ListaRoles)):
                if ListaRoles[i][0]==rol:
                    ListaRoles[i][2].append(nombre_integrante)

            nuevo_integrante = [id,nombre_integrante,rol]
            ListaIntegrantes.append(nuevo_integrante)
            
            p2 = False
            #! ESTO ESTA MAL, TIENE QUE SER AUTOMATICO CON LIBRERIA "date"
            registroFechaIntegrantes=input("Ingrese la fecha de hoy: ")
            print("")
            print("Nuevo integrante añadido con éxito ")
            print("ID:",nuevo_integrante[0])
            print("Nombre:",nuevo_integrante[1])
            print("Rol:",nuevo_integrante[2])
            input("Presione enter para continuar...")

def editar_integrante(ListaIntegrantes):
    clearConsole()
    print("[Menu Principal > Integrantes > *Editar Integrantes*]")
    print()
    
    if len(ListaIntegrantes)==0:
        input("No hay integrantes registrados")
    
    else:
        posicion = 0
        isMemberReal = False
        member_id = int(input("• Ingrese ID del integrante a editar: "))
        for item in ListaIntegrantes:
                if item[0] == member_id:
                    posicion = member_id - 1
                    isMemberReal = True
        if isMemberReal:
            print("1. Cambiar Nombre")
            print("2. Cambiar rol")
            print("")
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
    clearConsole()
    print("[Menu Principal > Integrantes > *Eliminar Integrante*]")
    print()
    if len(ListaIntegrantes) == 0:
        input("No hay integrantes registrados")
    else:
        idIngresado = input("Ingrese el ID del integrante a eliminar: ")
        isMemberReal = False
        for integrante in ListaIntegrantes:
            if integrante[0] == idIngresado:
                isMemberReal = True
        if isMemberReal:
            del ListaIntegrantes[idIngresado-1]
        else:
            print("El integrante con el ID ingresado no existe")    

    