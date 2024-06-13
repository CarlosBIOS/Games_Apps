from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

user_guess: str | None = screen.textinput('Make your bet', 'Which turtle will win the race? Enter a color: ')
colors_positions: list = [('red', -70), ('orange', -40), ('yellow', -10), ('green', 20), ('blue', 50), ('purple', 80)]
all_turtles: list = []

for color, position in colors_positions:
    tim = Turtle(shape='turtle')
    tim.speed('slowest')
    tim.penup()
    tim.color(color)
    tim.goto(x=-240, y=position)
    all_turtles.append(tim)

is_on = True
while is_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))

        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_guess:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
            is_on = False
            break

screen.exitonclick()
