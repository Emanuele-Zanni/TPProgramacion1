def mostrar_tarea_proyecto(mode,posicion):
    formatear_descripcion = lambda texto, max_caracteres=76: (
        str(texto)[:max_caracteres - 3] + "..."
        if len(str(texto)) > max_caracteres
        else str(texto)
    )

    if mode == "proyecto":
        espacios = " "*24
        print(f"{espacios}=== {posicion[1]} ===")
        print("-" * 68)
        print(f"ID: {posicion[0]} | Status: {posicion[5]} | Fecha Inicio/Final: {posicion[3].strftime('%d/%m/%Y')} - {posicion[4].strftime('%d/%m/%Y')}")
        print()

    elif mode == "tarea":
        espacios = " "*24
        print(f"{espacios}=== {posicion[1]} ===")
        print("-" * 68)
        print(f"Descripcion: {formatear_descripcion(posicion[2])}")
        print(f"ID: {posicion[0]} | Status: {posicion[5]} | Fecha Inicio/Final: {posicion[3].strftime('%d/%m/%Y')} - {posicion[4].strftime('%d/%m/%Y')}")
        print()
