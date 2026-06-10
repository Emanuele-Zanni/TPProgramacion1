from datetime import datetime

def inputFecha(mode):
            
    if mode == "Inicio" or mode == "inicio":
        fecha_texto = input("• Ingrese la fecha de inicio del proyecto (DD/MM/YYYY): ")
    elif mode == "Final" or mode == "final":
        fecha_texto = input("• Ingrese la fecha de finalizacion del proyecto (DD/MM/YYYY) : ")

    if fecha_texto == "0":
         
        return fecha_texto
    
    elif fecha_texto == "":
        
        return fecha_texto
    else:
        try:
            fecha = datetime.strptime(fecha_texto, "%d/%m/%Y")

            return fecha

        except ValueError:
            
            return None

        