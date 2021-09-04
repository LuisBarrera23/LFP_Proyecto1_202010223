from tkinter import Button, Tk,ttk,Canvas
class principal:
    
    def __init__(self):
        self.ventana=Tk()
        self.ventana.configure(background="#008080")
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
        b1=Button(self.ventana,text="Cargar",font=("Verdana",10),borderwidth=3,background="beige",command=cargarArchivo).place(x=20,y=20,height=40,width=100)
        b2=Button(self.ventana,text="Analizar",font=("Verdana",10),borderwidth=3,background="beige").place(x=120,y=20,height=40,width=100)
        b2=Button(self.ventana,text="Reportes",font=("Verdana",10),borderwidth=3,background="beige").place(x=220,y=20,height=40,width=100)
        b2=Button(self.ventana,text="Salir",font=("Verdana",10),borderwidth=3,background="Red").place(x=320,y=20,height=40,width=100)
        self.canvas = Canvas(self.ventana,width=940, height=580, bg='white')
        self.canvas.place(x=220,y=80)
        self.canvas.create_rectangle(10, 10, 200, 200, width=3, fill='red')
        self.ventana.mainloop()
        
def cargarArchivo():
            print("pulsacion cargar")