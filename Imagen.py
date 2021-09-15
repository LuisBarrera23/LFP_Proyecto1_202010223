from Celda import celda
class imagen:
    def __init__(self,titulo,ancho,alto,filas,columnas,celdas,filtros):
        self.titulo=titulo
        self.ancho=ancho
        self.alto=alto
        self.filas=filas
        self.columnas=columnas
        self.celdas=celdas
        self.filtros=filtros
    
    def mostrarCeldas(self):
        for cel in self.celdas:
            print(cel.x,cel.y,cel.pintado,cel.color)
        for f in self.filtros:
            print(f)