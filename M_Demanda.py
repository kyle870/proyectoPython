import pandas as pd
import numpy as np

from Menutab import Conexion


class M_Demanda():

    def __init__(self):
        self.Id_Demanda = -1
        self.Precio = 0.0
        self.Mes = ""
        self.Demanda = 0

    def Listar(self):
        Conex = Conexion()
        self.Conecction = Conex.getConnection()
        self.Cursor = Conex.getCursor()

        try:
            self.Lista = pd.read_sql_query(
                "select precio, mes, demanda from demanda", self.Conecction)
            # print(self.Lista['precio'])
            # print(self.Lista)

        except Exception as e:
            print(e)
        return self.Lista

    def Cursor(self):
        Conex = Conexion()
        self.Conecction = Conex.getConnection()
        self.Cursor = Conex.getCursor()

        try:
            self.Cursor.execute("select precio, mes, demanda from demanda")
        except Exception as e:
            print(e)
        return self.Cursor

    def getId_Demanda(self):
        return self.Id_Demanda

    def getPrecio(self):
        return self.Precio

    def getMes(self):
        return self.Mes

    def getDemanda(self):
        return self.Demanda


dema = M_Demanda()
"""Presenta todos las filas de la base de datos"""
pd.set_option('display.max_rows', dema.Listar().shape[0]+1)

# print(dema.Listar())
