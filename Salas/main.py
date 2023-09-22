from gurobipy import GRB, Model, quicksum
from carga_datos.cursos import curso
from carga_datos.salas import capacidad_salas
from carga_datos.preprocessing import salas, cursos

m = Model()
m.setParam("TimeLimit", 10)

# SETS

C = range(1, 5 + 1)  # curso
S = range(1, 20 + 1) # salas
S_1 = range(1, 20 + 1) # salas auxiliar



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

# Todos los alumnos deben ser asignados a alguna sala respetando las capacidades de una prueba (mitad)
m.addConstrs((quicksum(X[c, s] * capacidad[s] for s in S) >= 2 * Vacantes[c] for c in C), name="Asignacion")

m.update()

objetivo = quicksum(quicksum(d[s1, s2] * Y[c, s1, s2] for s1 in S for s2 in S if (s1 != s2)) for c in C)
m.setObjective(objetivo, GRB.MINIMIZE)
m.optimize()
valor_objetivo = m.ObjVal

# Muestra los valores de las soluciones
print("\n"+"-"*10+" Manejo Soluciones "+"-"*10)

for c in C:
    for s in S:
        if X[c, S].x != 0:
            print(f"EL curso {nombres[c]} utiliza a sala {nombre_sala[s]}")
