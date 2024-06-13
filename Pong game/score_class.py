from turtle import Turtle


class ScorePong(Turtle):

    def __init__(self):
        super().__init__()
        self.my_score = 0
        self.score_enemy = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=250)
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.write(f'{self.my_score}\t{self.score_enemy}', align='center', font=('Arial', 30, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        if self.my_score == 7:
            self.write(f'YOU WIN!', align='center', font=('Arial', 25, 'normal'))
        else:
            self.write(f'GAME OVER', align='center', font=('Arial', 26, 'normal'))
