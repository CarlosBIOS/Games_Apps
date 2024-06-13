from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, high_score):
        super().__init__()
        self.score = 0
        self.high_score = high_score
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.write(f'score = {self.score}  High Score: {self.high_score}', align='center', font=('Arial', 17, 'normal'))
        self.hideturtle()

    def up_score(self):
        self.clear()
        self.score += 1
        self.write(f'score = {self.score}  High Score: {self.high_score}', align='center',
                   font=('Arial', 17, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', 'w', encoding='utf-8') as file_input:
                print(self.high_score, file=file_input)
        self.score = 0
        self.up_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f'GAME OVER', align='center', font=('Arial', 17, 'normal'))
