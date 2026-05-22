def mostrar_tarea_proyecto(mode,posicion):

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
        print(f"ID: {posicion[0]} | Status: {posicion[4]} | Fecha Inicio/Final: {posicion[2].strftime('%d/%m/%Y')} - {posicion[3].strftime('%d/%m/%Y')}")
        print()