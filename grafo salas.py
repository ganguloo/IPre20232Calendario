import polars as pl
import pandas as pd
import networkx as nx
import os
import matplotlib.pyplot as plt
path_nodos = os.path.join('Datos', "Salas SJ 2023-07-13.xlsx")
path_edges = os.path.join('Datos', "datos grafo salas.xlsx")


def crear_grafo(path_edges, path_nodos):
    """cargar excel y arreglar nodos"""
    edgelist_pl = pl.read_excel(path_edges)
    nodelist_pl = pl.read_excel(path_nodos)
    new_columns = {col: col.strip() for col in nodelist_pl.columns}
    nodelist_pl = (nodelist_pl.rename(new_columns).drop('Location Formal Name').drop('Campus Partition').filter(pl.col("Max Capacity") >= 20))
    edgelist_pl = (edgelist_pl.filter(pl.col("distancia") != 0))
    lista = []
    for item in nodelist_pl.to_pandas()['Location Name'].values:
        lista.append(item[3:])
    nueva_col = pl.Series(lista)
    nodelist_pl.replace('Location Name', nueva_col)
    nodelist_pd = nodelist_pl.to_pandas()
    edgelist_pd = edgelist_pl.to_pandas()

    """Crear Grafo"""
    g = nx.Graph()
    for i, elrow in edgelist_pd.iterrows():
        g.add_edge(elrow[0], elrow[1], attr_dict=elrow[2:].to_dict())
    for i, nlrow in nodelist_pd.iterrows():
        g.add_node(nlrow[0], capacidad=nlrow[1])

    edge_colors = [e[2]['attr_dict']['color'] for e in list(g.edges(data=True))]
    # print(list(g.edges(data=True))[0:40])
    # print(list(g.nodes(data=True))[0:40])

    plt.figure(figsize=(8, 6))
    nx.draw(g, edge_color=edge_colors, node_size=10, node_color='black', with_labels=True, font_size=5)
    plt.show()


crear_grafo(path_edges, path_nodos)

# falta borrar de nodelist las salas con poca capacidad
