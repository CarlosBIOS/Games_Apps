from turtle import Turtle, Screen


def move_fowards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def clear_paint():
    tim.clear()
    tim.teleport(x=0, y=0)


tim = Turtle()

screen = Screen()

screen.listen()
screen.onkey(key='w', fun=move_fowards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='c', fun=clear_paint)

screen.exitonclick()
