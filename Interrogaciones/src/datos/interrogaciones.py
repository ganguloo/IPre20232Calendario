
def organizacion_datos_interrogaciones(mapeo_fechas, path):
    with open(path, 'r', encoding="utf-8") as file:
        archivo = [i.strip() for i in file.readlines()]
        fechas_actualizado = []

        for i in archivo:
            if "x" not in i:
                continue
            a = i.replace("[", ",").replace("]", ",")
            a = a.split(",")
            sigla = a[1]
            interrogacion = a[3]
            fechas_actualizado.append([sigla, int(a[2]), interrogacion])
        fechas_actualizado.sort(key=lambda x: int(x[1]))
        for indice, i in enumerate(fechas_actualizado):
            fechas_actualizado[indice][1] = mapeo_fechas[int(i[1])]

    return fechas_actualizado


def interrogaciones_mes(mes, fechas_interrogaciones, fechas):
    interrogaciones_del_mes = []
    for curso in fechas_interrogaciones:
        if mes in curso[1]:
            date = fechas[curso[1]].date()
            texto = f"I{curso[2]} : {curso[0]}"
            interrogaciones_del_mes.append((date, texto))

    return interrogaciones_del_mes
