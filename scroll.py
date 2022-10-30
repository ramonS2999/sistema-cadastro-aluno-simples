from tkinter import *
import view
from configuracao import  Configuracao
from menu import listar

class MyList(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_propagate(False)
        self.cf = Configuracao()

        self.lista_alunos = listar()

        self.canvas = Canvas(self)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scroll_bar = Scrollbar(self, orient=VERTICAL, command=self.canvas.yview)
        self.scroll_bar.grid(row=0, column=1, sticky='ns')
        self.canvas.config(yscrollcommand=self.scroll_bar.set)

        self.internal_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.internal_frame, anchor='nw')

        self.__build()
        self.internal_frame.update_idletasks()

        self.config(width=800, height=500)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def __build(self):
        """Função que fará as informações aparecerem no Scrollbar"""
        linha = 1
        view.show_campos(self.internal_frame)

        for key, value in self.lista_alunos.items():
            Label(self.internal_frame, font=self.cf.font1, text=f"{key}").grid(column=0, row=linha)
            Label(self.internal_frame, font=self.cf.font1, text=f"{self.lista_alunos.get(key)[0]}").grid(column=1, row=linha)
            Label(self.internal_frame, font=self.cf.font1, text=f"{(self.lista_alunos.get(key)[1])}").grid(column=2, row=linha)
            Label(self.internal_frame, font=self.cf.font1, text=f"{(self.lista_alunos.get(key)[2])}").grid(column=3, row=linha)
            Label(self.internal_frame, font=self.cf.font1, text=f"{(self.lista_alunos.get(key)[3])}").grid(column=4, row=linha)
            Label(self.internal_frame, font=self.cf.font1, text=f"{self.lista_alunos.get(key)[4]}").grid(column=5, row=linha)

            linha += 1
