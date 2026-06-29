# Pruebas manuales

Ejecutar con:

```powershell
C:\Users\emaza\AppData\Local\Programs\Python\Python313\python.exe main.py
```

## Login

1. `admin / 1234`: debe abrir el menú principal.
2. `admin / incorrecta`: debe rechazar la contraseña.
3. Usuario inexistente: debe informar que no existe.
4. Campos vacíos: deben ser rechazados sin cerrar el programa.

## Proyectos

5. Crear con nombre y fechas válidas: debe asignar un ID único.
6. Nombre vacío: debe repetir el ingreso.
7. Fecha inexistente, por ejemplo `31/02/2026`: debe rechazarla.
8. Fecha final anterior: debe rechazarla.
9. Modificar nombre: solo debe cambiar el índice de nombre.
10. Modificar fechas: debe conservar inicio menor o igual que fin.
11. Modificar estado: la fecha final debe permanecer intacta.
12. Seleccionar un ID existente: debe mostrar el proyecto.
13. Seleccionar un ID inexistente: debe informar el error una sola vez.
14. Eliminar proyecto vacío: debe eliminarlo.
15. Eliminar proyecto con tareas: debe bloquear la baja.

## Tareas y relaciones

16. Crear una tarea válida: debe generar siete campos.
17. Las tareas solo pueden crearse dentro de un proyecto seleccionado.
18. Solo deben asignarse usuarios integrantes del proyecto.
19. Editar nombre, descripción, fechas y estado: cada campo debe conservarse.
20. Repetir el punto anterior después de eliminar una tarea intermedia.
21. Consultar por estado desde Estadísticas > Consultas relacionadas.
22. Consultar tareas de un proyecto.
23. Consultar tareas de un responsable.
24. Eliminar una tarea: debe desaparecer de la matriz y de las relaciones.

## IDs

25. Crear tres registros y eliminar el segundo.
26. Crear un cuarto registro.
27. El nuevo ID debe ser el mayor existente más uno.
28. Los IDs anteriores deben continuar siendo localizables.

## Archivo plano

29. Iniciar con `data/roles.txt`: debe cargar sus roles.
30. Renombrar temporalmente el archivo: debe crear uno vacío.
31. Crear un rol: debe agregar una línea `id|nombre`.
32. Editarlo: debe reescribir la línea.
33. Eliminarlo: debe reescribir el archivo sin esa línea.
34. Agregar una línea inválida: debe ignorarla al cargar.
35. Quitar permisos de escritura: debe mostrarse un error de archivo.

## JSON

36. Iniciar con JSON válido: debe cargar usuarios y proyectos.
37. Sin archivo: debe crear la estructura inicial.
38. Archivo vacío: debe impedir el inicio e informar el error.
39. JSON mal formado: debe impedir el inicio sin sobrescribirlo.
40. Crear un proyecto y volver al menú: debe quedar guardado.
41. Modificarlo y volver: debe quedar actualizado.
42. Eliminarlo y volver: debe desaparecer del archivo.
43. Reiniciar: los datos deben recuperarse con fechas convertidas.

## Estadísticas

44. Con datos: los totales deben coincidir con las matrices.
45. Sin datos: los totales, porcentajes y promedios deben ser cero.
46. No debe ocurrir `ZeroDivisionError`.
47. Dos entidades empatadas deben aparecer juntas en máximos y mínimos.

## Recursividad

48. Ejecutar cada función con lista vacía.
49. Ejecutarla con un registro.
50. Ejecutarla con varios registros.
51. Buscar un ID inexistente: debe devolver `-1`.
52. Verificar que el índice aumente en cada llamada recursiva.

## Pruebas automáticas

53. Ejecutar `python -m pytest`.
54. Ejecutar `python -m pytest -v`.
55. Confirmar que los tests de archivo usan `tmp_path`.
56. Ejecutar dos veces: el resultado debe ser independiente.
57. Verificar casos de validación, CRUD, error, archivos, estadísticas y recursión.

## Menús

58. Recorrer todas las opciones visibles según el nivel de acceso.
59. Ingresar letras y opciones fuera de rango.
60. Usar `0` para volver en cada nivel.
61. Cerrar sesión y luego cerrar el programa.
62. Acceder a Roles como manager: no debe producir un ciclo infinito.
