from turtle import Screen, textinput, Turtle
import pandas
import time
from pygame import mixer, init
from os import path


# def get_mouse_click_coor(x, y):
#     print(x, y)


def create_screen():
    screen = Screen()
    screen.setup(600, 600)
    screen.title('U.S state Game')
    screen.bgpic('blank_states_img.gif')
    screen.tracer(0)
    # screen.onscreenclick(get_mouse_click_coor)
    return screen


def main():
    init()
    mp3_file = path.join(path.dirname(__file__), "This Is America.mp3")
    mixer.music.load(mp3_file)
    # musica.play(-1) # Num loop
    mixer.music.play(0)
    data = pandas.read_csv('50_states.csv')
    screen = create_screen()
    print(data)
    game_is_on = True
    write = 0
    data_values: list = data['state'].to_list()
    print(data_values)
    while game_is_on:
        screen.update()
        time.sleep(1)

        choice_user = textinput(f'{write}/50 States Correct', "What's another state name?").title().strip()
        if choice_user in data_values:
            del data_values[data_values.index(choice_user)]
            state = Turtle()
            state.penup()
            state.hideturtle()
            state_data = data[data.state == choice_user]
            state.goto(int(state_data.x), int(state_data.y))
            state.write(choice_user,  font=("Courier", 7, "normal"))
            write += 1
        elif choice_user in ('0', 'Exit'):
            game_is_on = False

    else:
        mixer.music.stop()


if __name__ == '__main__':
    main()
