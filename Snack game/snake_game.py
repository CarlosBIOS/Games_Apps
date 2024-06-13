from turtle import Screen
from snake_class import Snake
from food import Food
from scoreboard import ScoreBoard
from pygame import init, mixer
import time
from os import path

# todo: Para criar o Aplicativo, tenho qu executar este código:
#  pyinstaller --onefile --windowed --add-data="Zero to Hero.mp3;." snake_game.py


def create_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('My Snake Game')
    screen.tracer(0)  # Serve para 'desligar' o screen, ou seja, se não escrever screen.update() não vai aparecer nada
    # que coloquei dps deste código na screen!!!
    return screen


if not path.exists('high_score.txt'):
    with open('high_score.txt', 'w', encoding='utf-8') as file_output:
        high_score = 0
        print(high_score, file=file_output)
else:
    with open('high_score.txt', encoding='utf-8') as file_input:
        high_score = int(file_input.readline())


def main():
    init()
    mp3_file = path.join(path.dirname(__file__), "Zero to Hero.mp3")
    mixer.music.load(mp3_file)
    # musica.play(-1) # Num loop
    mixer.music.play(0)
    snake_object = Snake()
    food = Food()
    score = ScoreBoard(high_score)

    screen = create_screen()
    screen.listen()
    screen.onkey(snake_object.up, 'Up')
    screen.onkey(snake_object.down, 'Down')
    screen.onkey(snake_object.left, 'Left')
    screen.onkey(snake_object.right, 'Right')
    screen.onkey(snake_object.up, 'w')
    screen.onkey(snake_object.down, 's')
    screen.onkey(snake_object.left, 'a')
    screen.onkey(snake_object.right, 'd')

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.05)

        snake_object.move_snake()

        if snake_object.head.distance(food) < 15:
            snake_object.aumentar_snake()
            food.new_location()
            score.up_score()

        if (snake_object.head.ycor() < -290 or snake_object.head.xcor() > 290 or snake_object.head.xcor() < -290 or
                snake_object.head.ycor() > 290):
            score.reset()
            snake_object.reset()

        for segment in snake_object.snake_body[1:]:
            if snake_object.head.distance(segment) < 10:
                score.reset()
                snake_object.reset()

        # if not mixer.music.get_busy():
        #     tocar_proxima_musica(musicas)  # Carregue a próxima música quando a atual terminar

    else:
        mixer.music.stop()

    screen.exitonclick()


if __name__ == '__main__':
    main()
