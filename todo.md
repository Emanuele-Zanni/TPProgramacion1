# Corto Plazo -----

Opcion Seleccionar Proyecto NO se debe poder realizar si listaProyectos es 0
- Lo mismo con Editar Proyectos
- Lo mismo con Eliminar Proyectos
- Agregar la solucion a los demas MODULOS (a los CRUDs)

LOGICA DE ROLES ESTA MAL (no consume ListaRoles, esta hardcodeado)

[Menu Principal > Ver personal > *Roles*] FUNCIONA MAL, verificar inputs,se rompe con vacios, se estqa convirtiendo a "int"

ver integrantes NO tiene un input despues de mostrar la lista.

SOLUCIONAR falta de INPUTS en TODOS los MODULOS
- Crear poryecto necestia un INPUT final msotrando mensaje "Proyecto creado exitosamente"

Agregar el CRUD de Tareas dentro de seleccionar Proyecto (agregar mismas validaciones y fixes de los demas modulos)

Agregar lambdas (min 2) 

Agergar LOGIN y USERS (minimo 2 lvls, user y superUser) [Invitado?, Integrante, Manager, SuperUser/Developer/Admin]

# Cosas de Clase -----

HACER VIDEO (chequear consignas) ||| Grabar pantalla, uno habla y el otro ejecuta codigo? repartir tiempos y partes

Extraer archivo de checklist (en carpeta TPO)

Clase posterior a 6/4 Profesor "revela" formato/modalidad del parcial

# Largo Plazo ----

Implementar libreria de Date (reemplazar el sistema casero y agregar VALIDACIONES de ser necesario)

Sistema de reordenamiento automatico de IDs al eliminar algun elemento de alguna lista (Probablemente no hace falta)

# IDEAS ----
Managers pueden ver proyectos ajenos pero NO modificarlos, solo modificarl los suyos (relacionar owner de proyecto con id de manager logueado para determinar si accede al resto de CRUD o solo tiene Read)

