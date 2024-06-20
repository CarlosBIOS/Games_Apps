from quiz_brain import QuizBrain
from main import quiz
from tkinter import Tk, Button, Label, PhotoImage, StringVar


class QuizzInterface:

    def __init__(self, quizz_brain: QuizBrain):
        self.quiz = quizz_brain
        self.THEME_COLOR = "#375362"

        self.window = Tk()
        self.window.config(bg=self.THEME_COLOR, padx=20, pady=20)
        self.window.title('Quizzler')

        self.score_label = Label(text=f'Score: {self.quiz.score}', bg=self.THEME_COLOR, fg='white', font=('normal', 12))
        self.score_label.grid(row=0, column=1, sticky='e')
        self.text = StringVar()

        self.question_label = Label(textvariable=self.text, bg='white', font=('Arial', 20, 'italic'),
                                    fg=self.THEME_COLOR, width=40, height=15, wraplength=550)
        self.question_label.grid(row=1, column=0, columnspan=2)

        self.true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=self.true_image, command=self.button_right, highlightthickness=False, bg=self.THEME_COLOR)
        self.true_button.grid(row=2, column=0, sticky='s')

        self.false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_image, command=self.button_false, highlightthickness=False, bg=self.THEME_COLOR)
        self.false_button.grid(row=2, column=1, sticky='s')

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_label.config(bg='white')
        self.score_label.config(text=f'Score: {self.quiz.score}')
        q_text = self.quiz.next_question()
        self.text.set(q_text)

    def button_right(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def button_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.question_label.config(bg='green')
        else:
            self.question_label.config(bg='red')

        self.window.after(1000, self.get_next_question)


QuizzInterface(quiz)
