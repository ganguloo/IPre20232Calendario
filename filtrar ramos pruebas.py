import polars as pl
from datetime import datetime
import os

path_excel = os.path.join('Datos', 'Eventos Tipo Evaluaciones 20023-20 Total UC v2023-08-30.xlsx')
siglas_fis = ['FIS1514', 'FIS1523', 'FIS1533']
siglas_qim = ['QIM100E']
siglas_mat = ['MAT1610', 'MAT1620', 'MAT1630', 'MAT1640', 'MAT1203', 'EYP1113']
siglas_externas = siglas_fis + siglas_mat + siglas_qim
fecha_maxima = "6/30/2023"  # 'mes/dia/año'


def cursos_con_pruebas(path_excel, fecha_maxima, siglas):
    materias_dataframe = pl.read_excel(path_excel, sheet_name='Reservations')
    new_columns = {col: col.strip() for col in materias_dataframe.columns}
    materias_dataframe = (materias_dataframe.rename(new_columns)
                          .select(["Event Name", "Day", "Organization"]))
    # se filtra por fecha tope
    fecha_maxima = fecha_maxima.split('/')
    fecha_maxima = [int(x) for x in fecha_maxima]
    fecha_tope = datetime(fecha_maxima[2], fecha_maxima[0], fecha_maxima[1])
    lista = []
    for item in materias_dataframe.to_pandas()['Day'].values:
        item = item.split('/')
        item = [int(x) for x in item]
        lista.append(datetime(item[2], item[0], item[1]))
    nueva_col = pl.Series(lista)
    materias_dataframe.replace('Day', nueva_col)
    materias_dataframe = materias_dataframe.filter(pl.col('Day') <= fecha_tope)
    # se crea una tabla solo con otras facultades
    materias_dataframe2 = materias_dataframe.filter(~((pl.col("Organization") == 'Ingenieria') |
                                                    (pl.col("Organization") == 'Ing Matemática y Computacional') |
                                                    (pl.col("Organization") == 'Ingeniería Biológica y Médica')))
    # se seleccionan los ramos de ingenieria
    materias_dataframe = materias_dataframe.filter((pl.col("Organization") == 'Ingenieria') |
                                                   (pl.col("Organization") == 'Ing Matemática y Computacional') |
                                                   (pl.col("Organization") == 'Ingeniería Biológica y Médica'))
    # agrega los ramos de otras facultades
    for sigla in siglas:
        extra_dataframe = materias_dataframe2.filter(pl.col("Event Name").str.contains(sigla, literal=True))
        materias_dataframe = materias_dataframe.extend(extra_dataframe)
    # guarda en un excel la tabla
    materias_dataframe.to_pandas().to_excel(os.path.join('Datos', 'Datoscursos_con_pruebas.xlsx'), 'Hoja1')

    return materias_dataframe.to_pandas()


print(cursos_con_pruebas(path_excel, fecha_maxima, siglas_externas).head(10))
print(cursos_con_pruebas(path_excel, fecha_maxima, siglas_externas).tail(10))
