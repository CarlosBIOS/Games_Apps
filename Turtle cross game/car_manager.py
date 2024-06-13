from turtle import Turtle
from random import choice, randint
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed_car = STARTING_MOVE_DISTANCE
        self.list_cars = []
        self.tempo_now = time.time()
        self.tempo = 3

    def create_cars(self):
        if time.time() - self.tempo_now > self.tempo:
            car = Turtle()
            car.shape('square')
            car.shapesize(stretch_len=3, stretch_wid=1)
            car.color(choice(COLORS))
            car.penup()
            car.goto(x=280, y=randint(-100, 230))
            self.list_cars.append(car)
            self.tempo_now = time.time()

    def move_cars(self):
        for index, car in enumerate(self.list_cars):
            new_x = car.xcor() - self.speed_car
            car.goto(x=new_x, y=car.ycor())
            if car.xcor() <= -300:
                del self.list_cars[index]
                car.hideturtle()
