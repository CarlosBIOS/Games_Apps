# colorgram, serve para return a list of tuples das cores que estão em uma certa foto!!!
import colorgram
from turtle import Turtle, Screen
import random


def main():
    """A função principal!"""
    timmy_the_turtle = Turtle()
    screen = Screen()
    # timmy_the_turtle.shape('turtle')
    timmy_the_turtle.color('red')
    timmy_the_turtle.speed('fastest')

    # for _ in range(4):  # Serve para criar um square
    #     timmy_the_turtle.forward(100)
    #     timmy_the_turtle.left(90)

    # P1: A minha versão, onde tem 50 traços:
    # screen.screensize(500, 500)

    # for index in range(520, -500, -20):
    #     timmy_the_turtle.teleport(-index)
    #     timmy_the_turtle.forward(10)

    # P2: Pela stora, tem 15 traços:
    # for _ in range(15):
    #     timmy_the_turtle.forward(10)
    #     timmy_the_turtle.penup()
    #     timmy_the_turtle.forward(10)
    #     timmy_the_turtle.pendown()

    # Challenge 3: Criar 10 figuras geométricas:
    # a = 3
    # timmy_the_turtle.teleport(0, -100)
    # colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
    #            "SeaGreen"]
    # while a != 11:
    #     timmy_the_turtle.color(random.choice(colours))
    #     for angulo in range(a):
    #         timmy_the_turtle.forward(100)
    #         timmy_the_turtle.left(180 - (((a - 2) * 180) / a))
    #
    #     a += 1

    # for _ in range(36):
    #     timmy_the_turtle.circle(100)
    #     timmy_the_turtle.left(10)

    # The challenge:
    screen.colormode(255)
    screen.screensize(400, 400)
    colors = colorgram.extract('image.jpg', 30)
    colors_list = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        colors_list.append(new_color)

    print(colors_list)

    contar = 0
    y = -210
    timmy_the_turtle.color('white')
    while contar != 10:
        timmy_the_turtle.teleport(-240, y)
        for bola in range(10):
            timmy_the_turtle.dot(20, random.choice(colors_list))
            timmy_the_turtle.penup()
            timmy_the_turtle.forward(50)
            timmy_the_turtle.pendown()
        y += 50
        contar += 1

    screen.exitonclick()


if __name__ == '__main__':
    main()
