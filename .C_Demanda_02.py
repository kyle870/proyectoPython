import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error, r2_score
import sklearn as sk
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt


from M_Demanda import M_Demanda
#from V_Demanda import pronosticoGUI

class C_Demanda:
    def __init__(self):
        self.Demanda = M_Demanda()
        self.ListaDF = self.Demanda.Listar()
        self.X_train = pd.DataFrame()
        self.X_test = pd.DataFrame()
        self.Y_train = pd.DataFrame()
        self.y_test = pd.DataFrame()

        self.AprendizajeGet()

    def getX_Test(self):
        return self.X_test


    def getY_Test(self):
        
        #print(self.X_test.plot.scatter(x='Precio', y='Mes'))

        self.DF_Ytest = pd.DataFrame(self.y_test)

        pd.set_option('display.max_rows', self.DF_Ytest.shape[0]+1)

        return self.DF_Ytest

    def getErrorCuadrado(self):
        return self.test_set_rmse

    def getRdos(self):
        return self.test_set_r2

    def getRegresion(self, precio=60, mes=1):
        # Regresion Multiple
        #regret = pronosticoGUI()
        self.lin_reg_mod = LinearRegression()

        self.lin_reg_mod.fit(self.X_train, self.y_train)

        # self.pred = self.lin_reg_mod.predict(self.X_test)

        self.A_Pred = {"Precio": [precio], "Mes": [mes]}

        self.DF_Pred = pd.DataFrame(self.A_Pred)

        self.pred = self.lin_reg_mod.predict(self.DF_Pred)

        return self.pred

    def AprendizajeGet(self):

        self.X = pd.DataFrame(
            np.c_[self.ListaDF["precio"], self.ListaDF["mes"]],
            columns=["Precio", "Mes"],
        )

        self.Y = self.ListaDF["demanda"]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.Y, test_size=0.3, random_state=9
        )

        self.lin_reg_mod = LinearRegression()

        self.lin_reg_mod.fit(self.X_train, self.y_train)

        self.pred = self.lin_reg_mod.predict(self.X_test)

        self.test_set_rmse = np.sqrt(mean_squared_error(self.y_test, self.pred))

        self.test_set_r2 = r2_score(self.y_test, self.pred)

        # print (self.pred)
        # print(test_set_rmse)
        # print(test_set_r2)
        # print(self.ListaDF.plot(figsize=(18,5)))
        # print(self.ListaDF.hist())

        self.DF_Pred = pd.DataFrame(self.pred)

        pd.set_option('display.max_rows', self.DF_Pred.shape[0]+1)

        return self.DF_Pred


c = C_Demanda()
#print(c.AprendizajeGet())
#c.getGrafica()

#print("Regresion - Pronostico")
print("Valor de la regresión: ", c.getRegresion())
#print("Error cuadratico")
#print(c.getErrorCuadrado())
#print("Rdos")
#print(c.getRdos())
#print(c.getX_Test())

#print(c.getY_Test())
#print(pd.DataFrame(c.getY_Test()))
#print(c.AprendizajeGet())

# print(c.getY_Test())
print(sns.pairplot(c.getY_Test().loc[:]))
#plt.show()
