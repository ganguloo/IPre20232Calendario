import pandas as pd

cursos = pd.read_csv('datos/cursos.csv')['nombre'].tolist()
salas = pd.read_csv('datos/salas.csv')['nombre'].tolist()
