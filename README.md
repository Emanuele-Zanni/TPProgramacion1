# TPProgramacion1

Aplicacion de consola en Python para administrar proyectos, tareas e integrantes. El proyecto esta organizado por modulos y hoy funciona con datos en memoria, sin persistencia en base de datos o archivos.

## Estado actual

El proyecto se encuentra en desarrollo. Ya existe un flujo navegable por menus para:

- iniciar sesion
- ver y gestionar proyectos
- ver y gestionar tareas dentro de un proyecto
- ver y gestionar integrantes
- gestionar roles

Tambien hay validaciones basicas de entrada en varios formularios, pero todavia hay partes marcadas como `WIP` y varias mejoras pendientes.

## Tecnologias

- Python
- consola interactiva con `input()` y `print()`
- organizacion modular por carpetas

No hay dependencias externas declaradas actualmente.

## Estructura del proyecto

```text
TPProgramacion1/
|-- main.py
|-- Database/
|   `-- usuarios.py
|-- General/
|   |-- clearConsole.py
|   `-- inputFecha.py
|-- Integrantes/
|   |-- funciones.py
|   |-- menus.py
|   `-- roles.py
|-- Proyectos/
|   |-- funciones.py
|   `-- menus.py
|-- Tareas/
|   |-- funciones.py
|   `-- menus.py
|-- todo.md
`-- COMANDOS_PARA_PUSHEAR.md
```

## Modulos principales

### `main.py`

Punto de entrada de la aplicacion. Inicializa datos mockeados y muestra el menu principal:

- `1. Ver Proyectos`
- `2. Ver Personal`
- `3. Stats (WIP)`
- `4. Cerrar sesion`
- `0. Cerrar Programa`

### `Database/usuarios.py`

Contiene:

- usuarios mockeados
- contrasenas mockeadas
- niveles de acceso (`clearance`)
- funcion `login()`

Hoy los usuarios se construyen en memoria a partir de listas:

- `Candela / 1234`
- `Emanuele / 5555`

## Datos mockeados actuales

La aplicacion arranca con datos de prueba cargados en `main.py`.

### Proyectos

Se crean 4 proyectos de ejemplo en memoria al iniciar:

- `Proyecto 1`
- `Proyecto 2`
- `Proyecto 3`
- `Proyecto 4`

Cada proyecto sigue esta estructura:

```python
[id, nombreProyecto, tareas, fechaInicio, fechaFinal, estado]
```

### Integrantes

Actualmente hay un integrante de ejemplo:

```python
[1, "Emanuele", "rol", "TareasAsignadas"]
```

### Roles

La lista de roles inicia vacia:

```python
ListaRoles = []
```

## Funcionalidades implementadas

### Login

El sistema pide:

- nombre de usuario
- contrasena

La validacion de contrasena usa `get()` para evitar errores cuando el usuario no existe.

### Proyectos

Menu disponible en `Proyectos/menus.py`.

Segun el tipo de acceso, el usuario puede ver:

- menu basico:
  - ver proyectos
  - seleccionar proyecto
- menu extendido:
  - ver proyectos
  - seleccionar proyecto
  - crear proyecto
  - editar proyecto
  - eliminar proyecto

Operaciones implementadas:

- listar proyectos
- seleccionar un proyecto por ID
- crear proyecto
- editar nombre, fecha de inicio, fecha final o estado
- eliminar proyecto

### Tareas

Las tareas se gestionan dentro de un proyecto seleccionado.

Operaciones implementadas:

- ver tareas
- crear tarea
- editar tarea
- eliminar tarea

La estructura actual de una tarea creada es:

```python
[id, nombreTarea, fechaInicio, fechaFinal]
```

### Integrantes

Operaciones implementadas:

- ver integrantes
- agregar integrante
- editar integrante
- eliminar integrante

### Roles

Operaciones implementadas o iniciadas:

- ver roles
- crear rol
- editar rol
- eliminar rol

## Ejecucion

Desde la raiz del proyecto:

```powershell
python main.py
```

Si tu sistema usa `py` en lugar de `python`:

```powershell
py main.py
```

## Flujo general de uso

1. Ejecutar `main.py`.
2. Iniciar sesion con un usuario mockeado.
3. Elegir una opcion del menu principal.
4. Navegar por los menus de proyectos, tareas o integrantes.

## Utilidades generales

### `General/clearConsole.py`

Limpia la consola usando:

- `cls` en Windows
- `clear` en sistemas compatibles con Unix

### `General/inputFecha.py`

Existe como modulo auxiliar para validacion de fechas, pero hoy esta incompleto y no esta integrado al flujo principal.

## Limitaciones actuales

- No hay persistencia de datos: al cerrar el programa, todo se pierde.
- Los datos se cargan manualmente como listas en memoria.
- La opcion de estadisticas todavia esta en `WIP`.
- La validacion de fechas todavia es basica y en varios casos solo verifica si el input es numerico.
- Hay funciones con comportamiento parcial o en proceso de refactor.
- La gestion de permisos existe conceptualmente mediante `clearance`, pero su uso todavia no esta completamente consolidado en toda la aplicacion.

## Archivos de apoyo

- `todo.md`: lista de pendientes funcionales y tecnicos
- `COMANDOS_PARA_PUSHEAR.md`: ayuda rapida para publicar cambios con Git
