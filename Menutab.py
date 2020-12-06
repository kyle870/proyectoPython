# from tkinter import messagebox
import pymysql


class Conexion:
    def __init__(self):
        # self.connection = pymysql.connect(host='192.168.15.89',
        #                                   user='root',
        #                                   password='Aa_123456',
        #                                   db='trasport')
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='programacion6',
                                          db='trasport')
        # self.connection = pymysql.connect(host='localhost',
        #                                   user='root',
        #                                   password='123456',
        #                                   db='trasport')
        self.cursor = self.connection.cursor()
        print("Conexión establecida exitosamente!")
        # messagebox.showinfo("Conexion", "Conexión establecida exitosamente")

    def getConnection(self):
        return self.connection

    def getCursor(self):
        return self.cursor


# database = DataBase()
# database.select_user(1)
