# To Do:

- Modulo de Stats (determinar que stats son pertinentes para cada seccion).
Stats va a dividirse por cada modulo (Stats de proyectos, Stats de integrantes, etc). Verificar que las stats sean pertinentes y no crear stats por crear (verificar logica del negocio).

- Aplicar todos los requisitos del CHECKLIST

- Normalizar todas las cosas que hagan falta normalizar (Textos, estilos, prints, etc)

- Upgradear la logica de TAREAS (agregar descripcion para tareas , mejorar el print de tareas mostrando title y desc??). aGREGAR TAMBIEN reloj interno para determinar cuando expira o no (automaticamente cambiar el estado. Agregar esstados a tarea y modificaciones)
- Estados de tarea: Completado, Pendiente/InProgress, Expirado/DueDate,

- Upgradear y normalizar prints de las listas? Agregar sistema de logs de todas las tareas/proyectos/integrantes???

- Validaciones de fecha para los inputs de fecha en proyecto y tareas

- asignar tarea a persona (falta funcion)

# Bugs

- el de Candela de login con ucuenta creada e intento de acceso a proyectos (ver proyectos o crea proyecto)

# Corto Plazo -----

[Menu Principal > Ver personal > *Roles*] FUNCIONA MAL, verificar inputs,se rompe con vacios, se estqa convirtiendo a "int"

Agregar el CRUD de Tareas dentro de seleccionar Proyecto (agregar mismas validaciones y fixes de los demas modulos)

Agregar lambdas (min 2) 

Agergar LOGIN y USERS (minimo 2 lvls, user y superUser) [Invitado?, Integrante, Manager, SuperUser/Developer/Admin]

- stats de proyectos: 
    cantidad de proyectos total (en marcha, terminados, cancelados, entre otros)
    cantidad de tiempo que lleva en proceso el proyecto

- stats de tareas: lo mismo que stats proyectos 
- stats personal: 
    cantidad de proyectos y tareas a los que fue asigando
    cantidad de proyectos y tareas completadas
    cantidad de tiempo invertido en cada proyecto o tarea


# Cosas de Clase -----
# Cosas de Clase / CHECKLIST -----

HACER VIDEO (chequear consignas) ||| Grabar pantalla, uno habla y el otro ejecuta codigo? repartir tiempos y partes

Extraer archivo de checklist (en carpeta TPO)

# Preguntas
json, se puede aplicar
si modficamos las matrices a diccionarios
cuantas tuplas hay q aplicar, danos ejemplos a como aplicar tuplas, conjuntos
como va a ser el parcial 


no toma git
nos da un código breve, q devuelve el código, q representa un valor dentro de una matriz, o q cambiar para q devuelve, cual es el valor q toma la variable, q hace tal metodo de un diccinario/tupla/cadena, q es sorted, slicing, iteración de diccionarios listas, listas x comrpension en sus 3 versiones (if, else elif), split, upper, lower de cadenas, funcion map aplicado a lambda, filter aplicado a lambda
expresiones regulares
