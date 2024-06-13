from turtle import Turtle

POSITIONS: list = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(object):

    def __init__(self):
        self.snake_body: list = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self) -> None:
        for index in POSITIONS:
            self.add_segment(index)

    def add_segment(self, position):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)

    def aumentar_snake(self):
        self.add_segment(self.snake_body[-1].position())

    def move_snake(self):
        for snake_index in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake_index - 1].xcor()
            new_y = self.snake_body[snake_index - 1].ycor()
            self.snake_body[snake_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def change_direction(self, direction):
        if (self.head.heading() - direction) % 180 != 0:  # Prevent immediate backtracking
            self.head.setheading(direction)

    def up(self):
        self.change_direction(UP)

    def down(self):
        self.change_direction(DOWN)

    def left(self):
        self.change_direction(LEFT)

    def right(self):
        self.change_direction(RIGHT)

    def reset(self):
        for snake in self.snake_body:
            snake.hideturtle()
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
