import pandas as pd

def fechas_prohibidas(excel_file, sheet):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file, sheet_name=sheet)

    # Filter the DataFrame to select rows where the second column is 0 (not an available date)
    filtered_df = df[df.iloc[:, 1] == 0]

    # Extract the data from the first column of the filtered DataFrame, convert to string, and store them in a list
    lista_fechas = filtered_df.iloc[:, 0].dt.strftime("%d-%b").tolist()

    # Return the list of data with a value of 0 (not an available date)
    return lista_fechas


def excel_cursos_coordinados(excel_file, sheet):
    # Read the specified sheet of the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file, sheet_name=sheet)

    # Extract the data from the first column and store them in a list
    lista_cursos = df.iloc[:, 0].tolist()

    # Return the list of data from the first column
    return lista_cursos
