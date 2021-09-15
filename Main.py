from tkinter import Button, Image, Tk,ttk,Canvas,filedialog,messagebox
import tkinter
from Error import Error
from Token import Token
from Imagen import imagen
from Celda import celda


#Variables globales
Errores=[]
Tokens=[]
Imagenes=[]
texto=""
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
    b1=Button(ventana,text="Cargar",command=cargarArchivo,font=("Verdana",10),borderwidth=3,background="beige").place(x=20,y=20,height=40,width=100)
    b2=Button(ventana,text="Analizar",command=Solicitaranalisis,font=("Verdana",10),borderwidth=3,background="beige").place(x=120,y=20,height=40,width=100)
    b3=Button(ventana,text="Reportes",font=("Verdana",10),borderwidth=3,background="beige").place(x=220,y=20,height=40,width=100)
    b4=Button(ventana,text="Salir",command=ventana.destroy,font=("Verdana",10),borderwidth=3,background="Red").place(x=320,y=20,height=40,width=100)
    b5=Button(ventana,text="Original",command=VerOriginal,font=("Verdana",10),borderwidth=3,background="#79FF00").place(x=20,y=400,height=40,width=180)
    b6=Button(ventana,text="Mirror X",font=("Verdana",10),borderwidth=3,background="#FF8700").place(x=20,y=440,height=40,width=180)
    b7=Button(ventana,text="Mirror Y",font=("Verdana",10),borderwidth=3,background="#FF8700").place(x=20,y=480,height=40,width=180)
    b8=Button(ventana,text="Double Mirror",font=("Verdana",10),borderwidth=3,background="#FF8700").place(x=20,y=520,height=40,width=180)
    

    ventana.mainloop()


def Solicitaranalisis():
    global texto
    if texto=="":
        print("texto vacio")
    else:
        analizar(texto)


def cargarArchivo():
    global texto
    archivo=filedialog.askopenfile(
        title="Por favor seleccine un archivo",
        initialdir="./",
        filetypes=(
            ("Todos los archivos","*.*"),("Archivo PXLA","*.pxla")
        )
    )

    if archivo is None:
        messagebox.showerror(message="No selecciono ningun archivo, por favor vuelva a intentarlo",title="Error")
        print("No selecciono ningun archivo, por favor vuelva a intentarlo")
    else:
        texto=archivo.read()
        archivo.close()

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

def isEspacio(C):
    if (ord(C)==32 or ord(C)==9 or ord(C)==10):
        return True
    else:
        return False

