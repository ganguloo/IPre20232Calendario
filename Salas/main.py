from gurobipy import GRB, Model, quicksum
from carga_datos.cursos import curso
from carga_datos.salas import capacidad_salas
from grafo_salas import crear_grafo
import os
import networkx as nx

path_nodos = os.path.join('Datos', "Salas SJ 2023-07-13.xlsx")
path_edges = os.path.join('Datos', "datos grafo salas.xlsx")
G = crear_grafo(path_edges, path_nodos)
m = Model()
m.setParam("TimeLimit", 600)

# SETS

C = range(1, 5 + 1)  # curso
S = range(1, 196) # salas
S_1 = range(1, 196) # salas auxiliar


# IMPORT PARAMS
nombres = curso("nombres")
vacantes = curso("vacantes")
particion_maxima = curso("particion")
capacidad = capacidad_salas("capacidad")
nombre_sala = capacidad_salas("name")


# PARAMS
Vacantes = {(c): vacantes[c - 1] for c in C}
Particion = {(c): particion_maxima[c - 1] for c in C}
Tamano = {(s): capacidad[s - 1] for s in S}
Distancia = {}


# Coloque aca sus variables
X = m.addVars(C, S, vtype=GRB.BINARY, name="X_cs")  # Si el curso c utiliza la sala s
Y = m.addVars(C, S, S_1, vtype=GRB.BINARY, name="Y_cs1s2")  # Si el cursos c utiliza las salas s1 y s2
m.update()

# Evitar que un cuirso sea dividido en muchas salas chicas
m.addConstrs((quicksum(X[c, s] for s in S) <= Particion[c] for c in C), name="Granularidad")

# Relación de variables
m.addConstrs((X[c, s1] + X[c, s2] <= Y[c, s1, s2] + 1 for c in C for s1 in S for s2 in S_1 if (s1 != s2)), name="Relacion")

m.addConstrs((quicksum(X[c, s] for c in C) <= 1  for s in S), name="Relacion_2")

# Todos los alumnos deben ser asignados a alguna sala respetando las capacidades de una prueba (mitad)
m.addConstrs((quicksum(X[c, s] * capacidad[s] for s in S) >= 2 * Vacantes[c] for c in C), name="Asignacion")

m.update()
# nx.shortest_path_length(G,source=s1,target=s2)
objetivo = quicksum(quicksum(nx.shortest_path_length(G, source=nombre_sala[s1], target=nombre_sala[s2])* Y[c, s1, s2] for s1 in S for s2 in S if (s1 != s2)) for c in C)
m.setObjective(objetivo, GRB.MINIMIZE)
m.optimize()
valor_objetivo = m.ObjVal

# Muestra los valores de las soluciones
print("\n"+"-"*10+" Manejo Soluciones "+"-"*10)

for c in C:
    for s in S:
        if X[c, s].x == 1:
            print(f"EL curso {nombres[c]} utiliza la sala {nombre_sala[s]}")
