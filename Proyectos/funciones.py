from General.clearConsole import *
from General.inputFecha import *
from Tareas.funciones import *
from General.formato import imprimir_tabla, imprimir_titulo
# from Proyectos.menus import imprimirMenuSeleccionarProyecto

def mostrarListaProyectos(ListaProyectos):
    imprimir_titulo("Lista de Proyectos")
    columnas = [
        {"titulo": "ID", "min": 4, "peso": 1},
        {"titulo": "Nombre", "min": 18, "peso": 4},
        {"titulo": "Tareas", "min": 8, "peso": 1},
        {"titulo": "Inicio", "min": 12, "peso": 2},
        {"titulo": "Fin", "min": 12, "peso": 2},
        {"titulo": "Estado", "min": 10, "peso": 2},
    ]
    filas = []
    for proyecto in ListaProyectos:
        id_ = proyecto[0]
        nombre = proyecto[1]
        tareas = len(proyecto[2])
        inicio = proyecto[3]
        fin = proyecto[4]
        estado = proyecto[5]
        filas.append([
            id_,
            nombre,
            tareas,
            inicio.strftime('%d/%m/%Y'),
            fin.strftime('%d/%m/%Y'),
            estado,
        ])
    imprimir_tabla(columnas, filas)
    

def ver_proyectos(ListaProyectos):
    clearConsole()
    print("\033[33m[Menu Principal > Proyectos > *Ver Proyectos*]\033[0m")
    print()       
    
    if len(ListaProyectos) == 0:
        input("No hay proyectos registrados.")
    elif len(ListaProyectos) > 0:
        mostrarListaProyectos(ListaProyectos)
        input("Ingrese cualquier opcion para continuar...")


def obtener_id_usuario_desde_credencial(ListaUsuarios, credencial):
    usuario_credencial = credencial.get("user")

    for nombre_usuario, datos_usuario in ListaUsuarios.items():
        if nombre_usuario == usuario_credencial:
            return datos_usuario.get("id")

    return None


def obtener_managers_disponibles(ListaUsuarios, owner_id_actual):
    managers = []

    for nombre_usuario, datos_usuario in ListaUsuarios.items():
        usuario_id = datos_usuario.get("id")
        if datos_usuario.get("clearance") == 2 and usuario_id != owner_id_actual:
            managers.append((nombre_usuario, datos_usuario))

    return managers


