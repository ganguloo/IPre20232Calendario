from datetime import datetime, timedelta
from parametros.parametros import FECHAS_PROHIBIDAS_GENERAL

def generacion_calendario(mes_inicial=3,
                          dia_inicial=6,
                          ano=2023,
                          dias_prohibidos=FECHAS_PROHIBIDAS_GENERAL):
    fecha_calendario = datetime(ano, mes_inicial, dia_inicial)
    fechas = dict()
    fechas_validas = dict()
    mapeo_fechas = dict()
    for indice in range(0, 117):
        if fecha_calendario.strftime("%d-%b") not in dias_prohibidos:
            dia = fecha_calendario.strftime("%d-%b")
            fechas[dia] = fecha_calendario
            fechas_validas[indice] = dia
        mapeo_fechas[indice] = fecha_calendario.strftime("%d-%b")
        fecha_calendario += timedelta(days=1)

    return fechas_validas, mapeo_fechas, fechas
