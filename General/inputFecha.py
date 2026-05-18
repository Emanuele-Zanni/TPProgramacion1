from datetime import datetime
from General.clearConsole import clearConsole

def inputFecha(nombreProyecto,mode, FechaInicio=None):
    on = True
    fecha_texto = ""
    while on:
        clearConsole()
        print("[Menu Principal > Proyectos > *Crear Proyectos*]")
        print()
        print(f"Nombre del Proyecto: {nombreProyecto}")

        if FechaInicio != None:
            print(f"Fecha de Inicio: {FechaInicio}")
            
        if mode == "Inicio" or mode == "inicio":
            fecha_texto = input("• Ingrese la fecha de inicio del proyecto (DD/MM/YYYY): ")
        elif mode == "Final" or mode == "final":
            fecha_texto = input("• Ingrese la fecha de finalizacion del proyecto (DD/MM/YYYY): ")

        if fecha_texto == "X" or fecha_texto == "x":
            on = False 
            return fecha_texto
        else:
            try:
                fecha = datetime.strptime(fecha_texto, "%d/%m/%Y").strftime("%d/%m/%Y")
                input(f"Fecha válida == {fecha}")

                return fecha

            except ValueError:
                input("Formato inválido ")

        