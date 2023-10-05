"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dfframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_df():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)

    df.dropna(inplace=True)
    df = df.apply(lambda x: x.astype(str).str.replace("_","-").str.replace("-"," ").str.replace("$","").str.replace(",",""))
    df = df.apply(lambda x: x.astype(str).str.lower().str.strip(" "))
    df.fecha_de_beneficio = pd.to_datetime(df["fecha_de_beneficio"],format='mixed', dayfirst = True)
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.drop_duplicates(inplace=True)

    return df
