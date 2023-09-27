from turtle import Turtle

class Road(Turtle):
    
    def __init__(self):
        super().__init__()
        lanes = [(-400, -240), (-400, -200)]
        self.color("white")
        self.width(5)
        self.hideturtle()
        self.penup()
        self.goto(-380, -260)
        self.drawLaneLines()
        
    
    def drawLaneLines(self):
        for i in range(-260, 260, 80):
            self.goto(-380, i)
            for j in range(0, 10):
                self.pendown()
                self.forward(59)
                self.penup()
                self.forward(19)