def entregar_ownership_proyecto(proyecto, ListaUsuarios):
    owner_id_actual = proyecto[7] if len(proyecto) > 7 else None
    managers_disponibles = obtener_managers_disponibles(ListaUsuarios, owner_id_actual)

    if len(managers_disponibles) == 0:
        print()
        input("No hay managers disponibles")
        return

    clearConsole()
    print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > Editar *Proyectos(Ownership)*]\033[0m")
    print()
    mostrar_tarea_proyecto("proyecto", proyecto)
    imprimir_tabla(
        [
            {"titulo": "ID", "min": 4, "peso": 1},
            {"titulo": "Usuario", "min": 18, "peso": 3},
        ],
        [[datos_usuario.get("id", ""), nombre_usuario.capitalize()] for nombre_usuario, datos_usuario in managers_disponibles]
    )

    nuevo_owner_id = input("â€¢ Ingrese el ID del manager que recibira el ownership (0 para cancelar): ")
    if nuevo_owner_id == "0":
        print()
        input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
        return
    if nuevo_owner_id == "":
        print()
        input("\033[31m[ERROR] El id no puede estar vacio.\033[0m")
        return
    if nuevo_owner_id.isdigit() == False:
        print()
        input("\033[31m[ERROR] El id debe ser un numero.\033[0m")
        return

    nuevo_owner_id = int(nuevo_owner_id)
    nuevo_owner_usuario = None
    for nombre_usuario, datos_usuario in managers_disponibles:
        if datos_usuario.get("id") == nuevo_owner_id:
            nuevo_owner_usuario = (nombre_usuario, datos_usuario)
            break

    if nuevo_owner_usuario is None:
        print()
        input("\033[31m[ERROR] El manager con ese ID no existe.\033[0m")
        return

    proyecto[7] = nuevo_owner_id
    if nuevo_owner_id not in proyecto[6]:
        proyecto[6].append(nuevo_owner_id)

    for _, datos_usuario in ListaUsuarios.items():
        for proyecto_usuario in datos_usuario.get("projects", []):
            if proyecto_usuario.get("projectId") == proyecto[0] and proyecto_usuario.get("rol") == "Owner":
                proyecto_usuario["rol"] = "Sin rol"

    proyectos_usuario_owner = nuevo_owner_usuario[1].setdefault("projects", [])
    registro_owner = None
    for proyecto_usuario in proyectos_usuario_owner:
        if proyecto_usuario.get("projectId") == proyecto[0]:
            registro_owner = proyecto_usuario
            break

    if registro_owner is None:
        proyectos_usuario_owner.append({
            "projectId": proyecto[0],
            "rol": "Owner",
            "tareas": []
        })
    else:
        registro_owner["rol"] = "Owner"

    print()
    input("\033[92m[EXITO] Ownership transferido correctamente.\033[0m")


def seleccionar_proyecto(ListaProyectos, ListaUsuarios, credencial):
        isProjectReal = False
        p1 = True
        inProgress = True


        if len(ListaProyectos) == 0:
            clearConsole()
            print("\033[33m[Menu principal > Proyectos > *Seleccionar Proyectos*]\033[0m")
            print()
            input("No hay proyectos registrados.")
        else:
            while p1 and inProgress:
                clearConsole()
                print("\033[33m[Menu principal > Proyectos > *Seleccionar Proyectos*]\033[0m")
                # print()
                mostrarListaProyectos(ListaProyectos)
                id = input("• Ingrese el ID del proyecto a seleccionar (0 para volver): ")
                if id.isdigit():
                    if id == "0":
                        inProgress = False
                        print()
                        # input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
                    else:    
                        id = int(id)
                        for project in ListaProyectos:
                            if project[0] == id:   
                                isProjectReal = True
                                proyecto = project
                                p1 = False
                        if not isProjectReal:
                            print()
                            input("\033[31m[ERROR] El ID ingresado no pertenece a ningun proyecto.\033[0m")
               
                elif id == "":
                    print("")
                    input("\033[31m[ERROR] El id no puede estar vacio.\033[0m")

                else:
                    print("")
                    input("\033[31m[ERROR] El ID ingresado debe ser un numero.\033[0m")
                        
            if isProjectReal:
                on = True
                while on:
                    clearConsole()
                    print("\033[33m[Menu principal > Proyectos > Seleccionar Proyectos > *Proyecto Seleccionado*]\033[0m")
                    # print() 
                    #! nombre poco autodescriptivo
                    mostrar_tarea_proyecto("proyecto", proyecto)

                    if credencial["clearance"] == 1:
                        print("1. Ver tarea")
                        print("?. Seleccionar tarea (WIP)")
                        print("0. Volver atras")
                        print()
                        opcion=input("• Seleccione una opcion: ")
                        if opcion=="1":
                            ver_tareas(proyecto[2], proyecto, ListaUsuarios, credencial)
                        elif opcion=="0":
                            on=False
                        else:
                            input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
                    # elif credencial["clearance"] > 1:
                    #     print("1. Ver tarea")
                    #     print("?. Seleccionar tarea (WIP)")
                    #     print("0. Volver atras")
                    #     print()
                    #     opcion=input("• Seleccione una opcion: ")
                    #     if opcion=="1":
                    #         ver_tareas(proyecto[2])
                    #     elif opcion=="0":
                    #         on=False
                    #     else:
                    #         input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
                    else:
                        print("1. Ver tareas")
                        print("2. Crear tarea")
                        print("3. Editar tarea")
                        print("4. Eliminar tarea")
                        print("5. Asignar tareas")
                        print("6. Gestionar integrantes del proyecto")
                        print("0. Volver atras")
                        print()
                        opcion=input("• Seleccione una opcion: ")
                        if opcion=="1":
                            ver_tareas(proyecto[2], proyecto, ListaUsuarios, credencial)
                        elif opcion=="2":
                            crear_tarea(proyecto[2])
                        elif opcion=="3":
                            editar_tarea(proyecto[2])
                        elif opcion=="4":
                            eliminar_tarea(proyecto[2])
                        elif opcion=="5":
                            asignar_tarea_integrante(proyecto[2], proyecto, ListaUsuarios)
                        elif opcion=="6":
                            gestionar_integrantes_proyecto(proyecto, ListaUsuarios)
                        elif opcion=="0":
                            on=False
                        else:
                            input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
    

def crear_proyecto(ListaProyectos, ListaUsuarios, credencial):
    clearConsole()
    print("\033[33m[Menu Principal > Proyectos > *Crear Proyectos*]\033[0m")
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
        print("\033[33m[Menu Principal > Proyectos > *Crear Proyectos*]\033[0m")
        print()
        nombreProyecto=input("• Ingrese el nombre del proyecto (0 para cancelar): ")  
        if nombreProyecto == "":
            print("")
            input("\033[31m[ERROR] El nombre ingresado no puede estar vacio.\033[0m") 
        elif nombreProyecto == "0":
            inProgress = False
            print()
            input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
        else:
            p1 = False
            p2 = True

    while p2 and inProgress: 
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > *Crear Proyectos*]\033[0m")
        print()
        print(f"Nombre del Proyecto: {nombreProyecto}")
        FechaInicio=inputFecha("Inicio")
        if FechaInicio == "":
            print("")
            input("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m") 
        elif FechaInicio == "0":
            inProgress = False
            print()
            input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
        elif FechaInicio == None:
            print("")
            input("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
        else:
            p2 = False
            p3 = True
    
    while p3 and inProgress:
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > *Crear Proyectos*]\033[0m")
        print()
        print(f"Nombre del Proyecto: {nombreProyecto}")
        print(f"Fecha de Inicio: {FechaInicio.strftime('%d/%m/%Y')}")
        FechaFinal=inputFecha("Final")
        if FechaFinal == None:
            print("")
            input("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
        elif FechaFinal < FechaInicio:
            print("")
            input("\033[31m[ERROR] La fecha final no puede ser anterior a la fecha de inicio.\033[0m")
        elif FechaFinal == "0":
            inProgress = False
            print()
            input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
        else:
            Estado = "Activo"
            p3 = False

    if inProgress:

        owner_id = obtener_id_usuario_desde_credencial(ListaUsuarios, credencial)
        integrantes = []
        if owner_id is not None:
            integrantes.append(owner_id)

        #? Type Proyecto = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado,integrantes,ownerId]
        nuevo_proyecto = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado,integrantes,owner_id]
        
        ListaProyectos.append(nuevo_proyecto)
        if owner_id is not None:
            for datos_usuario in ListaUsuarios.values():
                if datos_usuario.get("id") == owner_id:
                    datos_usuario.setdefault("projects", []).append({
                        "projectId": id,
                        "rol": "Owner",
                        "tareas": []
                    })
                    break
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > *Crear Proyectos*]\033[0m")
        print()
        print(f"ID: {id}")
        print(f"Nombre del Proyecto: {nombreProyecto}")
        print(f"Fecha de Inicio: {FechaInicio.strftime('%d/%m/%Y')}")
        print(f"Fecha de Finalizacion: {FechaFinal.strftime('%d/%m/%Y')}")
        print()
        input("\033[92m[EXITO] Proyecto creado correctamente.\033[0m")
        gestionar_integrantes_proyecto(nuevo_proyecto, ListaUsuarios)

#no basico
def editar_proyecto(ListaProyectos, ListaUsuarios, credencial):
    on = True
    
    if len(ListaProyectos) == 0:
        clearConsole()
        print("\033[33m[Menu Proyectos > *Editar Proyectos*]\033[0m")
        print()
        input("No hay proyectos registrados.")
    else:
        while on:   
            p1 = True
            p2 = False
            clearConsole()
            print("\033[33m[Menu Proyectos > *Editar Proyectos*]\033[0m")
            print()
            mostrarListaProyectos(ListaProyectos)
            #* Que_proyecto? [POSICION]
            posicion = 0
            isProjectReal = False
            project_id = input("• Ingrese ID del proyecto a editar (0 para vover cancelar): ")
            if project_id == "":
                print()
                input("\033[31m[ERROR] El id no puede estar vacio.\033[0m")
            elif project_id.isdigit() == False:
                print()
                input("\033[31m[ERROR] El id debe ser un numero.\033[0m")
            elif project_id == "0":
                on = False
                # print()
                # input("Volviendo al menu...")
                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
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
                    print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos*]\033[0m")
                    print()
                    mostrar_tarea_proyecto("proyecto", ListaProyectos[posicion])
                    print("1. Cambiar Nombre")
                    print("2. Cambiar fecha de inicio")
                    print("3. Cambiar fecha final")
                    print("4. Cambiar el estado del proyecto")
                    if credencial["clearance"] >= 2:
                        print("5. Entregar Ownership")
                    print("0. Volver")
                    print("")
                    opcion = input("• Seleccione una opcion:")
                    p4 = True

                    if opcion == "1":
                        while p4:    
                            clearConsole()
                            print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos(Nombre)*]\033[0m")
                            print()
                            mostrar_tarea_proyecto("proyecto", ListaProyectos[posicion])
                            editarNombre=input("• Ingrese el nuevo nombre del proyecto (0 para cancelar): ")
                            if editarNombre == "":
                                print("")
                                input("\033[31m[ERROR] El nombre ingresado no puede estar vacio.\033[0m")
                            elif editarNombre == "0":
                                p4 = False
                                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
                            else:
                                p4 = False   
                                p1 = False
                                p2 = True
                    
                    elif opcion == "2":
                        while p4:  
                            clearConsole()
                            print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos(Fecha de Inicio)*]\033[0m")
                            print()
                            mostrar_tarea_proyecto("proyecto", ListaProyectos[posicion])
                            editarFechaInicio=inputFecha("Inicio")
                            if editarFechaInicio == "":
                                print("")
                                input("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m")
                            elif editarFechaInicio == None:
                                print("")
                                input("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
                            elif editarFechaInicio == "0":
                                p4 = False
                                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
                            elif editarFechaInicio > editarFechaFinal:
                                print("")
                                input("\033[31m[ERROR] La fecha de inicio no puede ser posterior a la fecha final.\033[0m")
                            else:
                                p4 = False   
                                p1 = False
                                p2 = True
                            
                    elif opcion == "3":
                        while p4:   
                            clearConsole()
                            print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos(Fecha Final)*]\033[0m")
                            print()
                            mostrar_tarea_proyecto("proyecto", ListaProyectos[posicion])
                            editarFechaFinal=inputFecha("Final")
                            if editarFechaFinal == "":
                                print("")
                                input("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m")
                            elif editarFechaFinal == "0":
                                p4 = False
                                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
                            elif editarFechaFinal == None:
                                print("")
                                input("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
                            elif editarFechaFinal < editarFechaInicio:
                                print("")
                                input("\033[31m[ERROR] La fecha final no puede ser anterior a la fecha de inicio.\033[0m")
                            else:
                                p4 = False   
                                p1 = False
                                p2 = True
                    
                    elif opcion == "4": 
                        clearConsole()
                        while p4:
                            clearConsole()
                            print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos(Estado)*]\033[0m")
                            print()
                            mostrar_tarea_proyecto("proyecto", ListaProyectos[posicion])
                            print("1. Activo")
                            print("2. Completado")
                            print("3. Expirado")
                            print("0. Volver")
                            editarEstado=input("Ingrese el nuevo estado del proyecto(0 para cancelar): ")
                            ListaProyectos[posicion][4] = editarEstado
                            if editarEstado == "1":
                                editarEstado = "Activo"
                                ListaProyectos[posicion][4] = editarEstado
                                p4 = False
                                p1 = False
                                p2 = True
                            elif editarEstado == "2":
                                editarEstado = "Completado"
                                ListaProyectos[posicion][4] = editarEstado
                                p4 = False
                                p1 = False
                                p2 = True
                            elif editarEstado == "3":
                                editarEstado = "Expirado"
                                ListaProyectos[posicion][4] = editarEstado
                                p4 = False
                                p1 = False
                                p2 = True
                            elif opcion == "":
                                print("Opcion invalida. Intente nuevamente.")
                                input("Ingrese cualquier opcion para continuar...")
                            elif editarEstado == "0":
                                p4 = False
                                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
                            else:
                                print("Opcion invalida. Intente nuevamente.")
                                input("Ingrese cualquier opcion para continuar...")
                    elif opcion == "5" and credencial["clearance"] >= 2:
                        entregar_ownership_proyecto(ListaProyectos[posicion], ListaUsuarios)
                    elif opcion == "0":
                        p1 = False
                        input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
                    else:
                        input("\033[31m[ERROR] Número inválido.\033[0m")

                    proyecto_editado = [
                        id,
                        editarNombre,
                        ListaProyectos[posicion][2],
                        editarFechaInicio,
                        editarFechaFinal,
                        editarEstado,
                        ListaProyectos[posicion][6],
                        ListaProyectos[posicion][7]
                    ]

                while p2 and isProjectReal:
                    clearConsole()
                    print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Proyectos*]\033[0m")
                    print()
                    print(f"Nombre del proyecto: {editarNombre}")
                    print(f"Fecha de Inicio: {editarFechaInicio.strftime('%d/%m/%Y')}")
                    print(f"Fecha Final: {editarFechaFinal.strftime('%d/%m/%Y')}")
                    print(f"Estado: {editarEstado}")
                    print()
                    opcion = input("¿Desea guardar los cambios? (1 = Si | 0 = No): ")
                    if opcion == "1":
                        ListaProyectos[posicion] = proyecto_editado
                        print()
                        input("[EXITO] Proyecto editado correctamente.")
                        p2 = False
                        
                    elif opcion == "0":
                        print()
                        input("\033[93m[CANCELADO] No se realizaron cambios.\033[0m")
                        p2 = False

                    elif opcion == "":
                        print("opcion invalida")
                        input("ingrese cualquier opcion para continuar: ")    
                    else:
                        print("opcion invalida")
                        input("ingrese cualquier opcion para continuar: ")  

            else:
                input("\033[31m[ERROR] El proyecto ingresado no existe.\033[0m")
   
                                                               
#no basico
def eliminar_proyecto(ListaProyectos):
    on = True
    while on:    
        clearConsole()
        print("\033[33m[Menu principal > Proyectos > *Eliminar Proyectos*]\033[0m")
        print()
        if len(ListaProyectos) == 0:
            input("No hay proyectos registrados.")
        else:
            #* Aca falta agregar validacion de input NO numerico para que no rompa (y conversor de texto a num)
            id = input("• Ingrese el ID del proyecto a eliminar (0 para cancelar): ")
            isProjectReal = False

            if id == "":
                print()
                input("\033[31m[ERROR] El id no puede estar vacio.\033[0m")
            elif id == "0":
                on = False
                print()
                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
            else:
                id = int(id)
                for item in ListaProyectos:
                    if item[0] == id:
                        isProjectReal = True
                        p1 = True
                        while p1: 
                            clearConsole()
                            print("\033[33m[Menu principal > Proyectos > *Eliminar Proyectos*]\033[0m")
                            print()  
                            mostrar_tarea_proyecto("proyecto", item)
                            print()
                            opcion = input("¿Desea eliminar este proyecto? (1 = Si | 0 = No): ")
                            if opcion == "1":
                                ListaProyectos.remove(item)
                                input(f"[EXITO] '{item}' eliminado exitosamente")
                                p1 = False
                                on = False
                            elif opcion == "0":
                                p1 = False
                                on = False
                                print()
                                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
                            else:
                                print()
                                input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")

                if isProjectReal == False:
                    print()
                    input("\033[31m[ERROR] El proyecto con el ID ingresado no existe.\033[0m")

def mostrarListaIntegrantesProyecto(ListaUsuarios, proyecto):
    integrantes_proyecto = proyecto[6] if len(proyecto) > 6 else []
    filas = []
    for nombre_usuario, datos_usuario in ListaUsuarios.items():
        usuario_id = datos_usuario.get("id", "")
        agregado = "Si" if usuario_id in integrantes_proyecto else "No"
        filas.append([usuario_id, nombre_usuario.capitalize(), agregado])

    imprimir_tabla(
        [
            {"titulo": "ID", "min": 4, "peso": 1},
            {"titulo": "Usuario", "min": 18, "peso": 3},
            {"titulo": "Agregado", "min": 10, "peso": 1},
        ],
        filas
    )


def gestionar_integrantes_proyecto(proyecto, ListaUsuarios):
    if len(proyecto) <= 6:
        proyecto.append([])

    on = True

    while on:
        clearConsole()
        print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Gestionar Integrantes*]\033[0m")
        print()
        mostrar_tarea_proyecto("proyecto", proyecto)
        mostrarListaIntegrantesProyecto(ListaUsuarios, proyecto)
        usuario_id = input("Ingrese el ID del usuario para agregarlo o quitarlo del proyecto (0 para volver): ")

        if usuario_id == "":
            print()
            input("\033[31m[ERROR] El ID no puede estar vacio.\033[0m")
            continue

        if usuario_id == "0":
            print()
            # input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
            on = False
            continue

        if usuario_id.isdigit() == False:
            print()
            input("\033[31m[ERROR] El ID debe ser un numero.\033[0m")
            continue

        usuario_id = int(usuario_id)
        usuario_encontrado = None

        for nombre_usuario, datos_usuario in ListaUsuarios.items():
            if datos_usuario.get("id") == usuario_id:
                usuario_encontrado = (nombre_usuario, datos_usuario)
                break

        if usuario_encontrado is None:
            print()
            input("\033[31m[ERROR] El usuario con ese ID no existe.\033[0m")
            continue

        nombre_usuario, datos_usuario = usuario_encontrado
        proyectos_usuario = datos_usuario.setdefault("projects", [])
        registro_proyecto = None

        for proyecto_usuario in proyectos_usuario:
            if proyecto_usuario.get("projectId") == proyecto[0]:
                registro_proyecto = proyecto_usuario
                break

        if usuario_id in proyecto[6]:
            proyecto[6].remove(usuario_id)
            if registro_proyecto is not None:
                proyectos_usuario.remove(registro_proyecto)
            print()
            # input(f"\033[92m[EXITO] {nombre_usuario} fue quitado del proyecto.\033[0m")
        else:
            proyecto[6].append(usuario_id)
            if registro_proyecto is None:
                proyectos_usuario.append({
                    "projectId": proyecto[0],
                    "rol": "Sin rol",
                    "tareas": []
                })
            print()
            # input(f"\033[92m[EXITO] {nombre_usuario} fue agregado al proyecto.\033[0m")

