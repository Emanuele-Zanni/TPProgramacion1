# Aplicación de seguimiento de proyectos

Aplicación de consola desarrollada en Python para administrar proyectos,
tareas, integrantes, usuarios y roles. Es un trabajo práctico de
Programación 1 y conserva listas de listas como estructura principal para
proyectos, tareas y roles.

## Estado actual

El sistema permite:

- iniciar sesión y registrar usuarios;
- crear, consultar, modificar y eliminar proyectos;
- transferir el ownership de un proyecto;
- agregar y quitar integrantes de un proyecto;
- crear, consultar, modificar, eliminar y asignar tareas;
- administrar integrantes y niveles de acceso;
- realizar un CRUD completo de roles;
- consultar tareas por proyecto, estado y responsable;
- obtener estadísticas de proyectos, tareas, integrantes y roles;
- guardar y recuperar información mediante JSON y un archivo de texto;
- ejecutar 24 pruebas automáticas con `pytest`.

El programa no utiliza clases, base de datos, frameworks ni librerías externas
durante su ejecución normal.

## Datos académicos pendientes

- Número de grupo: pendiente de completar.
- Integrantes: pendiente de completar por el equipo.
- Enlace al video: pendiente de completar.
- Informe `.docx`: pendiente de incorporar.

Estos datos no se deducen de los autores de Git porque autores y miembros del
grupo no necesariamente representan lo mismo.

## Requisitos

- Python 3.13. El proyecto fue verificado con Python 3.13.7.
- `pytest` solamente para ejecutar la suite de pruebas.

Instalación de la dependencia de desarrollo:

```powershell
python -m pip install -r requirements-dev.txt
```

Si `python` no está agregado al `PATH`, en el equipo usado para desarrollar el
proyecto se puede ejecutar:

```powershell
C:\Users\emaza\AppData\Local\Programs\Python\Python313\python.exe -m pip install -r requirements-dev.txt
```

## Ejecución

La aplicación debe iniciarse desde la raíz del repositorio porque las rutas de
persistencia son relativas a esa carpeta.

```powershell
python main.py
```

Comando correspondiente al entorno de desarrollo actual:

```powershell
C:\Users\emaza\AppData\Local\Programs\Python\Python313\python.exe main.py
```

El punto de entrada es `main.py`. La ejecución está protegida mediante:

```python
if __name__ == "__main__":
    ejecutar()
```

Por este motivo, importar `main` desde una prueba o desde otro módulo no inicia
los menús interactivos.

## Credenciales iniciales

Cuando `data/datos.json` no contiene usuarios, el programa crea:

| Usuario | Contraseña | Nivel de acceso |
|---|---|---:|
| `admin` | `1234` | 3 |
| `manager` | `5555` | 2 |
| `integrante` | `123` | 1 |

Son credenciales académicas de demostración. El archivo JSON es persistente,
por lo que puede contener usuarios y proyectos adicionales creados durante el
uso del programa.

Los roles iniciales, cuando `data/roles.txt` está vacío, son:

```text
1|Desarrollador
2|QA
```

## Menú y permisos

### Nivel 1 — Integrante

- consultar proyectos;
- abrir un proyecto y consultar sus tareas;
- consultar la lista de integrantes.

### Nivel 2 — Manager

- todas las operaciones del nivel 1;
- crear, editar y eliminar proyectos;
- transferir el ownership de un proyecto a un manager disponible;
- crear, editar, eliminar y asignar tareas;
- gestionar integrantes de un proyecto;
- editar integrantes;
- consultar roles.

### Nivel 3 — Administrador

- todas las operaciones anteriores;
- registrar usuarios indicando su nivel de acceso;
- eliminar integrantes que no tengan proyectos asociados;
- crear, editar y eliminar roles;

Los menús verifican `credencial["clearance"]` antes de mostrar y ejecutar
operaciones restringidas.

La aplicación utiliza normalmente los niveles 1, 2 y 3. El formulario
administrativo admite técnicamente el valor 0, pero no existe una cuenta
inicial ni un perfil funcional documentado para ese nivel.

## Menú principal

```text
1. Proyectos
2. Personal
3. Estadísticas
4. Cerrar sesión
0. Cerrar programa
```

La consola se limpia antes de mostrar cada menú principal. Los títulos y
breadcrumbs se muestran en amarillo mediante códigos ANSI.

## Modelo de datos

Los índices oficiales están centralizados en `General/constantes.py`. No se
debe interpretar un ID como una posición dentro de una lista.

### Proyecto

Estructura en memoria:

```text
[0] ID
[1] Nombre
[2] Lista de tareas
[3] Fecha de inicio (datetime)
[4] Fecha final (datetime)
[5] Estado
[6] IDs de integrantes
[7] ID del owner
```

Representación:

```python
[
    id,
    nombre,
    tareas,
    fecha_inicio,
    fecha_final,
    estado,
    integrantes_ids,
    owner_id,
]
```

### Tarea

