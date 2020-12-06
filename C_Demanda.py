import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error, r2_score
# import sklearn as sk
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress

from M_Demanda import M_Demanda


class C_Demanda:
    def __init__(self):
        self.Demanda = M_Demanda()
        self.ListaDF = self.Demanda.Listar()
        self.X_train = pd.DataFrame()
        self.X_test = pd.DataFrame()
        self.Y_train = pd.DataFrame()
        self.y_test = pd.DataFrame()

        self.AprendizajeGet()

    def GraYprecio(self):
        # Grafica de regresion lineal entre demanda y precio

        x = pd.DataFrame(self.getX_Test()).astype(float)["Precio"]
        y = pd.DataFrame(self.getY_Test()).astype(float)["demanda"]

        stats = linregress(x, y)

        m = stats.slope
        b = stats.intercept
        plt.scatter(x, y)

        plt.plot(x, m * x + b, color="red")

        plt.show()

    def GraYmes(self):
        # Grafica de regresion lineal entre demanda y mes

        x = pd.DataFrame(self.getX_Test()).astype(float)["Mes"]
        y = pd.DataFrame(self.getY_Test()).astype(float)["demanda"]

        stats = linregress(x, y)

        m = stats.slope
        b = stats.intercept

        plt.scatter(x, y)
        plt.plot(x, m * x + b, color="red")

        plt.show()

    def GraDispersion(self):
        # Grafico de dispersion para la parte de los Test

        x = self.X_test["Precio"]
        y = self.getY_Test()["demanda"]
        print(sns.scatterplot(x=x, y=y))

    def getX_Test(self):
        return pd.DataFrame(self.X_test)

    def getY_Test(self):
        return self.y_test

    def getErrorCuadrado(self):
        # Retornar Error cuadratico medio del aprendizaje
        return self.test_set_rmse

    def getRdos(self):
        # Retornar Rdos (coeficiente de determinacion)
        return self.test_set_r2

    def getRegresion(self, precio=60, mes=1):
        # Regresion Multiple pasando como parametro el mes y precio

        self.lin_reg_mod = LinearRegression()

        self.lin_reg_mod.fit(self.X_train, self.y_train)

        # self.pred = self.lin_reg_mod.predict(self.X_test)

        self.A_Pred = {"Precio": [precio], "Mes": [mes]}

        self.DF_Pred = pd.DataFrame(self.A_Pred)

        self.pred = self.lin_reg_mod.predict(self.DF_Pred)

        return self.pred

    def AprendizajeGet(self):
        # Aprendizaje del algoritmo y retorna la prediccion

        self.X = pd.DataFrame(
            np.c_[self.ListaDF["precio"], self.ListaDF["mes"]],
            columns=["Precio", "Mes"],
        )

        self.Y = self.ListaDF["demanda"]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.Y, test_size=0.3, random_state=9)

        self.lin_reg_mod = LinearRegression()

        self.lin_reg_mod.fit(self.X_train, self.y_train)

        self.pred = self.lin_reg_mod.predict(self.X_test)

        self.test_set_rmse = np.sqrt(mean_squared_error(self.y_test,
                                                        self.pred))

        self.test_set_r2 = r2_score(self.y_test, self.pred)

        return self.pred
