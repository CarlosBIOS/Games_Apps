from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            "<p>This is a paragraph</p><br>"
            "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2ZoeHg5NDBmMXk5Y2kzb215Nno5aG5wMmQyOXo3dWRmb"
            "TIzYzlvYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DxX2ToxuJ1fkynLf9I/giphy.webp' width=700>")


def make_bold(function):
    def bold():
        message = function()
        return f'<b>{message}</b>'
    return bold


def italic_decorator(function):
    def wrapper_function():
        fresult = function()
        return f"<em>{fresult}</em>"
    return wrapper_function


def make_underline(function):
    def underline():
        message = function()
        return f'<u>{message}</u>'
    return underline


@app.route("/bye")
@make_bold
@italic_decorator
@make_underline
def say_bye():
    return "<p>Bye!</p>"


@app.route('/username/<name>/<int:number>')
def greet(name: str, number: int):
    return f'<p>Hello {name.title()}. You are {number} years old!</p>'


@app.route('/age/<path:age>')
def agee(age: str):
    return f'<p>Hello {age.title()}!</p>'


if __name__ == '__main__':
    # app.run() -> Não dá para fazer alterações enquanto executa
    app.run(debug=True)