Las tareas están anidadas en la posición `[2]` del proyecto al que pertenecen.

```text
[0] ID
[1] Nombre
[2] Descripción
[3] Fecha de inicio (datetime)
[4] Fecha final (datetime)
[5] Estado
[6] Integrantes asignados
```

Cada integrante asignado se guarda de forma normalizada:

```python
{"id": usuario_id, "nombre": nombre_visible}
```

### Rol

```text
[0] ID
[1] Nombre
```

El nombre del rol asignado dentro de un proyecto se almacena en la relación del
usuario con ese proyecto.

### Usuario/integrante

Los usuarios se almacenan en un diccionario cuya clave es el nombre de acceso:

```python
{
    "usuario": {
        "id": 1,
        "password": "contraseña",
        "clearance": 1,
        "projects": [
            {
                "projectId": 1,
                "rol": "Desarrollador",
                "tareas": [1, 2]
            }
        ]
    }
}
```

El diccionario resuelve autenticación y relaciones. Proyectos, tareas y roles
continúan usando matrices/listas de listas.

## Estados válidos

Los estados son tuplas inmutables definidas en `General/constantes.py`:

```python
ESTADOS_PROYECTO = ("Activo", "Completado", "Expirado")
ESTADOS_TAREA = ("Activo", "Completado", "Expirado")
```

Las funciones de lógica rechazan estados fuera de esas tuplas.

## IDs y búsquedas

`General/utilidades.py` implementa:

- `buscar_posicion_por_id()`: búsqueda secuencial con `while`;
- `obtener_proximo_id()`: mayor ID existente más uno;
- `ids_duplicados()`: detección mediante conjuntos.

Eliminar un registro intermedio no cambia los IDs restantes y no provoca que
el siguiente alta reutilice accidentalmente un ID.

## Validaciones

`General/validaciones.py` concentra las validaciones reutilizables:

- fechas con formato `dd/mm/aaaa`;
- existencia real de la fecha mediante `datetime.strptime`;
- fecha final no anterior a fecha inicial;
- nombres;
- nombres de usuario;
- contraseñas;
- estados;
- enteros y confirmaciones.

Patrones utilizados:

```python
PATRON_FECHA = r"^\d{2}/\d{2}/\d{4}$"
PATRON_NOMBRE = r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9][A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9 _.-]{1,59}$"
PATRON_USUARIO = r"^[a-zA-Z][a-zA-Z0-9_.]{2,24}$"
```

`General/inputFecha.py` es la única entrada interactiva de fechas y reutiliza
la validación centralizada.

## Integridad de relaciones

El sistema aplica estas reglas:

- un proyecto con tareas no puede eliminarse;
- un integrante asociado a proyectos no puede eliminarse;
- un rol asignado no puede eliminarse;
- al eliminar una tarea se quita su ID de las relaciones de los usuarios;
- al eliminar un proyecto se eliminan sus relaciones en los usuarios;
- una tarea solo puede asignarse a integrantes del proyecto;
- la asignación se sincroniza entre la tarea y el registro del usuario;
- los IDs de proyectos, tareas, roles y usuarios son independientes de la
  posición física en las colecciones.

## Persistencia

### JSON

Archivo: `data/datos.json`

Contiene un único objeto:

```json
{
    "proyectos": [],
    "usuarios": {}
}
```

Proyectos, tareas y usuarios se guardan en JSON. Las fechas, que son objetos
`datetime` en memoria, se convierten a texto `dd/mm/aaaa` al guardar y se
reconstruyen al cargar.

La implementación utiliza:

- `json.load()`;
- `json.dump()`;
- `indent=4`;
- `ensure_ascii=False`;
- `with`;
- `encoding="utf-8"`.

Se manejan archivos inexistentes, JSON mal formado, permisos y errores del
sistema operativo. Un JSON inválido impide iniciar el programa para evitar
sobrescribir información dañada.

### Archivo plano

Archivo: `data/roles.txt`

Formato:

```text
id|nombre
```

Los roles tienen CRUD persistente completo:

- `cargar_roles_txt`;
- `guardar_roles_txt`;
- `crear_rol_txt`;
- `buscar_rol_txt`;
- `modificar_rol_txt`;
- `eliminar_rol_txt`.

Las líneas vacías o inválidas se ignoran durante la carga.

### Momento de guardado

Los datos se cargan al iniciar. Se guardan:

- después de las operaciones CRUD de los menús principales;
- al volver del proyecto seleccionado, incluyendo los cambios en sus tareas;
- al volver de los submenús principales;
- al cerrar sesión;
- al cerrar el programa.

## Consultas relacionadas

Desde `Estadísticas > Consultas relacionadas` se puede consultar:

- tareas de un proyecto;
- tareas por estado;
- tareas por responsable.

`General/consultas.py` también obtiene integrantes únicos de un proyecto
combinando integrantes directos y responsables de tareas.

## Estadísticas

El menú de estadísticas incluye:

1. estadísticas de proyectos;
2. estadísticas de integrantes;
3. estadísticas de roles;
4. resumen ejecutivo;
5. consultas relacionadas.

