# ProyectoPythonLigaClasificacion
El programa debe mostrar finalmente la clasificación completa de la liga indicando para cada equipo el número de partidos ganados empatados y perdidos así como los puntos totales obtenidos. Para lograr esto se deben construir varias funciones que trabajarán de manera conjunta.

La función LeerPartidos se encargará de leer el archivo liga.csv y devolver su contenido en forma de una lista de diccionarios donde cada diccionario representa un partido. La función impClasificacion recibirá esa lista y generará la clasificación final mostrándola por pantalla. Para poder hacerlo utilizará varias funciones auxiliares. La función Equipos recibirá la lista de partidos y devolverá un conjunto con todos los equipos que participan en la liga. La función InfoEquipos recibirá la lista de partidos y el conjunto de equipos y calculará para cada uno de ellos cuántos partidos ha ganado empatado o perdido así como los puntos totales obtenidos. Para realizar estos cálculos usará la función QuienGana que determinará si un resultado corresponde a una victoria del equipo local del visitante o a un empate y también usará la función Puntos que calculará la puntuación total de cada equipo a partir del número de victorias empates y derrotas. Finalmente la función Clasificacion ordenará los equipos según los puntos obtenidos y generará la clasificación final.

A continuación se deja un espacio para asignar a cada miembro del grupo la responsabilidad de una función concreta. Es importante que esta información se complete antes de comenzar el desarrollo del proyecto para organizar correctamente el trabajo.

Reparto de tareas
LeerPartidos() –Rubén
impClasificacion() –Jesús
Equipos() –Rubén
InfoEquipos() –Jesús
QuienGana() –Rubén
Puntos() –Jesús
Clasificacion() –Rubén y Jesús
