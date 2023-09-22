archivo = open("datos/cursos.csv")
info = archivo.readlines()[1:]
archivo.close()


def curso(criterio):
    if criterio == "vacantes":
        pedido = list(map(lambda x: float(x.split("\n")[0].split(",")[1]), info))
    elif criterio == "nombres":
        pedido = list(map(lambda x: float(x.split("\n")[0].split(",")[0]), info))
    elif criterio == "particion":
        pedido = list(map(lambda x: float(x.split("\n")[0].split(",")[2]), info))
    return pedido