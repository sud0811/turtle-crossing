from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        

    def create_car(self):
        if random.randint(1,6)==1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            new_y = random.randint (-250, 250)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for cars in self.all_cars:
            cars.backward(self.speed)

    def inc_speed(self):
        self.speed = self.speed + MOVE_INCREMENT


