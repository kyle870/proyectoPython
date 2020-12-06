import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
# from M_Demanda import M_Demanda


class Table(tk.Frame):
    def __init__(self, parent=None, title="", headers=[], *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._title = tk.Label(self, text=title, background="#51507D",
                               fg="white", font=("Verdana", 12, "bold"))
        self._headers = headers
        self._tree = ttk.Treeview(self,
                                  height=15,
                                  columns=self._headers,
                                  show="headings")
        self._title.pack(side=tk.TOP, fill="x")

        # Agregamos dos scrollbars
        vsb = ttk.Scrollbar(self, orient="vertical",
                            command=self._tree.yview)
        vsb.pack(side='right', fill='y')
        hsb = ttk.Scrollbar(self, orient="horizontal",
                            command=self._tree.xview)
        hsb.pack(side='bottom', fill='x')

        self._tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
        self._tree.pack(side="left")

        for header in self._headers:
            self._tree.heading(header, text=header.title())
            self._tree.column(header, stretch=True,
                              width=tkFont.Font().measure(header.title()))

    def add_row(self, row):
        self._tree.insert('', 'end', values=row)
        for i, item in enumerate(row):
            col_width = tkFont.Font().measure(item)
            if self._tree.column(self._headers[i], width=None) < col_width:
                self._tree.column(self._headers[i], width=col_width)
