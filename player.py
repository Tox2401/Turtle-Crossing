from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.shapesize(0.5, 0.5, None)
        self.setheading(90)
        self.penup()
        self.goto(0, -280)
        
        
    def move(self):
        self.forward(20)