from turtle import Screen
from player import Player
from road import Road
from carManager import CarManager
import time

level = 1
difficulty = [0.1, 0.08, 0.07, 0.06, 0.05, 0.045, 0.04,
              0.035, 0.03, 0.025, 0.0225, 0.02, 0.0175,
              0.015, 0.0125, 0.01, 0.0075, 0.005, 0.0025, 0.002]

screen = Screen()
screen.title(f"Turtle Crossing - Level: {level}")
screen.setup(800, 600)
screen.tracer(0)
screen.bgcolor("black")

screen.listen()

player = Player()
road = Road()
carManager = CarManager()


screen.onkeypress(player.move, "w")

gameOn = True

while gameOn:
    
    screen.update()
    time.sleep(difficulty[level - 1])
    
    if len(carManager.cars) < 25:
        carManager.spawnCar(carManager.cars)
    carManager.moveCars(carManager.cars)
    carManager.cleanse(carManager.cars)
    
    for car in carManager.cars:
        if player.distance(car) < 10:
            gameOn = False
            
    if player.ycor() > 280:
        level += 1
        if level == 20:
            gameOn = False
        screen.clearscreen
        screen.title(f"Turtle Crossing - Level: {level}")
        player.goto(0, -280)

screen.title(f"Turtle Crossing - CONGRATULATIONS!!!!")
screen.exitonclick()