import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error, r2_score

# import sklearn as sk
from sklearn.linear_model import LinearRegression

from M_Demanda import M_Demanda


class C_Demanda:
    def __init__(self):
        self.Demanda = M_Demanda()
        self.ListaDF = self.Demanda.Listar()
        self.X_train = pd.DataFrame()
        self.X_test = pd.DataFrame()
        self.Y_train = pd.DataFrame()
        self.y_test = pd.DataFrame()
        self.Aprendizaje()

    def getX_Test(self):
        pd.set_option('display.max_rows', self.X_test.shape[0]+1)
        return self.X_test

    def getErrorCuadrado(self):
        self.test_set_rmse = np.sqrt(
            mean_squared_error(self.y_test, self.getRegresion())
        )
        return self.test_set_rmse

    def getRdos(self):
        self.test_set_r2 = r2_score(self.y_test, self.getRegresion())
        return self.test_set_r2

    def getRegresion(self):
        # Regresion Multiple
        self.lin_reg_mod = LinearRegression()

        self.lin_reg_mod.fit(self.X_train, self.y_train)

        # self.pred = self.lin_reg_mod.predict(self.X_test)

        d = {"Precio": [60], "Mes": [1]}

        self.pred = self.lin_reg_mod.predict(pd.DataFrame(d))

        print(pd.DataFrame(d))

        return self.pred

    def Aprendizaje(self):

        self.X = pd.DataFrame(
            np.c_[self.ListaDF["precio"], self.ListaDF["mes"]],
            columns=["Precio", "Mes"],
        )

        self.Y = self.ListaDF["demanda"]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.Y, test_size=0.2, random_state=9
        )

        # print (self.pred)
        # print(test_set_rmse)
        # print(test_set_r2)
        # print(self.ListaDF.plot(figsize=(18,5)))
        # print(self.ListaDF.hist())


c = C_Demanda()
c.Aprendizaje()
# print(c.getRegresion())
# print(c.getErrorCuadrado())
# print(c.getRdos())
# print(c.getX_Test())
