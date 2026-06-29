from General.formato import imprimir_titulo, obtener_ancho_terminal, truncar_texto
import re
import textwrap


ANSI_PATTERN = re.compile(r"\033\[[0-9;]*m")


def calcular_metricas_proyecto(proyecto):
    tareas = proyecto[2] if len(proyecto) > 2 else []
    integrantes = proyecto[6] if len(proyecto) > 6 else []

    total_tareas = len(tareas)
    tareas_completadas = 0

    for tarea in tareas:
        estado_tarea = str(tarea[5]).strip().lower() if len(tarea) > 5 else ""
        if estado_tarea in ["completado", "completa"]:
            tareas_completadas += 1

    if total_tareas == 0:
        progreso = "0%"
    else:
        progreso = f"{round((tareas_completadas / total_tareas) * 100)}%"

    return total_tareas, len(integrantes), progreso


def construir_row_simetrica(items, ancho_total):
    cantidad = len(items)
    if cantidad == 0:
        return ""

    def largo_visible(texto):
        return len(ANSI_PATTERN.sub("", str(texto)))

    items = [str(item) for item in items]
    largos = [largo_visible(item) for item in items]
    ancho_minimo = sum(largos)

    if ancho_minimo >= ancho_total:
        return " ".join(items)

    separadores = cantidad - 1
    espacio_disponible = ancho_total - ancho_minimo
    espacios = [0] * (cantidad + 1)

    if separadores == 0:
        espacios[0] = espacio_disponible // 2
        espacios[1] = espacio_disponible - espacios[0]
    else:
        espacio_extremos = espacio_disponible // (2 * cantidad)
        espacios[0] = espacio_extremos
        espacios[-1] = espacio_extremos
        espacio_restante = espacio_disponible - espacios[0] - espacios[-1]
        espacio_entre = espacio_restante // separadores
        sobrante = espacio_restante % separadores

        for indice in range(1, cantidad):
            espacios[indice] = espacio_entre
            if sobrante > 0:
                espacios[indice] += 1
                sobrante -= 1

    partes = [" " * espacios[0]]
    for indice, item in enumerate(items):
        partes.append(item)
        partes.append(" " * espacios[indice + 1])

    return "".join(partes)


def construir_row_columnas(items, ancho_total, pesos):
    def largo_visible(texto):
        return len(ANSI_PATTERN.sub("", str(texto)))

    separador = " | "
    ancho_separadores = len(separador) * (len(items) - 1)
    ancho_util = max(len(items), ancho_total - ancho_separadores)
    peso_total = sum(pesos)
    anchos = []

    for peso in pesos:
        anchos.append((ancho_util * peso) // peso_total)

    diferencia = ancho_util - sum(anchos)
    indice = len(anchos) - 1
    while diferencia > 0:
        anchos[indice] += 1
        diferencia -= 1
        indice = (indice - 1) % len(anchos)

    celdas = []
    for indice, item in enumerate(items):
        item = str(item)
        ancho_celda = anchos[indice]
        if largo_visible(item) > ancho_celda:
            texto_visible = ANSI_PATTERN.sub("", item)
            texto_recortado = truncar_texto(texto_visible, ancho_celda)
            item = texto_recortado
        padding_total = max(0, ancho_celda - largo_visible(item))
        padding_izquierdo = padding_total // 2
        padding_derecho = padding_total - padding_izquierdo
        celdas.append((" " * padding_izquierdo) + item + (" " * padding_derecho))

    return separador.join(celdas)


def centrar_texto_visible(texto, ancho_total):
    largo_visible = len(ANSI_PATTERN.sub("", str(texto)))
    if largo_visible >= ancho_total:
        return str(texto)

    padding_izquierdo = (ancho_total - largo_visible) // 2
    padding_derecho = ancho_total - largo_visible - padding_izquierdo
    return (" " * padding_izquierdo) + str(texto) + (" " * padding_derecho)


def imprimir_bloque_centrado(texto, ancho_total):
    lineas = textwrap.wrap(str(texto), width=max(20, ancho_total - 2), break_long_words=False, break_on_hyphens=False)
    if len(lineas) == 0:
        print("")
        return

    for linea in lineas:
        print(centrar_texto_visible(linea, ancho_total))


def mostrar_tarea_proyecto(mode,posicion):
    formatear_descripcion = lambda texto, max_caracteres=76: (
        str(texto)[:max_caracteres - 3] + "..."
        if len(str(texto)) > max_caracteres
        else str(texto)
    )
    ancho = obtener_ancho_terminal()
    separador = "-" * ancho

    if mode == "proyecto":
        total_tareas, total_integrantes, progreso = calcular_metricas_proyecto(posicion)
        imprimir_titulo(truncar_texto(posicion[1], max(10, ancho - 2)))
        pesos_columnas = [1, 1, 2]
        primera_row = construir_row_columnas(
            [
                f"\033[36mID:\033[0m {posicion[0]}",
                f"\033[36mStatus:\033[0m {posicion[5]}",
                f"\033[36mFecha Inicio/Final:\033[0m {posicion[3].strftime('%d/%m/%Y')} - {posicion[4].strftime('%d/%m/%Y')}",
            ],
            ancho,
            pesos_columnas
        )
        segunda_row = construir_row_columnas(
            [
                f"\033[36mIntegrantes:\033[0m {total_integrantes}",
                f"\033[36mTareas:\033[0m {total_tareas}",
                f"\033[36mProgreso:\033[0m {progreso}",
            ],
            ancho,
            pesos_columnas
        )
        print(primera_row)
        print(segunda_row)
        print()

    elif mode == "tarea":
        integrantes_asignados = posicion[6] if len(posicion) > 6 else []
        nombres_asignados = []
        for integrante in integrantes_asignados:
            if isinstance(integrante, dict) and "nombre" in integrante:
                nombres_asignados.append(str(integrante["nombre"]))
            else:
                nombres_asignados.append(str(integrante))

        integrantes_formateados = ", ".join(nombres_asignados) if len(nombres_asignados) > 0 else "Ninguno"
        cantidad_integrantes = len(integrantes_asignados)

        imprimir_titulo(truncar_texto(posicion[1], max(10, ancho - 2)))
        pesos_columnas = [1, 1, 2]
        primera_row = construir_row_columnas(
            [
                f"\033[36mID:\033[0m {posicion[0]}",
                f"\033[36mStatus:\033[0m {posicion[5]}",
                f"\033[36mFecha Inicio/Final:\033[0m {posicion[3].strftime('%d/%m/%Y')} - {posicion[4].strftime('%d/%m/%Y')}",
            ],
            ancho,
            pesos_columnas
        )
        print(primera_row)
        imprimir_bloque_centrado(
            f"\033[36mIntegrantes Asignados:\033[0m {integrantes_formateados}",
            ancho
        )
        print("")
        print("\033[36mDescripcion:\033[0m")
        print(textwrap.fill(str(posicion[2]), width=max(20, ancho - 2)))
        print()
