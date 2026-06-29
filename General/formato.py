import shutil


def obtener_medidas_terminal():
    return shutil.get_terminal_size(fallback=(120, 30))


def obtener_ancho_terminal(minimo=60):
    columnas = obtener_medidas_terminal().columns
    return max(minimo, columnas)


def truncar_texto(texto, ancho):
    texto = str(texto)
    if ancho <= 0:
        return ""
    if len(texto) <= ancho:
        return texto
    if ancho <= 3:
        return texto[:ancho]
    return texto[:ancho - 3] + "..."


def _normalizar_columnas(columnas):
    columnas_normalizadas = []
    for columna in columnas:
        columnas_normalizadas.append({
            "titulo": columna.get("titulo", ""),
            "clave": columna.get("clave"),
            "min": max(1, columna.get("min", len(columna.get("titulo", "")) + 2)),
            "peso": max(1, columna.get("peso", 1)),
        })
    return columnas_normalizadas


def _calcular_anchos(columnas, ancho_total):
    separadores = len(columnas) - 1
    ancho_disponible = max(len(columnas), ancho_total - separadores)
    ancho_minimo = sum(columna["min"] for columna in columnas)

    if ancho_minimo >= ancho_disponible:
        return [columna["min"] for columna in columnas]

    ancho_restante = ancho_disponible - ancho_minimo
    peso_total = sum(columna["peso"] for columna in columnas)
    anchos = [columna["min"] for columna in columnas]

    for indice, columna in enumerate(columnas):
        extra = (ancho_restante * columna["peso"]) // peso_total
        anchos[indice] += extra

    diferencia = ancho_disponible - sum(anchos)
    indice = 0
    while diferencia > 0:
        anchos[indice] += 1
        diferencia -= 1
        indice = (indice + 1) % len(anchos)

    return anchos


def _formatear_fila(valores, anchos):
    celdas = []
    for indice, valor in enumerate(valores):
        celdas.append(truncar_texto(valor, anchos[indice]).ljust(anchos[indice]))
    return " ".join(celdas)


def imprimir_titulo(titulo):
    ancho = obtener_ancho_terminal()
    print("\n" + "=" * ancho)
    print(str(titulo).center(ancho))
    print("=" * ancho)


def imprimir_tabla(columnas, filas):
    columnas = _normalizar_columnas(columnas)
    ancho = obtener_ancho_terminal()
    anchos = _calcular_anchos(columnas, ancho)

    encabezados = [columna["titulo"] for columna in columnas]
    print(_formatear_fila(encabezados, anchos))
    print("-" * ancho)

    for fila in filas:
        if isinstance(fila, dict):
            valores = [fila.get(columna["clave"], "") for columna in columnas]
        else:
            valores = list(fila)
        print(_formatear_fila(valores, anchos))

    print("")
