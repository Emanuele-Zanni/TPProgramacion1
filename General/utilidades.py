"""Operaciones comunes sobre las matrices del sistema."""


def buscar_posicion_por_id(registros, id_buscado):
    posicion = 0
    encontrado = False
    while posicion < len(registros) and not encontrado:
        if registros[posicion][0] == id_buscado:
            encontrado = True
        else:
            posicion += 1
    return posicion if encontrado else -1


def obtener_proximo_id(registros):
    if len(registros) == 0:
        return 1
    return max(registro[0] for registro in registros) + 1


def ids_duplicados(registros):
    vistos = set()
    duplicados = set()
    for registro in registros:
        if registro[0] in vistos:
            duplicados.add(registro[0])
        vistos.add(registro[0])
    return duplicados


def truncar_texto(texto, longitud=25):
    texto = str(texto)
    if len(texto) <= longitud:
        return texto
    if longitud <= 3:
        return texto[:longitud]
    return texto[:longitud - 3] + "..."

