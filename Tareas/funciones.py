from General.clearConsole import clearConsole
from General.inputFecha import inputFecha
from General.mostrarTareasProyectos import mostrar_tarea_proyecto
from General.formato import imprimir_tabla, imprimir_titulo, truncar_texto
from General.utilidades import obtener_proximo_id
from Tareas.asignaciones import (
    alternar_asignacion_usuario_logueado,
    desincronizar_tarea_en_usuario,
    integrante_esta_asignado,
    obtener_id_usuario_logueado,
    obtener_integrantes_reales_proyecto,
    resumir_integrantes_asignados,
    sincronizar_tarea_en_usuario,
)


def formatearDescripcion(texto, max_caracteres=76):
    texto = str(texto)
    return texto[:max_caracteres - 3] + "..." if len(texto) > max_caracteres else texto

def _asignar_tarea_integrante_real(ListaTareas, proyecto, ListaUsuarios):
    clearConsole()
    print("\033[33m[[Menu Principal > Proyectos > Seleccionar Proyectos > *Asignar Tareas*]\033[0m")
    print()

    integrantes_proyecto = obtener_integrantes_reales_proyecto(proyecto, ListaUsuarios)

    if len(ListaTareas) == 0:
        input("No hay tareas registradas para asignar.")
        return

    if len(integrantes_proyecto) == 0:
        input("No hay integrantes registrados para asignar.")
        return

    p1 = True
    while p1:
        clearConsole()
        print("\033[33m[[Menu Principal > Proyectos > Seleccionar Proyectos > *Asignar Tareas*]\033[0m")
        print()
        mostrarListaTareas(ListaTareas)
        tarea_seleccionada = None

        try:
            id = int(input("• Ingrese el ID de la tarea a asignar (0 para cancelar): "))
        except ValueError:
            input("\033[31m[ERROR] El id debe ser un numero.\033[0m")
            continue

        if id == 0:
            print()
            input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
            return

        for item in ListaTareas:
            if item[0] == id:
                tarea_seleccionada = item
                break

        if tarea_seleccionada is None:
            input("\033[31m[ERROR] La tarea con el ID ingresado no existe.\033[0m")
            continue

        p2 = True
        while p2:
            clearConsole()
            print("\033[33m[[Menu Principal > Proyectos > Seleccionar Proyectos > *Asignar Tareas*]\033[0m")
            print()
            mostrar_tarea_proyecto("tarea", tarea_seleccionada)
            imprimir_tabla(
                [
                    {"titulo": "ID", "min": 4, "peso": 1},
                    {"titulo": "Usuario", "min": 18, "peso": 3},
                ],
                [[integrante["id"], integrante["nombre"]] for integrante in integrantes_proyecto]
            )

            try:
                usuario_id = int(input("• Ingrese el ID del integrante a asignar la tarea (0 para cancelar): "))
            except ValueError:
                print()
                input("\033[31m[ERROR] El id debe ser un numero.\033[0m")
                continue

            if usuario_id == 0:
                print()
                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
                p2 = False
                continue

            integrante_seleccionado = None
            for integrante in integrantes_proyecto:
                if integrante["id"] == usuario_id:
                    integrante_seleccionado = integrante
                    break

            if integrante_seleccionado is None:
                input("\033[31m[ERROR] El integrante con el ID ingresado no existe.\033[0m")
                continue

            asignados_actuales = tarea_seleccionada[6] if len(tarea_seleccionada) > 6 else []
            ya_asignado = False
            for asignado in asignados_actuales:
                if isinstance(asignado, dict) and asignado.get("id") == usuario_id:
                    ya_asignado = True
                    break
                if asignado == usuario_id:
                    ya_asignado = True
                    break

            if ya_asignado:
                print()
                input("\033[31m[ERROR] Ese integrante ya esta asignado a esta tarea.\033[0m")
                continue

            tarea_seleccionada[6].append({
                "id": integrante_seleccionado["id"],
                "nombre": integrante_seleccionado["nombre"],
            })
            sincronizar_tarea_en_usuario(ListaUsuarios, proyecto[0], tarea_seleccionada[0], usuario_id)

            print()
            input(f"\033[92m[EXITO] Tarea asignada exitosamente a {integrante_seleccionado['nombre']}.\033[0m")
            return


def mostrarListaTareas(ListaTareas):
    imprimir_titulo("Lista de Tareas")
    columnas = [
        {"titulo": "ID", "min": 4, "peso": 1},
        {"titulo": "Nombre", "min": 16, "peso": 3},
        {"titulo": "Integrantes Asignados", "min": 22, "peso": 4},
        {"titulo": "Fecha Inicio", "min": 12, "peso": 2},
        {"titulo": "Fecha Final", "min": 12, "peso": 2},
        {"titulo": "Estado", "min": 10, "peso": 2},
    ]
    filas = []

    for tarea in ListaTareas:
        id_tarea = tarea[0]
        nombre = tarea[1]
        fecha_inicio = tarea[3]
        fecha_final = tarea[4]
        estado = tarea[5]
        integrantes_asignados = tarea[6] if len(tarea) > 6 else []
        filas.append([
            id_tarea,
            truncar_texto(nombre, 40),
            resumir_integrantes_asignados(integrantes_asignados),
            fecha_inicio.strftime('%d/%m/%Y'),
            fecha_final.strftime('%d/%m/%Y'),
            estado,
        ])

    imprimir_tabla(columnas, filas)

