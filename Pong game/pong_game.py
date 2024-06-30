from turtle import Screen
from pong_class import Pong
from score_class import ScorePong
from ball_class import Ball
import time
from pygame import init, mixer
from os import path
from threading import Thread


# # todo: Para criar o Aplicativo, tenho qu executar este código:
# #  pyinstaller --onefile --windowed --add-data="Wake Me UP.mp3;." pong_game.py


def create_screen():
    screen = Screen()
    screen.bgcolor('black')
    screen.setup(800, 600)
    screen.title('Pong Game')
    screen.tracer(0)
    return screen


def main():
    init()
    mp3_file = path.join(path.dirname(__file__), "Wake Me UP.mp3")
    mixer.music.load(mp3_file)
    # musica.play(-1) # Num loop
    mixer.music.play(0)
    pong_mine = Pong(-350)
    pong_enemy = Pong(350)
    ball = Ball()
    score = ScorePong()

    screen = create_screen()
    screen.listen()
    screen.onkeypress(pong_mine.up, 'w')
    screen.onkeypress(pong_mine.down, 's')
    # screen.onkeypress(pong_mine.up, 'w')
    # screen.onkeypress(pong_mine.down, 's')
    # Código para multiplayer:
    screen.onkeypress(pong_enemy.up, 'Up')
    screen.onkeypress(pong_enemy.down, 'Down')

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        score.write_score()
        ball.move_ball()

        if pong_mine.distance(ball) < 50:
            ball.x_move = 10
            ball.move_speed *= 0.9
        elif pong_enemy.distance(ball) < 50:
            ball.x_move = -10
            ball.move_speed *= 0.9

        if ball.xcor() <= -400:
            score.score_enemy += 1
            ball.move_speed = 0.1
            ball.goto(x=0, y=0)
            ball.x_move = 10

        elif ball.xcor() >= 400:
            score.my_score += 1
            ball.move_speed = 0.1
            ball.x_move = -10
            ball.goto(x=0, y=0)

        if score.my_score == 7 or score.score_enemy == 7:
            game_is_on = False
    else:
        mixer.music.stop()
        score.game_over()

    screen.exitonclick()


if __name__ == '__main__':
    main()