Los cálculos incluyen:

- totales generales;
- proyectos y tareas por estado;
- tareas por proyecto e integrante;
- tareas activas, completadas, expiradas, vencidas y sin asignar;
- porcentaje de tareas completadas y activas;
- porcentaje de proyectos activos;
- promedio de tareas por proyecto e integrante;
- proyectos e integrantes con mayor y menor cantidad de tareas;
- empates en máximos y mínimos;
- progreso y duración de proyectos;
- ownerships y carga de trabajo.

Las listas vacías devuelven valores cero y no producen divisiones por cero.

## Programación funcional y estructuras

El proyecto usa de manera efectiva:

- `lambda` para ordenamientos, filtros y transformaciones breves;
- `map` para transformar nombres e IDs;
- `filter` para consultas por estado y responsable;
- `reduce` para acumulaciones estadísticas;
- comprensiones de listas y diccionarios;
- slicing para copias y truncado;
- conjuntos para evitar integrantes repetidos y detectar IDs duplicados;
- tuplas para estados inmutables;
- diccionarios para usuarios, relaciones y agrupaciones estadísticas.

## Recursividad

`Recursividad/funciones.py` implementa:

1. `buscar_por_id_recursivo`;
2. `contar_tareas_proyecto_recursivo`;
3. `contar_tareas_estado_recursivo`;
4. `obtener_nombres_recursivo`.

Estas funciones tienen caso base, caso recursivo, avance hacia el caso base y
retorno definido. Se utilizan en consultas, normalización de nombres y
estadísticas.

## Manejo de excepciones

Se capturan específicamente, según la operación:

- `ValueError`;
- `TypeError`;
- `FileNotFoundError`;
- `PermissionError`;
- `OSError`;
- `json.JSONDecodeError`.

No se utilizan bloques `except:` genéricos.

## Presentación

`General/formato.py` proporciona:

- títulos;
- tablas alineadas;
- cálculo de ancho según la terminal;
- truncado de texto mediante slicing.

`General/mostrarTareasProyectos.py` presenta el detalle de proyectos y tareas,
incluyendo fechas, estado, progreso, responsables y descripción.

## Estructura del repositorio

```text
TPProgramacion1/
├── main.py
├── README.md
├── PRUEBAS_MANUALES.md
├── pytest.ini
├── requirements-dev.txt
├── Database/
│   └── usuarios.py
├── General/
│   ├── clearConsole.py
│   ├── constantes.py
│   ├── consultas.py
│   ├── formato.py
│   ├── inputFecha.py
│   ├── logica.py
│   ├── mostrarTareasProyectos.py
│   ├── persistencia.py
│   ├── utilidades.py
│   └── validaciones.py
├── Integrantes/
│   ├── funciones.py
│   ├── menus.py
│   └── roles.py
├── Proyectos/
│   ├── funciones.py
│   └── menus.py
├── Recursividad/
│   ├── __init__.py
│   └── funciones.py
├── Stats/
│   ├── funciones.py
│   └── menu.py
├── Tareas/
│   └── funciones.py
├── data/
│   ├── datos.json
│   └── roles.txt
└── tests/
    ├── test_archivos.py
    ├── test_consultas_estadisticas.py
    ├── test_crud.py
    ├── test_recursividad.py
    └── test_validaciones.py
```

## Pruebas automáticas

Ejecución:

```powershell
python -m pytest
python -m pytest -v
```

En el entorno de desarrollo:

```powershell
C:\Users\emaza\AppData\Local\Programs\Python\Python313\python.exe -m pytest -v
```

Estado verificado:

```text
24 tests collected
24 passed
```

Cobertura conceptual:

- fechas válidas e inválidas;
- regex de nombres y usuarios;
- estados inválidos;
- rangos de fechas;
- CRUD de proyectos y tareas;
- creación, búsqueda y protección de bajas de integrantes relacionados;
- CRUD completo de roles en archivo de texto;
- búsqueda de IDs inexistentes;
- próximo ID después de bajas;
- protección de relaciones;
- lectura y escritura JSON;
- archivo JSON inexistente o mal formado;
- CRUD de roles en TXT;
- líneas TXT inválidas;
- consultas relacionadas;
- estadísticas con datos, listas vacías y empates;
- cuatro funciones recursivas.

Las pruebas de archivos usan `tmp_path`, por lo que no modifican
`data/datos.json` ni `data/roles.txt`.

Los 62 recorridos manuales requeridos se encuentran en
`PRUEBAS_MANUALES.md`.

## Repositorio

Remoto configurado:

```text
https://github.com/Emanuele-Zanni/TPProgramacion1
```

Antes de entregar se debe comprobar que:

- el enlace sea público o tenga permisos para el docente;
- la rama entregada sea la correcta;
- el historial incluya commits descriptivos;
- los datos académicos, video e informe estén completos;
- no se incluyan entornos virtuales, cachés ni archivos temporales.
