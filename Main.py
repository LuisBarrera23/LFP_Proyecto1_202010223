from tkinter import Button, Image, Tk,ttk,Canvas,filedialog,messagebox
import tkinter
from os import startfile
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
combo=ttk.Combobox()
canvas = Canvas()

def generarVentana():
    global ventana,canvas,combo
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
    b3=Button(ventana,text="Reportes",command=generarReporteHTML,font=("Verdana",10),borderwidth=3,background="beige").place(x=220,y=20,height=40,width=100)
    b4=Button(ventana,text="Salir",command=ventana.destroy,font=("Verdana",10),borderwidth=3,background="Red").place(x=320,y=20,height=40,width=100)
    b5=Button(ventana,text="Original",command=VerOriginal,font=("Verdana",10),borderwidth=3,background="#79FF00").place(x=20,y=400,height=40,width=180)
    b6=Button(ventana,text="Mirror X",font=("Verdana",10),borderwidth=3,background="#FF8700").place(x=20,y=440,height=40,width=180)
    b7=Button(ventana,text="Mirror Y",font=("Verdana",10),borderwidth=3,background="#FF8700").place(x=20,y=480,height=40,width=180)
    b8=Button(ventana,text="Double Mirror",font=("Verdana",10),borderwidth=3,background="#FF8700").place(x=20,y=520,height=40,width=180)
    b9=Button(ventana,text="Ver imagen",command=verImagen,font=("Verdana",10),borderwidth=3,background="#FF8700").place(x=60,y=230,height=30,width=100)
    

    combo=ttk.Combobox(ventana,state="readonly")
    combo.place(x=20,y=200)
    combo.configure(width=27)
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
                else:
                        Errores.append(Error(fila,columna-len(LexemaActual),LexemaActual,"Palabra reservada mal escrita"))
                        LexemaActual=""
                        error=True
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
                    else:
                        Errores.append(Error(fila,columna-len(LexemaActual),LexemaActual,"Palabra reservada mal escrita"))
                        LexemaActual=""
                        error=True
                    Errores.append(Error(fila,columna,c,"Caracter no valido"))
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
                        ancho=int(LexemaActual)
                    elif actual=="ALTO":
                        alto=int(LexemaActual)
                    elif actual=="FILAS":
                        filas=int(LexemaActual)
                    elif actual=="COLUMNAS":
                        columnas=int(LexemaActual)
                    
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
                    x=int(LexemaActual)
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
                    y=int(LexemaActual)
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
            else:
                LexemaActual=""
                Errores.append(Error(fila,columna,c,"Caracter no valido"))
                error=True
                estado=0

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
                LexemaActual=""
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
        messagebox.showinfo(message="Se reportaron errores en el analisis por favor vea los reportes",title="Aviso")
    else:
        print("No hubo error")
        messagebox.showinfo(message="Se realizo el analisis con exito y sin errores",title="Aviso")
        modificarCombo()
        # for i in Imagenes:
        #     print(i.titulo)
        #     i.mostrarCeldas()

def modificarCombo():
    global combo, Imagenes
    combo["values"]=[]
    
    for i in Imagenes:
        values = list(combo["values"])
        combo["values"] = values + [i.titulo]
    combo.set("Seleccione una imagen")
    print(combo.get())

def generarReporteHTML():
    global Tokens,Errores
    f=open("Reporte.html","w",encoding='UTF-8')
    inicio="""
    <!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">

    <title>Reporte Proyecto 1</title>
    </head>
    <style>
    .titulo{
        text-align: center;
        background-color: aqua;
        padding: 8px;
    }
    .cuerpo{
        background-color: white;
    }
    .contenido{
        color: white;
    }
    .inscritos{
        color:white;
        background-color: teal;
        padding: 8px;
    }
    .tabla{
        width:80%; 
        text-align: center; 
        margin-right: auto; 
        margin-left: auto;
        padding: 15px;
    }
    h1,h2{
        text-align:center;
        padding:8px;
    }
    </style>
    <body class="cuerpo">
    <div class="titulo">
    <h1>Reportes</h1></div>"""

    inicio+="<div><h2>Tabla de Tokens</h2>"

    inicio+="<div class=\"tabla\"><table class=\"table table-dark table-hover\">"
    inicio+="""<thead><tr>
    <th scope="col">No.</th>
    <th scope="col">TOKEN</th>
    <th scope="col">LEXEMA</th>
    <th scope="col">FILA</th>
    <th scope="col">COLUMNA</th>
    </tr></thead><tbody>"""
            
    for i in range(len(Tokens)):
        inicio+="<tr>"
        inicio+="<th scope=\"row\">"+str(i+1)+"</th>"
        inicio+="<td>"+Tokens[i].token+"</td>"
        inicio+="<td>"+Tokens[i].lexema+"</td>"
        inicio+="<td>"+str(Tokens[i].fila)+"</td>"
        inicio+="<td>"+str(Tokens[i].columna)+"</td>"
        inicio+="</tr>"
            
    inicio+="</tbody></table></div></div>"
    #------------------------------------------------------------------------------------------------
    inicio+="<div><h2>Tabla de Errores</h2>"

    inicio+="<div class=\"tabla\"><table class=\"table table-dark table-hover\">"
    inicio+="""<thead><tr>
    <th scope="col">No.</th>
    <th scope="col">FILA</th>
    <th scope="col">COLUMNA</th>
    <th scope="col">CARACTER</th>
    <th scope="col">OBSERVACION</th>
    </tr></thead><tbody>"""
            
    for i in range(len(Errores)):
        inicio+="<tr>"
        inicio+="<th scope=\"row\">"+str(i+1)+"</th>"
        inicio+="<td>"+str(Errores[i].fila)+"</td>"
        inicio+="<td>"+str(Errores[i].columna)+"</td>"
        inicio+="<td>"+Errores[i].caracter+"</td>"
        inicio+="<td>"+Errores[i].observacion+"</td>"
        inicio+="</tr>"
            
    inicio+="</tbody></table></div></div>"




    fin="""
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
    </body>
    </html>"""
    f.write(inicio+fin)
    f.close()
    startfile("Reporte.html")

def generarImagenHTML(imagen):
    inicio="""<!doctype html>
        <html lang="en">
        <head>
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
        <style>
        table, td, th {
            border: 1px solid black;
        }

        table {
        border-collapse: collapse;
        }
        </style>
        </head>
        <body>
    """
    contenido=""
    contenido+=f"<table border=\"1\" width=\"{str(imagen.ancho)}\" height=\"{str(imagen.alto)}\">"
    for j in range(imagen.filas):
        contenido+="<tr>\n"
        for i in range(imagen.columnas):
            color=imagen.buscar(i,j)
            if color=="":
                contenido+="<td></td>\n"
            else:
                contenido+=f"<td style=\"background-color:{color}\"></td>\n"
        contenido+="</tr>\n"
    contenido+="</table>\n</body>\n</html>"
    documento=open("prueba.html","w",encoding="utf8")
    documento.write(inicio+contenido)
    documento.close()


def verImagen():
    global combo,Imagenes
    nombre=combo.get()
    if nombre=="" or nombre=="Seleccione una imagen":
        print("actualmente vacio")
    else:
        for i in Imagenes:
            if nombre==i.titulo:
                print(nombre)
                generarImagenHTML(i)
        
    

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