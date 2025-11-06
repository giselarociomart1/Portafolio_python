import pandas as pd
from sqlalchemy import create_engine


# Función para filtrar un DataFrame por un rango de fechas.
def filtrar_por_fecha(df, columna_fecha, fecha_inicio, fecha_fin):
    """
    Filtra un DataFrame por un rango de fechas.
    
    Parámetros:
    - df (pd.DataFrame): DataFrame a filtrar.
    - columna_fecha (str): Nombre de la columna con fechas.
    - fecha_inicio (str): Fecha de inicio en formato 'YYYY-MM-DD'.
    - fecha_fin (str): Fecha de fin en formato 'YYYY-MM-DD'.
    
    Retorna:
    - pd.DataFrame: DataFrame filtrado por fecha.
    """
    df[columna_fecha] = pd.to_datetime(df[columna_fecha])  # Aseguramos tipo datetime.
    resultado = df[(df[columna_fecha] >= fecha_inicio) & (df[columna_fecha] <= fecha_fin)]
    return resultado


# Función para generar reportes tipo tabla dinámica.
def generar_reporte(df, index, values, aggfunc, columns=None, margins=False):
    """
    Genera un reporte tipo tabla dinámica (pivot table).
    
    Parámetros:
    - df (pd.DataFrame): DataFrame base.
    - index (str o lista): Columna(s) para las filas del pivot.
    - values (str o lista): Columna(s) con los valores a agregar.
    - aggfunc (str): Función de agregación ('sum', 'mean', etc.).
    - columns (str o lista, opcional): Columnas adicionales para las columnas del pivot.
    - margins (bool): Si True, incluye fila/columna de totales.
    
    Retorna:
    - pd.DataFrame: DataFrame pivotado.
    """
    tabla = pd.pivot_table(
        df,
        index=index,
        columns=columns,
        values=values,
        aggfunc=aggfunc,
        fill_value=0,
        margins=margins,
        margins_name="TOTAL"
    )
    return tabla.reset_index()


# Función para escribir un DataFrame en la base de datos.
def escribir_en_db(df, tabla, engine, if_exists="replace"):
    """
    Guarda un DataFrame en PostgreSQL.
    
    Parámetros:
    - df (pd.DataFrame): DataFrame a guardar.
    - tabla (str): Nombre de la tabla en la base de datos.
    - engine (SQLAlchemy Engine): Conexión a la base de datos.
    - if_exists (str): Acción si la tabla ya existe ('replace', 'append', 'fail').
    """
    df.to_sql(tabla, con=engine, if_exists=if_exists, index=False)
    print(f"Tabla '{tabla}' guardada con éxito en PostgreSQL.")
