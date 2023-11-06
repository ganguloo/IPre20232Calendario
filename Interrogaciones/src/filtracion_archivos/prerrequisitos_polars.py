import polars as pl


def cursos_ingenieria_polars(path_excel_cursos: str) -> pl.DataFrame:
    """Retorna los cursos de Ingeniería junto con sus prerrequisitos y su sigla correspondiente.

    Args:
        path_excel_cursos (str): Corresponde a la ruta del archivo excel del listado de materias.

    Returns:
        pl.DataFrame: Dataframe de los cursos de ingeniería.
    """

    materias_dataframe = pl.read_excel(path_excel_cursos)
    new_columns = {col: col.strip() for col in materias_dataframe.columns}
    materias_dataframe = (materias_dataframe.rename(new_columns)
                          .with_columns(((pl.col("Materia") + pl.col("Número Curso")).alias("Sigla")))
                          .select(["Escuela", "Nombre Curso", "Prerrequisitos", "Sigla"])
                          .drop_nulls(subset=["Prerrequisitos"])
                          .filter(pl.col("Escuela") == '04 - Ingeniería')
                          .with_columns(pl.col("Prerrequisitos").str.replace_all("[()]", ""))
                          .drop("Escuela"))

    return materias_dataframe.to_pandas()
