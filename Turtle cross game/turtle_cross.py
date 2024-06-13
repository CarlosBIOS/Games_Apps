import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from pygame import init, mixer
from os import path


def create_screen():
    screen = Screen()
    screen.bgcolor('white')
    screen.setup(600, 600)
    screen.title('Turtle Cross Game')
    screen.tracer(0)
    return screen


def main():
    init()
    mp3_file = path.join(path.dirname(__file__), "Uptown Funk.mp3")
    mixer.music.load(mp3_file)
    # musica.play(-1) # Num loop
    mixer.music.play(-1)

    screen = create_screen()
    turtle_object = Player()
    score = Scoreboard()
    cars = CarManager()

    screen.listen()
    screen.onkeypress(turtle_object.move_up, 'w')
    screen.onkeypress(turtle_object.move_left, 'a')
    screen.onkeypress(turtle_object.move_right, 'd')
    screen.onkeypress(turtle_object.move_up, 'Up')
    screen.onkeypress(turtle_object.move_left, 'Left')
    screen.onkeypress(turtle_object.move_right, 'Right')

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        score.write_score()

        cars.create_cars()
        cars.move_cars()

        for car in cars.list_cars:
            if turtle_object.distance(car) < 27:
                score.game_over()
                game_is_on = False

        if turtle_object.ycor() >= 280:
            score.level += 1
            if score.level % 10 == 0:
                cars.speed_car += 2
            turtle_object.goto((0, -280))
            cars.tempo -= cars.tempo * 0.05

    screen.exitonclick()


if __name__ == '__main__':
    main()
