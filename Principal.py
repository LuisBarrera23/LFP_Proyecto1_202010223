from tkinter import *
import tkinter
class principal:
    def __init__(self):
        self.ventana=tkinter.Tk()
        ancho=1200
        alto=700
        x=self.ventana.winfo_screenwidth()
        #calculamos la coordenada X donde se posicionara la ventana
        x=(x-ancho)/2
        y=self.ventana.winfo_screenheight()
        #calculamos la coordenada Y donde se posicionara la ventana
        y=(y-alto)/2
        self.ventana.geometry('%dx%d+%d+%d' % (ancho, alto, x, y))
        self.ventana.title("Bitxelart")
        self.ventana
        self.ventana.mainloop()