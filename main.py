import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) #turn off the tracer

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,"w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if random.randint(1,6) == 1:
        car_manager.create_car()
    car_manager.move_car()
    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect succesful crossing
    if player.ycor() >= player.finish_line_y:
        player.return_to_start()
        car_manager.increase_speed()
        scoreboard.increase_level()
screen.exitonclick()