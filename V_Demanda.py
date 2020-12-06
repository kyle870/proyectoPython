import tkinter as tk

# from tkinter.ttk import *
from tkinter import ttk, Label, Button, CENTER
from C_Demanda import C_Demanda
from M_Demanda import M_Demanda
from scroll import Table
import pandas as pd

# import matplotlib.pyplot as plt

import matplotlib

matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure


class principal(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # construcción del resto GUI
        self.ventana = parent
        self.ventana.geometry("1080x540")
        self.ventana.title("Inicio")
        self.ventana.configure(background="#716FB7")
        self.demandagraf = C_Demanda()

        self.etiqueta = Label(
            self.ventana,
            text="Bienvenido",
            font=("Verdana", 20, "bold"),
            fg="white",
            background="#716FB7",
        )
        # self.etiqueta.pack(side=TOP)
        self.etiqueta.place(relx=0.50, rely=0.10, anchor=CENTER)

        self.lbldescript = Label(
            self.ventana,
            text="Presione un botón según lo que desea realizar.",
            font=("Arial", 16),
            fg="white",
            background="#716FB7",
        )

        self.lbldescript.place(relx=0.50, rely=0.20, anchor=CENTER)

        # ---------------------------------boton de pronostico---------------
        self.boton1 = Button(
            self.ventana,
            text="Calcular pronóstico",
            font=("Arial", 16, "bold"),
            width=16,
            height=4,
            command=self.funcpronostico,
        )
        self.boton1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.boton1.configure(background="#1489E1", fg="white")

        # ---------------------------------boton de grafico precio-------------
        self.boton2 = Button(
            self.ventana,
            text="Gráfica\nPrecio",
            font=("Arial", 16, "bold"),
            width=7,
            height=4,
            command=self.demandagraf.GraYprecio
        )
        self.boton2.place(relx=0.30, rely=0.5, anchor=CENTER)
        self.boton2.configure(background="#1489E1", fg="white")

        # ---------------------------------boton de grafico mes----------------
        self.botongr = Button(
            self.ventana,
            text="Gráfica\nMes",
            font=("Arial", 16, "bold"),
            width=7,
            height=4,
            command=self.demandagraf.GraYmes
        )
        self.botongr.place(relx=0.20, rely=0.5, anchor=CENTER)
        self.botongr.configure(background="#1489E1", fg="white")

        # ---------------------------------boton de tablas--------------------
        self.boton3 = Button(
            self.ventana,
            text="Observar tablas",
            font=("Arial", 16, "bold"),
            width=15,
            height=4,
            command=self.functablas,
        )
        self.boton3.place(relx=0.75, rely=0.5, anchor=CENTER)
        self.boton3.configure(background="#1489E1", fg="white")

    # ---------------------------------funciones-------------------
    def funcpronostico(self):
        self.pronostico = tk.Toplevel(self.ventana)
        self.app = pronosticoGUI(self.pronostico)

    # def funcgraficos(self):
        # self.demandagraf.union()
        # self.graficos = tk.Toplevel(self.ventana)
        # self.app = graficosGUI(self.graficos)

        # self.grafico1 = C_Demanda()
        # self.grafico2 = C_Demanda()

        # self.grafico1.GraYmes()
        # self.grafico2.GraYprecio()

    def functablas(self):
        self.tablas = tk.Toplevel(self.ventana)
        self.app = tablasGUI(self.tablas)


class pronosticoGUI:
    def __init__(self, parent):

        self.ventana = parent
        self.ventana.title("Pronósticos")
        self.ventana.geometry("1080x540")
        self.ventana.configure(background="#51507D")

        self.frame = tk.Frame(self.ventana)

        self.btncerrar = Button(
            self.ventana, text="Salir", width=4, height=1,
            command=self.close_windows
        )
        self.btncerrar.place(relx=0.55, rely=0.90, anchor=CENTER)
        self.btncerrar.configure(
            background="red", fg="white", font=("Verdana", 12, "bold")
        )

        # ------------------------seleccion de mes---------------
        self.lbleleccion = Label(
            self.ventana,
            text="Seleccione un mes:",
            font=("Verdana", 12, "bold"),
            fg="white",
            background="#51507D",
        )
        self.lbleleccion.place(relx=0.30, rely=0.10, anchor=CENTER)

        self.combo = ttk.Combobox(self.ventana, state="readonly")
        self.combo["values"] = [
            "Enero",
            "Febrero",
            "Marzo",
            "Abril",
            "Mayo",
            "Junio",
            "Julio",
            "Agosto",
            "Septiembre",
            "Octubre",
            "Noviembre",
            "Diciembre",
        ]
        self.combo.place(relx=0.30, rely=0.15, anchor=CENTER)

        # ------------------------- label de precio----------------------------
        self.lbleleccion = Label(
            self.ventana,
            text="Ingrese un precio:",
            font=("Verdana", 12, "bold"),
            fg="white",
            background="#51507D",
        )
        self.lbleleccion.place(relx=0.60, rely=0.10, anchor=CENTER)

        self.txtprecio = tk.Entry(self.ventana)

        self.txtprecio.place(relx=0.60, rely=0.15, anchor=CENTER)

        # -------------------------------- boton de calculo -------------------
        self.btncalcular = Button(
            self.ventana,
            text="Calcular pronóstico",
            width=15,
            height=1,
            command=self.calculo_precio,
        )
        self.btncalcular.place(relx=0.40, rely=0.90, anchor=CENTER)
        self.btncalcular.configure(
            background="green", fg="white", font=("Verdana", 12, "bold")
        )

    def calculo_precio(self):
        self.lblexplicacion = Label(
            self.ventana,
            text="El pronóstico de demanda para el mes de "
            + self.combo.get()
            + " con un precio de C$ "
            + self.txtprecio.get()
            + " es:",
        )
        # self.lblexplicacion = Label(self.ventana, text="ahkahdak")
        self.lblexplicacion.configure(
            font=("Verdana", 15, "bold"), fg="white", background="#51507D"
        )
        self.lblexplicacion.place(relx=0.50, rely=0.40, anchor=CENTER)

        self.reg_calculo = C_Demanda()
        self.lblregresion = Label(self.ventana,
                                  text=self.reg_calculo.getRegresion(
                                   precio=int(self.txtprecio.get()),
                                   mes=int(self.combo.current()) + 1),
                                  font=("Verdana", 20, "bold"),
                                  fg="white",
                                  background="#51507D")
        self.lblregresion.place(relx=0.50, rely=0.50, anchor=CENTER)
        # print(self.regresion)
        # print(int(self.txtprecio.get()))
        # print(self.combo.get())
        # print(int(self.combo.current()) + 1)

        self.frame.pack()

    def close_windows(self):
        self.ventana.destroy()


class tablasGUI:
    def __init__(self, parent):
        self.ventana2 = parent
        self.ventana2.title("Tablas")
        self.ventana2.geometry("1080x540")
        self.ventana2.configure(background="#51507D")

        self.frame = tk.Frame(self.ventana2)

        self.Demanda = C_Demanda()
        self.Deman = M_Demanda()

        # ------------------------ boton salir ventana-------------------------
        self.boton2 = Button(self.ventana2, text="Salir",
                             width=4, height=1, command=self.close_windows)
        self.boton2.place(relx=0.50, rely=0.90, anchor=CENTER)
        self.boton2.configure(
            background="red", fg="white", font=("Verdana", 12, "bold")
        )

        # self.vistatabla = Table()
        # self.vistatabla.ventana_reporte(self.ventana2)
        self.ventana_reporte(self.ventana2)

        # -----------------------------vista de las métricas-------------------
        self.var_error = C_Demanda()
        self.metrica_error_cuadrado = Label(
            self.ventana2,
            text="Error cuadrático de la regresión:\n" +
            str(self.var_error.getErrorCuadrado()),
            background="#51507D",
            fg="white",
            font=("Verdana", 12, "bold"),
        )
        self.metrica_error_cuadrado.place(relx=0.60, rely=0.20)

        self.var_Rdos = C_Demanda()
        self.metrica_Rdos = Label(
            self.ventana2,
            text="Coeficiente de determinación:\n" +
            str(self.var_Rdos.getRdos()),
            background="#51507D",
            fg="white",
            font=("Verdana", 12, "bold"),
        )
        self.metrica_Rdos.place(relx=0.60, rely=0.50)

    def ventana_reporte(self, parent):
        clientes_headers = (u"         Demanda       ", u"")
        clientes_tab = Table(parent, title="Datos Originales",
                             headers=clientes_headers)
        # clientes_tab.pack(side="right")
        clientes_tab.place(relx=0.40, rely=0.10)

        # vistademanda = M_Demanda()

        cursor = pd.DataFrame(self.Demanda.getY_Test()).to_numpy()

        for cur in cursor:
            clientes_tab.add_row(cur)

# ----------------------------otra tabla--------------------------------
        valores_predic_header = (u"        Demanda       ", u"")
        valores_predic = Table(
            parent, title="Datos pronosticados", headers=valores_predic_header
        )
        valores_predic.pack(side="left")
        valores_predic.place(relx=0.10, rely=0.10)

        cursor_predic = pd.DataFrame(self.Demanda.AprendizajeGet()).to_numpy()

        for row in cursor_predic:
            valores_predic.add_row(row)

# --------------------Elementos frame principal-----------------------
        self.frame.pack()

    def close_windows(self):
        self.ventana2.destroy()


if __name__ == "__main__":
    root = tk.Tk()

    principal(root).pack()
    root.mainloop()
