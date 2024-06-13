from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.y_move: int = -5
        self.x_move: int = -10
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        if self.ycor() >= 280:
            self.y_move = -5

        elif self.ycor() <= -280:
            self.y_move = 5

        self.goto(x=new_x, y=new_y)
