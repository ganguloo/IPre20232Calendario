archivo = open("datos/salas.csv")
info = archivo.readlines()[1:]
archivo.close()


def capacidad_salas(peticion):
    if peticion == "capacidad":
        return list(map(lambda x: int(x.split("\n")[0].split(",")[1]), info))
    else:
        return list(map(lambda x: float(x.split("\n")[0].split(",")[2]), info))