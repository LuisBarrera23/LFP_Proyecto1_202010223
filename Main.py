from tkinter import Button, Image, Tk,ttk,Canvas
import tkinter
ventana=Tk()
canvas = Canvas()

def generarVentana():
    global ventana,canvas
    canvas = Canvas(ventana,width=940, height=580, bg='white')
    canvas.place(x=220,y=80)
    ventana.configure(background="#008080")
    ancho=1200
    alto=700
    x=ventana.winfo_screenwidth()
    #calculamos la coordenada X donde se posicionara la ventana
    x=(x-ancho)/2
    y=ventana.winfo_screenheight()
    #calculamos la coordenada Y donde se posicionara la ventana
    y=(y-alto)/2
    ventana.geometry('%dx%d+%d+%d' % (ancho, alto, x, y))
    ventana.title("Bitxelart")
    b1=Button(ventana,text="Cargar",font=("Verdana",10),borderwidth=3,background="beige",command=cargarArchivo).place(x=20,y=20,height=40,width=100)
    b2=Button(ventana,text="Analizar",font=("Verdana",10),borderwidth=3,background="beige").place(x=120,y=20,height=40,width=100)
    b3=Button(ventana,text="Reportes",font=("Verdana",10),borderwidth=3,background="beige").place(x=220,y=20,height=40,width=100)
    b4=Button(ventana,text="Salir",font=("Verdana",10),borderwidth=3,background="Red").place(x=320,y=20,height=40,width=100)
    b5=Button(ventana,text="Original",command=VerOriginal,font=("Verdana",10),borderwidth=3,background="#79FF00").place(x=20,y=400,height=40,width=180)
    b6=Button(ventana,text="Mirror X",font=("Verdana",10),borderwidth=3,background="#FF8700").place(x=20,y=440,height=40,width=180)
    b7=Button(ventana,text="Mirror Y",font=("Verdana",10),borderwidth=3,background="#FF8700").place(x=20,y=480,height=40,width=180)
    b8=Button(ventana,text="Double Mirror",font=("Verdana",10),borderwidth=3,background="#FF8700").place(x=20,y=520,height=40,width=180)
    

    ventana.mainloop()

def cargarArchivo():
    global canvas
    print("pulsacion cargar")
    canvas.delete(tkinter.ALL)


def VerOriginal():
    global ventana,canvas
    canvas.delete(tkinter.ALL)
    print("hola")
    posx=10
    posy=10
    for i in range(5):
        canvas.create_rectangle(posx,posy,posx+10,posy+10, width=3, fill='red')
        posx+=10

if __name__=='__main__':
    generarVentana()