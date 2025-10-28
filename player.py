from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 287


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.y_distance = 10
        self.finish_line_y = FINISH_LINE_Y
    def move(self):
        new_y = self.ycor() + self.y_distance
        self.goto(self.xcor(),new_y)
    def return_to_start(self):
        self.goto(STARTING_POSITION)