archivo = open("Salas/datos/salas.csv")
info = archivo.readlines()[1:]
archivo.close()


def capacidad_salas(peticion):
    if peticion == "capacidad":
        return list(map(lambda x: int(x.split("\n")[0].split(",")[1]), info))
    else:
        return list(map(lambda x: x.split("\n")[0].split(",")[0], info))