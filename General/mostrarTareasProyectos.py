def mostrarProyecto_Tarea(mode,Lista,posicion,id): 
    if mode == "proyecto":    
        print(f"                ===== Proyecto{id+1} ======") 
        print()
        print(f"{"ID": <5}{"Nombre": <25}{"Fecha de Inicio": <20}{"Fecha Final": <20}{"Estado": <15}")
        print("-----------------------------------------------------------------------------")
        if len(Lista[posicion][1]) > 20:
            print(f"{Lista[posicion][0]:<5}{Lista[posicion][1][:20]+ '...':<25}{Lista[posicion][3]:<20}{Lista[posicion][4]:<20}{Lista[posicion][5]:<15}")
        else:   
            print(f"{Lista[posicion][0]:<5}{Lista[posicion][1]:<25}{Lista[posicion][3]:<20}{Lista[posicion][4]:<20}{Lista[posicion][5]:<15}")
        print()
    
    elif mode == "tarea":
        print(f"                ===== Tarea{id+1} ======") 
        print()
        print(f"{"ID": <5}{"Nombre": <25}{"Fecha de Inicio": <20}{"Fecha Final": <20}{"Estado": <15}")
        print("-----------------------------------------------------------------------------")
        if len(Lista[posicion][1]) > 20 and len(Lista[posicion][2]) > 30:
            print(f"{Lista[posicion][0]:<5}{Lista[posicion][1][:20]+ '...':<25}{Lista[posicion][2][:30]+ '...':<30}{Lista[posicion][3]:<20}{Lista[posicion][4]:<20}")
        elif len(Lista[posicion][1]) > 20:
            print(f"{Lista[posicion][0]:<5}{Lista[posicion][1][:20]+ '...':<25}{Lista[posicion][2]:<30}{Lista[posicion][3]:<20}{Lista[posicion][4]:<20}")
        elif len(Lista[posicion][2]) > 30:
            print(f"{Lista[posicion][0]:<5}{Lista[posicion][1]:<25}{Lista[posicion][2][:30]+ '...':<30}{Lista[posicion][3]:<20}{Lista[posicion][4]:<20}")
        else:   
            print(f"{Lista[posicion][0]:<5}{Lista[posicion][1]:<25}{Lista[posicion][2]:<30}{Lista[posicion][3]:<20}{Lista[posicion][4]:<20}")
        print()