import time
from turtle import Screen
from player import Player, FINISH_LINE_Y, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()


screen.listen()
screen.onkey(player.move_up, "Up")


cars= CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()

    # DETECT WHEN REACHED TOP 
    if player.ycor() > FINISH_LINE_Y:
        player.goto(STARTING_POSITION)
        cars.inc_speed()
        scoreboard.increase_score()
    
    # DETETCT COLLISION WITH CAR:

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

            

screen.exitonclick()