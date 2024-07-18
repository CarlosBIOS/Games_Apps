from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/")
def home():
    return ("<h1 style='text-align: center'>Guess a number between 1 and 10</h1>"
            "<img src='https://i.giphy.com/3o7aCSPqXE5C6T8tBC.webp' width=500>")


def guess_number(function):
    def number_guess(**kargs):
        number: int = randint(1, 10)
        number_user = function(kargs)['number']
        print(number_user)
        if number_user == number:
            return ('<h1 style="color: green">You found me!</h1>'
                    '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=500>')
        elif number_user < number:
            return ('<h1 style="color: red">Too low. Try again!</h1>'
                    '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=500>')
        else:
            return ('<h1 style="color: purple">Too high. Try again!</h1>'
                    '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=500>')
    return number_guess


@app.route('/<int:number>')
@guess_number
def guess(number: int):
    return number


if __name__ == '__main__':
    # app.run() -> Não dá para fazer alterações enquanto executa
    app.run(debug=True)
