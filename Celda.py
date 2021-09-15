class celda:
    def __init__(self,x,y,pintado,color):
        self.x=x
        self.y=y
        if pintado=="TRUE":
            self.pintado=True
        elif pintado=="FALSE":
            self.pintado=False
        self.color=color