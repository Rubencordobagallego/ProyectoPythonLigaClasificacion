import csv

def leerpartidos():
    partidos = []
    f = open("liga.csv", "r", encoding="utf-8")
    lector = csv.reader(f)
    next(lector)
    for fila in lector:
        gl1, gv1 = fila[3].split("-")
        gl2, gv2 = fila[4].split("-")
        gl = int(gl1) + int(gl2)
        gv = int(gv1) + int(gv2)
        partidos.append((fila[1], fila[2], gl, gv))
    f.close()
    return partidos


def equipos(partidos):
    e = {}
    for p in partidos:
        if p[0] not in e:
            e[p[0]] = [0, 0, 0, 0]
        if p[1] not in e:
            e[p[1]] = [0, 0, 0, 0]
    return e


def infosequipos(equipos):
    return equipos


def quiengana(partido):
    if partido[2] > partido[3]:
        return "local"
    elif partido[2] < partido[3]:
        return "visitante"
    else:
        return "empate"


def puntos(equipos, partido):
    r = quiengana(partido)
    local, visitante = partido[0], partido[1]

    if r == "local":
        equipos[local][0] += 1
        equipos[local][3] += 3
        equipos[visitante][1] += 1
    elif r == "visitante":
        equipos[visitante][0] += 1
        equipos[visitante][3] += 3
        equipos[local][1] += 1
    else:
        equipos[local][2] += 1
        equipos[visitante][2] += 1
        equipos[local][3] += 1
        equipos[visitante][3] += 1


def clasificacion(equipos):
    return sorted(equipos.items(), key=lambda x: x[1][3], reverse=True)


def impclasificacion(clasificacion):
    print("#  Equipo                |  PG  |  PP  |  PE  | PTS |")
    print("----------------------------------------------------")
    i = 1
    for equipo, d in clasificacion:
        print(f"| {i:<3} | {equipo:<16} | {d[0]:<4} | {d[1]:<4} | {d[2]:<4} |  {d[3]} |")
        i += 1


partidos = leerpartidos()
e = equipos(partidos)
infosequipos(e)

for p in partidos:
    puntos(e, p)

c = clasificacion(e)
impclasificacion(c)