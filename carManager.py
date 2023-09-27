from turtle import Turtle
import random

COLORS = ["tomato", "royal blue", "lime green", "orange red", "gold", "hot pink"]

class CarManager:
    
    def __init__(self):
        self.cars = []
        
    
    def makeLanes(self):
        lanes = []
        direction = 1
        for i in range(-240, 240, 40):
            lanes.append(((-400 * direction), i))
            direction *= -1
            
        return lanes
    
    def spawnCar(self, cars):
        lanes = self.makeLanes()
        car = Turtle("square")
        car.hideturtle()
        car.penup()
        car.shapesize(1, 2, None)
        car.color(random.choice(COLORS))
        car.goto(random.choice(lanes))
        car.showturtle()
        if car.xcor() == 400:
            car.setheading(180)
        
        cars.append(car)
            
    def moveCars(self, Cars):
        for car in Cars:
            car.forward(20)
            
    def cleanse(self, cars):
        for car in cars:
            if car.xcor() > 420 or car.xcor() < -420:
                car.hideturtle()
                cars.remove(car)