def mostrarDetalleTarea(tarea):
    mostrar_tarea_proyecto("tarea", tarea)


def eliminar_tarea_por_id(ListaTareas, task_id, proyecto=None, ListaUsuarios=None):
    for indice, tarea in enumerate(ListaTareas):
        if tarea[0] == task_id:
            del ListaTareas[indice]
            if proyecto is not None and ListaUsuarios is not None:
                for datos_usuario in ListaUsuarios.values():
                    for relacion in datos_usuario.get("projects", []):
                        if relacion.get("projectId") == proyecto[0]:
                            relacion["tareas"] = [
                                tarea_id
                                for tarea_id in relacion.get("tareas", [])
                                if tarea_id != task_id
                            ]
            return True
    return False


def editar_tarea_seleccionada(ListaTareas, task_id, opcion_preseleccionada=None):
    posicion = None
    for indice, tarea in enumerate(ListaTareas):
        if tarea[0] == task_id:
            posicion = indice
            break

    if posicion is None:
        print()
        input("\033[31m[ERROR] La tarea ingresada no existe.\033[0m")
        return

    on = True
    while on:
        tarea_actual = ListaTareas[posicion]
        editarNombre = tarea_actual[1]
        editarDescripcion = tarea_actual[2]
        editarFechaInicio = tarea_actual[3]
        editarFechaFinal = tarea_actual[4]
        editarEstado = tarea_actual[5]
        integrantesAsignados = tarea_actual[6]

        clearConsole()
        print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Editar Tareas*]\033[0m")
        print()
        mostrar_tarea_proyecto("tarea", tarea_actual)
        print("1. Cambiar Nombre")
        print("2. Cambiar fecha de inicio")
        print("3. Cambiar fecha final")
        print("4. Cambiar el estado de la tarea")
        print("0. Volver")
        print("")
        opcion = input("• Seleccione una opción:")

        if opcion == "1":
            clearConsole()
            print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Editar Tareas(Nombre)*]\033[0m")
            print()
            mostrar_tarea_proyecto("tarea", tarea_actual)
            nuevoNombre = input("• Ingrese el nuevo nombre de la tarea (0 para cancelar): ")
            if nuevoNombre == "":
                print("")
                input("\033[31m[ERROR] El nombre ingresado no puede estar vacio\033[0m")
            elif nuevoNombre == "0":
                print("")
                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
            else:
                ListaTareas[posicion] = [task_id, nuevoNombre, editarDescripcion, editarFechaInicio, editarFechaFinal, editarEstado, integrantesAsignados]
                print("")
                input("\033[92m[EXITO] Tarea editada exitosamente.\033[0m")
                return

        elif opcion == "2":
            clearConsole()
            print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Editar Tareas(Fecha de Inicio)*]\033[0m")
            print()
            mostrar_tarea_proyecto("tarea", tarea_actual)
            nuevaFechaInicio = inputFecha("Inicio")
            if nuevaFechaInicio == "":
                print("")
                input("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m")
            elif nuevaFechaInicio == "0":
                print("")
                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
            elif nuevaFechaInicio == None:
                print("")
                input("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
            elif nuevaFechaInicio > editarFechaFinal:
                print("")
                input("\033[31m[ERROR] La fecha de inicio no puede ser posterior a la fecha final.\033[0m")
            else:
                ListaTareas[posicion] = [task_id, editarNombre, editarDescripcion, nuevaFechaInicio, editarFechaFinal, editarEstado, integrantesAsignados]
                print("")
                input("\033[92m[EXITO] Tarea editada exitosamente.\033[0m")
                return

        elif opcion == "3":
            clearConsole()
            print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Editar Tareas(Fecha Final)*]\033[0m")
            print()
            mostrar_tarea_proyecto("tarea", tarea_actual)
            nuevaFechaFinal = inputFecha("Final")
            if nuevaFechaFinal == "":
                print("")
                input("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m")
            elif nuevaFechaFinal == "0":
                print("")
                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
            elif nuevaFechaFinal == None:
                print("")
                input("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
            elif nuevaFechaFinal < editarFechaInicio:
                print("")
                input("\033[31m[ERROR] La fecha final no puede ser anterior a la fecha de inicio.\033[0m")
            else:
                ListaTareas[posicion] = [task_id, editarNombre, editarDescripcion, editarFechaInicio, nuevaFechaFinal, editarEstado, integrantesAsignados]
                print("")
                input("\033[92m[EXITO] Tarea editada exitosamente.\033[0m")
                return

        elif opcion == "4":
            clearConsole()
            print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Editar Tareas(Estado)*]\033[0m")
            print()
            mostrar_tarea_proyecto("tarea", tarea_actual)
            print("1. Activo")
            print("2. Completado")
            print("3. Expirado")
            print("0. Volver")
            nuevoEstado = input("Ingrese el nuevo estado de la tarea: ")
            if nuevoEstado == "1":
                nuevoEstado = "Activo"
            elif nuevoEstado == "2":
                nuevoEstado = "Completado"
            elif nuevoEstado == "3":
                nuevoEstado = "Expirado"
            elif nuevoEstado == "0":
                print("")
                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
                continue
            else:
                print("")
                input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
                continue

            ListaTareas[posicion] = [task_id, editarNombre, editarDescripcion, editarFechaInicio, editarFechaFinal, nuevoEstado, integrantesAsignados]
            print("")
            input("\033[92m[EXITO] Tarea editada exitosamente.\033[0m")
            return

        elif opcion == "0":
            print("")
            input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
            return

        else:
            print("")
            input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")


def editar_campo_tarea_seleccionada(ListaTareas, task_id, opcion):
    for indice, tarea in enumerate(ListaTareas):
        if tarea[0] == task_id:
            posicion = indice
            break
    else:
        print("")
        input("\033[31m[ERROR] La tarea ingresada no existe.\033[0m")
        return

    tarea_actual = ListaTareas[posicion]
    editarNombre = tarea_actual[1]
    editarDescripcion = tarea_actual[2]
    editarFechaInicio = tarea_actual[3]
    editarFechaFinal = tarea_actual[4]
    editarEstado = tarea_actual[5]
    integrantesAsignados = tarea_actual[6]

    if opcion == "1":
        clearConsole()
        print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Editar Tareas(Nombre)*]\033[0m")
        print()
        mostrar_tarea_proyecto("tarea", tarea_actual)
        nuevoNombre = input("• Ingrese el nuevo nombre de la tarea (0 para cancelar): ")
        if nuevoNombre == "":
            print("")
            input("\033[31m[ERROR] El nombre ingresado no puede estar vacio\033[0m")
        elif nuevoNombre == "0":
            print("")
            input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
        else:
            ListaTareas[posicion] = [task_id, nuevoNombre, editarDescripcion, editarFechaInicio, editarFechaFinal, editarEstado, integrantesAsignados]
            print("")
            input("\033[92m[EXITO] Tarea editada exitosamente.\033[0m")

    elif opcion == "2":
        clearConsole()
        print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Editar Tareas(Descripcion)*]\033[0m")
        print()
        mostrar_tarea_proyecto("tarea", tarea_actual)
        nuevaDescripcion = input("• Ingrese la nueva descripción de la tarea (0 para cancelar): ")
        if nuevaDescripcion == "":
            print("")
            input("\033[31m[ERROR] La descripcion ingresada no puede estar vacia.\033[0m")
        elif nuevaDescripcion == "0":
            print("")
            input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
        else:
            ListaTareas[posicion] = [task_id, editarNombre, nuevaDescripcion, editarFechaInicio, editarFechaFinal, editarEstado, integrantesAsignados]
            print("")
            input("\033[92m[EXITO] Tarea editada exitosamente.\033[0m")

    elif opcion == "3":
        clearConsole()
        print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Editar Tareas(Fecha de Inicio)*]\033[0m")
        print()
        mostrar_tarea_proyecto("tarea", tarea_actual)
        nuevaFechaInicio = inputFecha("Inicio")
        if nuevaFechaInicio == "":
            print("")
            input("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m")
        elif nuevaFechaInicio == "0":
            print("")
            input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
        elif nuevaFechaInicio == None:
            print("")
            input("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
        elif nuevaFechaInicio > editarFechaFinal:
            print("")
            input("\033[31m[ERROR] La fecha de inicio no puede ser posterior a la fecha final.\033[0m")
        else:
            ListaTareas[posicion] = [task_id, editarNombre, editarDescripcion, nuevaFechaInicio, editarFechaFinal, editarEstado, integrantesAsignados]
            print("")
            input("\033[92m[EXITO] Tarea editada exitosamente.\033[0m")

    elif opcion == "4":
        clearConsole()
        print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Editar Tareas(Fecha Final)*]\033[0m")
        print()
        mostrar_tarea_proyecto("tarea", tarea_actual)
        nuevaFechaFinal = inputFecha("Final")
        if nuevaFechaFinal == "":
            print("")
            input("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m")
        elif nuevaFechaFinal == "0":
            print("")
            input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
        elif nuevaFechaFinal == None:
            print("")
            input("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
        elif nuevaFechaFinal < editarFechaInicio:
            print("")
            input("\033[31m[ERROR] La fecha final no puede ser anterior a la fecha de inicio.\033[0m")
        else:
            ListaTareas[posicion] = [task_id, editarNombre, editarDescripcion, editarFechaInicio, nuevaFechaFinal, editarEstado, integrantesAsignados]
            print("")
            input("\033[92m[EXITO] Tarea editada exitosamente.\033[0m")

    elif opcion == "5":
        clearConsole()
        print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Editar Tareas(Estado)*]\033[0m")
        print()
        mostrar_tarea_proyecto("tarea", tarea_actual)
        print("\033[92m1. Activo\033[0m" if editarEstado == "Activo" else "1. Activo")
        print("\033[92m2. Completado\033[0m" if editarEstado == "Completado" else "2. Completado")
        print("\033[92m3. Expirado\033[0m" if editarEstado == "Expirado" else "3. Expirado")
        print("0. Volver")
        nuevoEstado = input("Ingrese el nuevo estado de la tarea: ")
        if nuevoEstado == "1":
            nuevoEstado = "Activo"
        elif nuevoEstado == "2":
            nuevoEstado = "Completado"
        elif nuevoEstado == "3":
            nuevoEstado = "Expirado"
        elif nuevoEstado == "0":
            print("")
            input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
            return
        else:
            print("")
            input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
            return

        ListaTareas[posicion] = [task_id, editarNombre, editarDescripcion, editarFechaInicio, editarFechaFinal, nuevoEstado, integrantesAsignados]
        return


def seleccionar_tarea_basica(ListaTareas):
    clearConsole()
    print("\033[33m[Menu principal > Proyectos > Seleccionar Proyectos > Proyecto Seleccionado > *Seleccionar Tarea*]\033[0m")
    print()

    if len(ListaTareas) == 0:
        input("No hay tareas registradas.")
        return

    on = True
    while on:
        clearConsole()
        print("\033[33m[Menu principal > Proyectos > Seleccionar Proyectos > Proyecto Seleccionado > *Seleccionar Tarea*]\033[0m")
        # print()
        mostrarListaTareas(ListaTareas)
        task_id = input("• Ingrese el ID de la tarea a seleccionar (0 para volver): ")

        if task_id == "":
            print()
            input("\033[31m[ERROR] El id no puede estar vacio.\033[0m")
            continue
        elif task_id.isdigit() == False:
            print()
            input("\033[31m[ERROR] El id debe ser un numero.\033[0m")
            continue
        elif task_id == "0":
            print()
            # input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
            return

        tarea_seleccionada = None
        task_id = int(task_id)
        for tarea in ListaTareas:
            if tarea[0] == task_id:
                tarea_seleccionada = tarea
                break

        if tarea_seleccionada is None:
            print()
            input("\033[31m[ERROR] La tarea ingresada no existe.\033[0m")
            continue

        submenu_on = True
        while submenu_on:
            clearConsole()
            print("\033[33m[Menu principal > Proyectos > Seleccionar Proyectos > Proyecto Seleccionado > *Tarea Seleccionada*]\033[0m")
            print()
            mostrarDetalleTarea(tarea_seleccionada)
            print("1. Cambiar Nombre")
            print("2. Cambiar fecha de inicio")
            print("3. Cambiar fecha final")
            print("4. Cambiar el estado de la tarea")
            print("5. Eliminar tarea")
            print("0. Volver")
            print()
            opcion = input("• Seleccione una opción: ")

            if opcion in ["1", "2", "3", "4"]:
                editar_campo_tarea_seleccionada(ListaTareas, task_id, opcion)
                return
            elif opcion == "5":
                clearConsole()
                print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Eliminar Tarea*]\033[0m")
                print()
                mostrarDetalleTarea(tarea_seleccionada)
                confirmacion = input("¿Desea eliminar esta tarea? (1 = Sí | 0 = No): ")
                if confirmacion == "1":
                    eliminar_tarea_por_id(ListaTareas, task_id)
                    print()
                    input("\033[92m[EXITO] Tarea eliminada correctamente.\033[0m")
                    return
                elif confirmacion == "0":
                    print()
                    input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
                else:
                    print()
                    input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
            elif opcion == "0":
                return
            else:
                print()
                input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")

def ver_tareas_basica(ListaTareas):
    seleccionar_tarea_basica(ListaTareas)

def crear_tarea(ListaTareas):
    clearConsole()
    print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Crear Tarea*]\033[0m")
    print()
    id = obtener_proximo_id(ListaTareas)
    p1,p2,p3,p4= True,False,False,False

    inProgress = True

    while p1 and inProgress:
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > *Crear Tarea*]\033[0m")
        print()
        nombreTarea=input("• Ingrese el nombre de la tarea (0 para cancelar): ")
        if nombreTarea == "":
            print("")
            input("\033[31m[ERROR] El nombre de la tarea no puede estar vacio.\033[0m")
        elif nombreTarea == "0":
            p1 = False
            inProgress = False
            print("")
            input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
        else:
            p1 = False
            p2 = True

    while p2 and inProgress:
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > *Crear Tarea*]\033[0m")
        print()
        print(f"\033[36mNombre de la tarea:\033[0m {nombreTarea}")
        print()
        descripcionTarea=input("• Ingrese la descripcion de la tarea (0 para cancelar): ")
        if descripcionTarea == "":
            print("")
            input("\033[31m[ERROR] El nombre de la tarea no puede estar vacio.\033[0m")
        elif descripcionTarea == "0":
            p2 = False
            inProgress = False
            print("")
            input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
        else:
            p2 = False
            p3 = True

    while p3 and inProgress:
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > *Crear Tarea*]\033[0m")
        print()
        print(f"\033[36mNombre de la tarea:\033[0m {nombreTarea}")
        print(f"\033[36mDescripcion de la tarea:\033[0m {formatearDescripcion(descripcionTarea)}")
        print()
        FechaInicio=inputFecha("Inicio")
        if FechaInicio == "":
            print("")
            input("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m") 
        elif FechaInicio == None:
            print("")
            input("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
        elif FechaInicio == "0":
            p3 = False
            inProgress = False
            print("")
            input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
        else:
            p3 = False
            p4 = True
    
    while p4 and inProgress:
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > *Crear Tarea*]\033[0m")
        print()
        print(f"\033[36mNombre de la tarea:\033[0m {nombreTarea}")
        print(f"\033[36mDescripcion de la tarea:\033[0m {formatearDescripcion(descripcionTarea)}")
        print(f"\033[36mFecha de Inicio:\033[0m {FechaInicio.strftime('%d/%m/%Y')}")
        print()
        FechaFinal=inputFecha("Final")
        if FechaFinal == "0":
            p4 = False
            inProgress = False
            print("")
            input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
        elif FechaFinal == "":
            print("")
            input("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m")
        elif FechaFinal == None:
            print("")
            input("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
        elif FechaFinal < FechaInicio:
            print("")
            input("\033[31m[ERROR] La fecha final no puede ser anterior a la fecha de inicio.\033[0m")
        else:
            p4 = False
            EstadoTarea = "Activo"
    
    if inProgress:
        #? Type Proyecto = [id,nombreProyecto,tareas,FechaInicio,FechaFinal,Estado]
        nueva_tarea = [id,nombreTarea,descripcionTarea,FechaInicio,FechaFinal,EstadoTarea,[]]
        
        ListaTareas.append(nueva_tarea)
        clearConsole()
        print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > *Crear Tarea*]\033[0m")
        print("")
        print(f"\033[36mNombre de la tarea:\033[0m {nombreTarea}")
        print(f"\033[36mDescripcion de la tarea:\033[0m {formatearDescripcion(descripcionTarea)}")
        print(f"\033[36mFecha de Inicio:\033[0m {FechaInicio.strftime('%d/%m/%Y')}")
        print(f"\033[36mFecha de Finalizacion:\033[0m {FechaFinal.strftime('%d/%m/%Y')}")
        # print(f"Estado: {EstadoTarea}")
        print()
        input("\033[92m[EXITO] Tarea creada correctamente.\033[0m")
    else:
        # input("Operacion cancelada.")
        pass


def editar_tarea(ListaTareas):
    on = True
    
    if len(ListaTareas) == 0:
        clearConsole()
        print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Editar Tareas*]\033[0m")
        print()
        input("No hay tareas registradas.")
    else:
        while on:   
            p1 = True
            p2 = False
            clearConsole()
            print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Editar Tareas*]\033[0m")
            print()
            mostrarListaTareas(ListaTareas)
            #* Que_tarea? [POSICION]
            posicion = 0
            isTaskReal = False
            task_id = input("• Ingrese ID de la tarea a editar (0 para cancelar): ")
            if task_id == "":
                print()
                input("\033[31m[ERROR] El id no puede estar vacio.\033[0m")
            elif task_id.isdigit() == False:
                print()
                input("\033[31m[ERROR] El id debe ser un numero.\033[0m")
            elif task_id == "0":
                on = False
                print()
                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
            elif task_id.isdigit() == True and task_id != "":
                task_id = int(task_id)
                for indice, item in enumerate(ListaTareas):
                        if item[0] == task_id:
                            posicion = indice
                            isTaskReal = True
                            p1 = True

                while p1 and isTaskReal:
                    p4 = True
                    #* Menu con variables de ESA tarea (1. Cambiar Nombre - 2. Cambiar fecha de inicio - 3. Cambiar fecha final - 4. Nuevo estado de la tarea)
                    id = ListaTareas[posicion][0]
                    editarNombre = ListaTareas[posicion][1]
                    editarDescripcion = ListaTareas[posicion][2]
                    editarFechaInicio = ListaTareas[posicion][3]
                    editarFechaFinal = ListaTareas[posicion][4]
                    editarEstado = ListaTareas[posicion][5]
                    integrantesAsignados = ListaTareas[posicion][6]
                   
                    clearConsole()
                    print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Editar Tareas*]\033[0m")
                    print()
                    mostrar_tarea_proyecto("tarea", ListaTareas[posicion])
                    print("1. Cambiar Nombre")
                    print("2. Cambiar fecha de inicio")
                    print("3. Cambiar fecha final")
                    print("4. Cambiar el estado de la tarea")
                    print("0. Volver")
                    print("")
                    opcion = input("• Seleccione una opcion:")
                    
                    if opcion == "1":
                        while p4:    
                            clearConsole()
                            print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Tareas(Nombre)*]\033[0m")
                            print()
                            mostrar_tarea_proyecto("tarea", ListaTareas[posicion])
                            editarNombre=input("• Ingrese el nuevo nombre de la tarea (0 para cancelar): ")
                            if editarNombre == "":
                                print("")
                                print("\033[31m[ERROR] El nombre ingresado no puede estar vacio\033[0m")
                                input("Ingrese cualquier opcion para continuar...")
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
                            print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Tareas(Fecha de Inicio)*]\033[0m")
                            print()
                            mostrar_tarea_proyecto("tarea", ListaTareas[posicion])
                            editarFechaInicio=inputFecha("Inicio")
                            if editarFechaInicio == "":
                                print("")
                                print("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m")
                                input("Ingrese cualquier opcion para continuar...")
                            elif editarFechaInicio == "0":
                                p4 = False
                                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
                            elif editarFechaInicio == None:
                                print("")
                                print("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
                                input("Ingrese cualquier opcion para continuar...")
                            elif editarFechaInicio > editarFechaFinal:
                                print("")
                                print("\033[31m[ERROR] La fecha de inicio no puede ser posterior a la fecha final.\033[0m")
                                input("Ingrese cualquier opcion para continuar...")
                            else:
                                p4 = False   
                                p1 = False
                                p2 = True
                            
                    elif opcion == "3":
                        while p4:   
                            clearConsole()
                            print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Tareas(Fecha Final)*]\033[0m")
                            print()
                            mostrar_tarea_proyecto("tarea", ListaTareas[posicion])
                            editarFechaFinal=inputFecha("Final")
                            if editarFechaFinal == "":
                                print("")
                                print("\033[31m[ERROR] La fecha ingresada no puede estar vacia.\033[0m")
                                input("Ingrese cualquier opcion para continuar...")
                            elif editarFechaFinal == "0":
                                p4 = False
                                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
                            elif editarFechaFinal == None:
                                print("")
                                print("\033[31m[ERROR] La fecha ingresada no es valida.\033[0m")
                                input("Ingrese cualquier opcion para continuar...")
                            elif editarFechaFinal < editarFechaInicio:
                                print("")
                                print("\033[31m[ERROR] La fecha final no puede ser anterior a la fecha de inicio.\033[0m")
                                input("Ingrese cualquier opcion para continuar...")
                            else:
                                p4 = False   
                                p1 = False
                                p2 = True
                    
                    elif opcion == "4": 
                        clearConsole()
                        while p4:
                            clearConsole()
                            print("\033[33m[Menu Principal > Proyectos > Seleccionar Proyectos > Editar *Tareas(Estado)*]\033[0m")
                            print()
                            mostrar_tarea_proyecto("tarea", ListaTareas[posicion])
                            print("1. Activo")
                            print("2. Completado")
                            print("3. Expirado")
                            print("0. Volver")
                            editarEstado=input("Ingrese el nuevo estado de la tarea: ")
                            if editarEstado == "1":
                                editarEstado = "Activo"
                                p4 = False
                                p1 = False
                                p2 = True
                            elif editarEstado == "2":
                                editarEstado = "Completado"
                                p4 = False
                                p1 = False
                                p2 = True
                            elif editarEstado == "3":
                                editarEstado = "Expirado"
                                p4 = False
                                p1 = False
                                p2 = True
                            elif editarEstado == "":
                                print("Opcion invalida. Intente nuevamente.")
                                input("Ingrese cualquier opcion para continuar...")
                            else:
                                print("Opcion invalida. Intente nuevamente.")
                                input("Ingrese cualquier opcion para continuar...")
                    elif opcion == "0":
                        p1 = False
                        input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
                    else:
                        input("\033[31m[ERROR] Número inválido.\033[0m")

                    tarea_editada = [id,editarNombre,editarDescripcion,editarFechaInicio,editarFechaFinal,editarEstado,integrantesAsignados]
                   

                while p2 and isTaskReal:
                    clearConsole()
                    print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Editar Tareas*]\033[0m")
                    print()
                    print(f"Nombre: {editarNombre}")
                    print(f"Descripcion: {formatearDescripcion(editarDescripcion)}")
                    print(f"Fecha de Inicio: {editarFechaInicio.strftime('%d/%m/%Y')}")
                    print(f"Fecha Final: {editarFechaFinal.strftime('%d/%m/%Y')}")
                    print(f"Estado: {editarEstado}")
                    print()
                    try:
                        opcion = int(input("¿Desea guardar los cambios? (1 = Si | 0 = No): "))
                        if opcion == 1:
                            ListaTareas[posicion] = tarea_editada
                            print()
                            input("[EXITO] Tarea editada exitosamente.")
                            p2 = False
                            
                        elif opcion == 0:
                            print()
                            input("\033[93m[CANCELADO] No se realizaron cambios.\033[0m")
                            p2 = False

                        elif opcion == "":
                            input("\033[31m[ERROR] La opción no puede estar vacía.\033[0m")
                        else:
                            input("\033[31m[ERROR] Opcion Invalida\033[0m") 
                    except ValueError:
                        print()
                        input("\033[31m[ERROR] El valor ingresado debe ser un numero \033[0m") 
 

            else:
                input("\033[31m[ERROR] La tarea ingresada no existe.\033[0m")


def eliminar_tarea(ListaTareas, proyecto=None, ListaUsuarios=None):
    #! AGREGAR CONFIRMACION PARA EL DELETE DE LA TAREA + MOSTRAR LA TAREA (imprimir Tarea) para que el usuario vea los datos y confirme visualmente que sea la tarea que queria inputear by ID
    if len(ListaTareas) == 0:
        clearConsole()
        print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Eliminar Tarea*]\033[0m")
        print()
        input("No hay tareas registradas.")
    else:
        on = True
        while on:
            clearConsole()
            print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Eliminar Tarea*]\033[0m")
            print()
            id = input("• Ingrese el ID de la tarea a eliminar: (0 para volver)")
            isTaskReal = False
            if id == "":
                print()
                input("\033[31m[ERROR] El id no puede estar vacio.\033[0m")
            elif id.isdigit() == False:
                print()
                input("\033[31m[ERROR] El id debe ser un numero.\033[0m") 
            elif id == "0":
                on = False
                print()
                input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
            else:
                id = int(id)
                for item in ListaTareas:
                    if item[0] == id:
                        isTaskReal = True
                if isTaskReal:
                    eliminar_tarea_por_id(ListaTareas, id, proyecto, ListaUsuarios)
                    on = False
                    print()
                    input("\033[92m[EXITO] Tarea eliminada correctamente.\033[0m")
                else:
                    print()
                    input("\033[31m[ERROR] La tarea con el ID ingresado no existe.\033[0m")

def asignar_tarea_integrante_basica(ListaTareas, ListaUsuariosProyecto):
    clearConsole()
    print("\033[33m[[Menu Principal > Proyectos > Seleccionar Proyectos > *Asignar Tareas*]\033[0m")
    print()
    if len(ListaTareas) == 0:
        input("No hay tareas registradas para asignar.")
    elif len(ListaUsuariosProyecto) == 0:
        input("No hay integrantes registrados para asignar.")
    else:
        p1 = True
        while p1:
            clearConsole()
            print("\033[33m[[Menu Principal > Proyectos > Seleccionar Proyectos > *Asignar Tareas*]\033[0m")
            print()
            mostrarListaTareas(ListaTareas)
            isTaskReal = False
            try:
                id = int(input("• Ingrese el ID de la tarea a asignar (0 para cancelar): "))
                if id == 0:
                    p1 = False
                    print()
                    input("Operacion cancelada")
                else:
                    for item in ListaTareas:
                        if item[0] == id:
                            isTaskReal = True
                    if isTaskReal:
                        #* Mostrar lista de integrantes y seleccionar integrante para asignar la tarea
                        clearConsole()
                        print("\033[33m[[Menu Principal > Proyectos > Seleccionar Proyectos > *Asignar Tareas*]\033[0m")
                        print()
                        #for integrante in ListaUsuariosProyecto:
                            # print("==== Integrantes ====")
                            # print()
                            # print(f"{'ID':<5}{'Nombre':<25}{'Rol':<15}")
                            # print("-" * 50)
                            # print(f"ID: {integrante[0]} | Nombre: {integrante[1]} | Rol: {integrante[2]}")
                        print()
                        p2 = True
                        while p2:
                            clearConsole()
                            print("\033[33m[[Menu Principal > Proyectos > Seleccionar Proyectos > *Asignar Tareas*]\033[0m")
                            print()
                            try:    
                                isIntegranteReal = False
                                usuario_id = int(input("• Ingrese el ID del integrante a asignar la tarea (0 para cancelar): "))
                                if usuario_id == 0:
                                    p2 = False
                                    print()
                                    input("Operacion cancelada")
                                else:
                                    for usuario in ListaUsuariosProyecto:
                                        if usuario == usuario_id:
                                            isIntegranteReal = True
                                            item[6].append(usuario_id)

                                    if isIntegranteReal:
                                        p2 = False
                                        print()
                                        print(f"Tarea asignada exitosamente al usuario {usuario_id}")
                                        input("Ingrese cualquier opcion para continuar...")

                                    else:
                                        input("\033[31m[ERROR] El integrante con el ID ingresado no existe.\033[0m")

                            
                            except ValueError:
                                print()
                                input("\033[31m[ERROR] El id debe ser un numero.\033[0m")

                    else:
                        input("\033[31m[ERROR] La tarea con el ID ingresado no existe.\033[0m")
            
            except ValueError:
                input("\033[31m[ERROR] El id debe ser un numero.\033[0m")


def _asignar_tarea_integrante_real_persistente(ListaTareas, proyecto, ListaUsuarios):
    clearConsole()
    print("\033[33m[[Menu Principal > Proyectos > Seleccionar Proyectos > *Asignar Tareas*]\033[0m")
    print()

    integrantes_proyecto = obtener_integrantes_reales_proyecto(proyecto, ListaUsuarios)

    if len(ListaTareas) == 0:
        input("No hay tareas registradas para asignar.")
        return

    if len(integrantes_proyecto) == 0:
        input("No hay integrantes registrados para asignar.")
        return

    while True:
        clearConsole()
        print("\033[33m[[Menu Principal > Proyectos > Seleccionar Proyectos > *Asignar Tareas*]\033[0m")
        print()
        mostrarListaTareas(ListaTareas)

        try:
            task_id = int(input("• Ingrese el ID de la tarea a gestionar (0 para volver): "))
        except ValueError:
            input("\033[31m[ERROR] El id debe ser un numero.\033[0m")
            continue

        if task_id == 0:
            return

        tarea_seleccionada = None
        for tarea in ListaTareas:
            if tarea[0] == task_id:
                tarea_seleccionada = tarea
                break

        if tarea_seleccionada is None:
            input("\033[31m[ERROR] La tarea con el ID ingresado no existe.\033[0m")
            continue

        while True:
            clearConsole()
            print("\033[33m[[Menu Principal > Proyectos > Seleccionar Proyectos > *Asignar Tareas*]\033[0m")
            print()
            mostrar_tarea_proyecto("tarea", tarea_seleccionada)

            asignados_actuales = tarea_seleccionada[6] if len(tarea_seleccionada) > 6 else []
            filas_integrantes = []
            for integrante in integrantes_proyecto:
                filas_integrantes.append([
                    integrante["id"],
                    integrante["nombre"],
                    "Si" if integrante_esta_asignado(asignados_actuales, integrante["id"]) else "No",
                ])

            imprimir_tabla(
                [
                    {"titulo": "ID", "min": 4, "peso": 1},
                    {"titulo": "Usuario", "min": 18, "peso": 3},
                    {"titulo": "Asignado", "min": 10, "peso": 1},
                ],
                filas_integrantes
            )

            try:
                usuario_id = int(input("• Ingrese el ID del integrante para asignarlo/quitarlo de la tarea (0 para volver): "))
            except ValueError:
                input("\033[31m[ERROR] El id debe ser un numero.\033[0m")
                continue

            if usuario_id == 0:
                break

            integrante_seleccionado = None
            for integrante in integrantes_proyecto:
                if integrante["id"] == usuario_id:
                    integrante_seleccionado = integrante
                    break

            if integrante_seleccionado is None:
                input("\033[31m[ERROR] El integrante con el ID ingresado no existe.\033[0m")
                continue

            if integrante_esta_asignado(asignados_actuales, usuario_id):
                tarea_seleccionada[6] = [
                    asignado for asignado in asignados_actuales
                    if not (
                        (isinstance(asignado, dict) and asignado.get("id") == usuario_id) or
                        asignado == usuario_id
                    )
                ]
                desincronizar_tarea_en_usuario(ListaUsuarios, proyecto[0], tarea_seleccionada[0], usuario_id)
                input(f"\033[92m[EXITO] {integrante_seleccionado['nombre']} fue quitado de la tarea.\033[0m")
                continue

            tarea_seleccionada[6].append({
                "id": integrante_seleccionado["id"],
                "nombre": integrante_seleccionado["nombre"],
            })
            sincronizar_tarea_en_usuario(ListaUsuarios, proyecto[0], tarea_seleccionada[0], usuario_id)
            input(f"\033[92m[EXITO] Tarea asignada exitosamente a {integrante_seleccionado['nombre']}.\033[0m")


def asignar_tarea_integrante(ListaTareas, proyecto=None, ListaUsuarios=None):
    if ListaUsuarios is None:
        integrantes = proyecto if proyecto is not None else []
        return asignar_tarea_integrante_basica(ListaTareas, integrantes)
    return _asignar_tarea_integrante_real_persistente(ListaTareas, proyecto, ListaUsuarios)


def seleccionar_tarea(ListaTareas, proyecto, ListaUsuarios, credencial):
    clearConsole()
    print("\033[33m[Menu principal > Proyectos > Seleccionar Proyectos > Proyecto Seleccionado > *Seleccionar Tarea*]\033[0m")
    print()

    if len(ListaTareas) == 0:
        input("No hay tareas registradas.")
        return

    while True:
        clearConsole()
        print("\033[33m[Menu principal > Proyectos > Seleccionar Proyectos > Proyecto Seleccionado > *Seleccionar Tarea*]\033[0m")
        mostrarListaTareas(ListaTareas)
        task_id = input("• Ingrese el ID de la tarea a seleccionar (0 para volver): ")

        if task_id == "":
            print()
            input("\033[31m[ERROR] El id no puede estar vacio.\033[0m")
            continue
        if task_id.isdigit() == False:
            print()
            input("\033[31m[ERROR] El id debe ser un numero.\033[0m")
            continue
        if task_id == "0":
            return

        tarea_seleccionada = None
        task_id = int(task_id)
        for tarea in ListaTareas:
            if tarea[0] == task_id:
                tarea_seleccionada = tarea
                break

        if tarea_seleccionada is None:
            print()
            input("\033[31m[ERROR] La tarea ingresada no existe.\033[0m")
            continue

        while True:
            clearConsole()
            print("\033[33m[Menu principal > Proyectos > Seleccionar Proyectos > Proyecto Seleccionado > *Tarea Seleccionada*]\033[0m")
            print()
            mostrarDetalleTarea(tarea_seleccionada)

            usuario_id_logueado, _ = obtener_id_usuario_logueado(ListaUsuarios, credencial)
            asignados_actuales = tarea_seleccionada[6] if len(tarea_seleccionada) > 6 else []
            texto_toggle_asignacion = "Dejar Tarea" if integrante_esta_asignado(asignados_actuales, usuario_id_logueado) else "Asignarse Tarea"

            print("1. Cambiar Nombre")
            print("2. Cambiar descripcion")
            print("3. Cambiar fecha de inicio")
            print("4. Cambiar fecha final")
            print("5. Cambiar el estado de la tarea")
            print(f"6. {texto_toggle_asignacion}")
            print("7. Eliminar tarea")
            print("0. Volver")
            print()
            opcion = input("• Seleccione una opción: ")

            if opcion in ["1", "2", "3", "4", "5"]:
                editar_campo_tarea_seleccionada(ListaTareas, task_id, opcion)
                for tarea_actualizada in ListaTareas:
                    if tarea_actualizada[0] == task_id:
                        tarea_seleccionada = tarea_actualizada
                        break
                continue
            if opcion == "6":
                alternar_asignacion_usuario_logueado(tarea_seleccionada, proyecto, ListaUsuarios, credencial)
                continue
            if opcion == "7":
                clearConsole()
                print("\033[33m[Menu principal > Proyectos > Proyecto Seleccionado > *Eliminar Tarea*]\033[0m")
                print()
                mostrarDetalleTarea(tarea_seleccionada)
                confirmacion = input("¿Desea eliminar esta tarea? (1 = Si | 0 = No): ")
                if confirmacion == "1":
                    eliminar_tarea_por_id(
                        ListaTareas, task_id, proyecto, ListaUsuarios
                    )
                    print()
                    input("\033[92m[EXITO] Tarea eliminada correctamente.\033[0m")
                    return
                if confirmacion == "0":
                    print()
                    input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
                    continue
                print()
                input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
                continue
            if opcion == "0":
                return

            print()
            input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")


def ver_tareas(ListaTareas, proyecto=None, ListaUsuarios=None, credencial=None):
    if proyecto is None or ListaUsuarios is None or credencial is None:
        return ver_tareas_basica(ListaTareas)
    seleccionar_tarea(ListaTareas, proyecto, ListaUsuarios, credencial)
