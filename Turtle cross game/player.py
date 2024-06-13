from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move_up(self):
        if self.ycor() < FINISH_LINE_Y:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(x=self.xcor(), y=new_y)

    def move_left(self):
        if self.xcor() > -FINISH_LINE_Y:
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(x=new_x, y=self.ycor())

    def move_right(self):
        if self.xcor() < FINISH_LINE_Y:
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(x=new_x, y=self.ycor())
