from tkinter import Button, Image, Tk,ttk,Canvas,filedialog,messagebox
import tkinter
from Error import Error
from Token import Token
Errores=[]
Tokens=[]
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
    ventana.iconbitmap('Complementos\Mario.ico')
    b1=Button(ventana,text="Cargar",font=("Verdana",10),borderwidth=3,background="beige",command=cargarArchivo).place(x=20,y=20,height=40,width=100)
    b2=Button(ventana,text="Analizar",font=("Verdana",10),borderwidth=3,background="beige").place(x=120,y=20,height=40,width=100)
    b3=Button(ventana,text="Reportes",font=("Verdana",10),borderwidth=3,background="beige").place(x=220,y=20,height=40,width=100)
    b4=Button(ventana,text="Salir",command=ventana.destroy,font=("Verdana",10),borderwidth=3,background="Red").place(x=320,y=20,height=40,width=100)
    b5=Button(ventana,text="Original",command=VerOriginal,font=("Verdana",10),borderwidth=3,background="#79FF00").place(x=20,y=400,height=40,width=180)
    b6=Button(ventana,text="Mirror X",font=("Verdana",10),borderwidth=3,background="#FF8700").place(x=20,y=440,height=40,width=180)
    b7=Button(ventana,text="Mirror Y",font=("Verdana",10),borderwidth=3,background="#FF8700").place(x=20,y=480,height=40,width=180)
    b8=Button(ventana,text="Double Mirror",font=("Verdana",10),borderwidth=3,background="#FF8700").place(x=20,y=520,height=40,width=180)
    

    ventana.mainloop()

def cargarArchivo():
    archivo=filedialog.askopenfile(
        title="Por favor seleccine un archivo",
        initialdir="./",
        filetypes=(
            ("Todos los archivos","*.*"),("Archivo PXLA","*.PXLA")
        )
    )

    if archivo is None:
        messagebox.showerror(message="No selecciono ningun archivo, por favor vuelva a intentarlo",title="Error")
        print("No selecciono ningun archivo, por favor vuelva a intentarlo")
    else:
        texto=archivo.read()
        archivo.close()
        analizar(texto)

def isLetra(C):
    if((ord(C) >= 65 and ord(C) <= 90) or (ord(C) >= 97 and ord(C) <= 122) or ord(C) == 164 or ord(C) == 165):
        return True
    else:
        return False

def isNumero(C):
    if ((ord(C) >= 48 and ord(C) <= 57)):
        return True
    else:
        return False

def analizar(txt):
    global Tokens,Errores
    fila=1
    columna=1
    estado=0
    error=False
    LexemaActual=""
    for c in txt:
        #print("Fila:",fila,"Columna:",columna,"caracter:",c)
        if estado==0 and ord(c)!=32:
            if isLetra(c):
                LexemaActual+=c
                estado=1
            else:
                Errores.append(Error(fila,columna,c))
                error=True
                LexemaActual=""
        elif estado==1:
            if isLetra(c):
                LexemaActual+=c
                estado=1
            elif ord(c)==61:#signo =
                print(LexemaActual)
                LexemaActual=""
                estado=2
            else:
                if ord(c)==32:
                    pass
                else:
                    #print("Error, se esperaba letra en Fila:",fila,"columna:",columna)
                    Errores.append(Error(fila,columna,c))
                    estado=0
                    LexemaActual=""
        elif estado==2:
            if ord(c)==34:
                estado=3
            else:
                if ord(c)==32:
                    pass
                else:
                    Errores.append(Error(fila,columna,c))
                    estado=0
                    LexemaActual=""
        
        elif estado==3:
            if isLetra(c):
                LexemaActual+=c
                estado=4
            elif isNumero(c):
                LexemaActual+=c
                estado=4
            else:
                if ord(c)==34:
                    estado=5
                    print("nombre vacio")
                else:
                    LexemaActual+=c
                    estado=4
        elif estado==4:
            if ord(c)==34:
                print(LexemaActual)
                LexemaActual=""
                estado=5
            else:
                LexemaActual+=c
        elif estado==5:
            if ord(c)==59:
                print("caracter",c)
                estado=0
            else:
                Errores.append(Error(fila,columna,c))
                estado=0
                LexemaActual=""
        




        # controlador de filas y columnas
        if ord(c) == 10:
            columna=1
            fila+=1
            continue
        elif(ord(c) == 9): #para tabulación
            columna+=4
            continue
        elif(ord(c)==32):
            columna+=1
            continue
        columna+=1
    
    for e in Errores:
        print("fila:",e.fila,"columna",e.columna,"caracter:",e.caracter)


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