def analizar(txt):
    global Tokens,Errores,Imagenes
    Errores=[]
    Tokens=[]
    Imagenes=[]
    fila=1
    columna=1
    estado=0
    error=False
    LexemaActual=""
    actual=""
    celdas=[]
    filtros=[]
    for c in txt:
        if estado==0 and not isEspacio(c):
            if isLetra(c):
                LexemaActual+=c
                estado=1
            elif ord(c)==64:
                LexemaActual+=c
                estado=18
            else:
                Errores.append(Error(fila,columna,c,"Se esperaba letra"))
                error=True
                LexemaActual=""
                estado=0
        elif estado==1:
            if isLetra(c):
                LexemaActual+=c
                estado=1
            elif ord(c)==61:#signo =
                #print(LexemaActual)
                if LexemaActual=="TITULO":
                    Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    actual=LexemaActual
                elif LexemaActual=="ANCHO":
                    Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    actual=LexemaActual
                elif LexemaActual=="ALTO":
                    Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    actual=LexemaActual
                elif LexemaActual=="FILAS":
                    Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    actual=LexemaActual
                elif LexemaActual=="COLUMNAS":
                    Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    actual=LexemaActual
                elif LexemaActual=="CELDAS":
                    Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    actual=LexemaActual
                elif LexemaActual=="FILTROS":
                    Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    actual=LexemaActual
                Tokens.append(Token("Simbolo",c,fila,columna))
                LexemaActual=""
                estado=2
            else:
                if ord(c)==32:
                    pass
                else:
                    if LexemaActual=="TITULO":
                        Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    elif LexemaActual=="ANCHO":
                        Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    elif LexemaActual=="ALTO":
                        Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    elif LexemaActual=="FILAS":
                        Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    elif LexemaActual=="COLUMNAS":
                        Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    elif LexemaActual=="CELDAS":
                        Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    elif LexemaActual=="FILTROS":
                        Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    Errores.append(Error(fila,columna,c))
                    error=True
                    estado=0
                    LexemaActual=""
        elif estado==2:
            if ord(c)==34: #comillas dobles
                Tokens.append(Token("Simbolo",c,fila,columna))
                estado=3
            elif isNumero(c): #numero
                LexemaActual+=c
                estado=5
            elif ord(c)==123: #llave
                Tokens.append(Token("Simbolo",c,fila,columna))
                estado=6
            elif isLetra(c): #letra
                LexemaActual+=c
                estado=17
            else:
                if ord(c)==32:
                    pass
                else:
                    Errores.append(Error(fila,columna,c,"caracter no valido"))
                    error=True
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
                    estado=21
                    Tokens.append(Token("Simbolo",c,fila,columna))
                    Errores.append(Error(fila,columna,c,"nombre vacio"))
                    error=True
                    print("nombre vacio")
                else:
                    LexemaActual+=c
                    estado=4
        elif estado==4:
            if ord(c)==34:
                titulo=LexemaActual
                Tokens.append(Token("Cadena",LexemaActual,fila,columna-len(LexemaActual)))
                Tokens.append(Token("Simbolo",c,fila,columna))
                LexemaActual=""
                estado=21
            else:
                LexemaActual+=c
        # logica los numeros--------------------------------------------------------------------
        elif estado==5:
            if isNumero(c):
                LexemaActual+=c
                estado=5
            elif isLetra(c):
                Errores.append(Error(fila,columna,c,"se esperaba numero"))
                error=True
                estado=0
            elif ord(c)==59:
                Tokens.append(Token("Numero",LexemaActual,fila,columna-len(LexemaActual)))
                Tokens.append(Token("Simbolo",c,fila,columna))
                if error is False:
                    if actual=="ANCHO":
                        ancho=str(LexemaActual)
                    elif actual=="ALTO":
                        alto=str(LexemaActual)
                    elif actual=="FILAS":
                        filas=str(LexemaActual)
                    elif actual=="COLUMNAS":
                        columnas=str(LexemaActual)
                    
                LexemaActual=""
                estado=0
            else:
                Errores.append(Error(fila,columna,c,"se esperaba numero"))
                error=True
                estado=0
        #logica de celdas --------------------------------------------------------------------------
        elif estado==6 and not isEspacio(c):
            if ord(c)==91: #corchete
                Tokens.append(Token("Simbolo",c,fila,columna))
                estado=7
            else: 
                Errores.append(Error(fila,columna,c,"se esperaba corchete"))
                error=True

        elif estado==7 and not isEspacio(c):
            if isNumero(c):
                LexemaActual+=c
                estado=8
            else:
                Errores.append(Error(fila,columna,c,"se esperaba numero"))
                error=True
                LexemaActual=""
                estado=6
        elif estado==8:
            if isNumero(c):
                LexemaActual+=c
                estado=8
            elif ord(c)==44:
                if error is False:
                    x=str(LexemaActual)
                Tokens.append(Token("Numero",LexemaActual,fila,columna-len(LexemaActual)))
                Tokens.append(Token("Simbolo",c,fila,columna))
                LexemaActual=""
                estado=9
            else:
                Errores.append(Error(fila,columna,c,"Caracter no valido"))
                error=True
                LexemaActual=""
                estado=6
        elif estado==9 and not isEspacio(c):
            if isNumero(c):
                LexemaActual+=c
                estado=10
            else:
                Errores.append(Error(fila,columna,c,"se esperaba numero"))
                error=True
                LexemaActual=""
                estado=6 
        elif estado==10:
            if isNumero(c):
                LexemaActual+=c
                estado=10
            elif ord(c)==44:
                if error is False:
                    y=str(LexemaActual)
                Tokens.append(Token("Numero",LexemaActual,fila,columna-len(LexemaActual)))
                Tokens.append(Token("Simbolo",c,fila,columna))
                LexemaActual=""
                estado=11
            else:
                Errores.append(Error(fila,columna,c,"Caracter no valido"))
                error=True
                LexemaActual=""
                estado=6
        elif estado==11 and not isEspacio(c):
            if isLetra(c):
                LexemaActual+=c
                estado=12
            else:
                Errores.append(Error(fila,columna,c,"Caracter no valido"))
                error=True
                estado=6
        elif estado==12:
            if isLetra(c):
                LexemaActual+=c
                estado=12
            elif ord(c)==44:
                if LexemaActual=="TRUE":
                    if error is False:
                        pintado=LexemaActual
                    Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    LexemaActual=""
                    estado=13
                elif LexemaActual=="FALSE":
                    if error is False:
                        pintado=LexemaActual
                    Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    LexemaActual=""
                    estado=13
                else:
                    Errores.append(Error(fila,columna-len(LexemaActual),c,"Palabra reservada mal escrita"))
                    LexemaActual=""
                    error=True
                    estado=6
                Tokens.append(Token("Simbolo",c,fila,columna))
            else:
                Errores.append(Error(fila,columna,c,"caracter no valido"))
                error=True
                estado=6
                
        elif estado==13 and not isEspacio(c):
            if ord(c)==35:
                LexemaActual+=c
                estado=14
            else:
                Errores.append(Error(fila,columna,c,"Se esperaba #"))
                error=True
                estado=6
        elif estado==14:
            if isLetra(c) or isNumero(c):
                LexemaActual+=c
                estado=15
            else:
                Errores.append(Error(fila,columna,c,"Caracter no valido"))
                error=True
                LexemaActual=""
                estado=6
        elif estado==15:
            if isLetra(c) or isNumero(c):
                LexemaActual+=c
                estado=15
            elif ord(c)==93:# cerra corchete
                if error is False:
                    color=LexemaActual
                    celdas.append(celda(x,y,pintado,color))
                Tokens.append(Token("Color",LexemaActual,fila,columna-len(LexemaActual)))
                Tokens.append(Token("Simbolo",c,fila,columna))
                LexemaActual=""
                estado=16
            else:
                LexemaActual=""
                Errores.append(Error(fila,columna,c,"Caracter no valido"))
                error=True
                estado=6
        elif estado==16 and not isEspacio(c):
            if ord(c)==44:
                LexemaActual=""
                Tokens.append(Token("Simbolo",c,fila,columna))
                estado=6
            elif ord(c)==125:
                LexemaActual=""
                Tokens.append(Token("Simbolo",c,fila,columna))
                estado=21
            else:
                LexemaActual=""
                Errores.append(Error(fila,columna,c,"Caracter no valido"))
                error=True
                estado=0
            
        # logica de los filtros---------------------------------------------------------------------------
        elif estado==17:
            if isLetra(c):
                LexemaActual+=c
                estado=17
            elif ord(c)==44:
                if LexemaActual=="MIRRORX" or LexemaActual=="MIRRORY" or LexemaActual=="DOUBLEMIRROR":
                    Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    if error is False:
                        filtros.append(LexemaActual)
                    LexemaActual=""
                    estado=17
                else:
                    Errores.append(Error(fila,columna-len(LexemaActual),c,"Palabra reservada mal escrita"))
                    LexemaActual=""
                    error=True
                    estado=0
                Tokens.append(Token("Simbolo",c,fila,columna))
            elif ord(c)==59:
                if LexemaActual=="MIRRORX" or LexemaActual=="MIRRORY" or LexemaActual=="DOUBLEMIRROR":
                    Tokens.append(Token("Reservada",LexemaActual,fila,columna-len(LexemaActual)))
                    if error is False:
                        filtros.append(LexemaActual)
                        Imagenes.append(imagen(titulo,ancho,alto,filas,columnas,celdas,filtros))
                        celdas=[]
                        filtros=[]
                    LexemaActual=""
                    estado=0
                else:
                    Errores.append(Error(fila,columna-len(LexemaActual),c,"Palabra reservada mal escrita"))
                    LexemaActual=""
                    error=True
                    estado=0
                Tokens.append(Token("Simbolo",c,fila,columna))

        #logica para separador----------------------------------------------------------------
        elif estado==18:
            if ord(c)==64:
                LexemaActual+=c
                estado=19
            else:
                Errores.append(Error(fila,columna,c,"Se esperaba @"))
                LexemaActual=""
                error=True
                estado=0
        elif estado==19:
            if ord(c)==64:
                LexemaActual+=c
                estado=20
            else:
                Errores.append(Error(fila,columna,c,"Se esperaba @"))
                LexemaActual=""
                error=True
                estado=0
        elif estado==20:
            if ord(c)==64:
                LexemaActual+=c
                Tokens.append(Token("Separador",LexemaActual,fila,columna-len(LexemaActual)))
                estado=0
            else:
                Errores.append(Error(fila,columna,c,"Se esperaba @"))
                LexemaActual=""
                error=True
                estado=0

        
        
        
        elif estado==21:
            if ord(c)==59:
                Tokens.append(Token("Simbolo",c,fila,columna))
                estado=0
            else:
                Errores.append(Error(fila,columna,c,"se esperaba simbolo"))
                error=True
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
        print("fila:",e.fila,"columna",e.columna,"caracter:",e.caracter,e.observacion)

    #for t in Tokens:
    #    print(t.token,t.lexema,t.fila,t.columna)
    if error:
        print("Si hubo error")
    else:
        print("No hubo error")
        for i in Imagenes:
            print(i.titulo)
            i.mostrarCeldas()


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