# todo Em certos browsers, quando entro num website, o browser instala o styles.css e outras items que são importantes
#  para o site. Pois se formos outra vez para esse site no mesmo dia, vai abrir o q intalá-mos. Por um lado é excelente,
#  pois não é preciso instalar os items sempre que abrirmos o site, mas por outro, se fizermos alguma alteração no
#  styles.css, por exemplo, e se atualizarmos a página, a página vai continuar com o antigo styles.css. Para atualizar
#  direito, tenho que carregar em shift + o botão de atualizar!!!

# todo Se quiser fazer altereções diretamente no chrome, posso ir à console no inspecionar elementos e escrever:
#   document.body.contentEditable=true
#   Faço as alterações e dps instalo o html e substituo no templates

# Ver jinja Documentation: Explica tudo sobre dynamical variables
# https://jinja.palletsprojects.com/en/2.11.x/templates/
from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    # https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
    # Eu sou mesmo obrigado a criar os folders: static e templates. Pois, como flask its a infrastructure e não a
    # library, flask tem regras, e uma dessas regras é se tiver algum ficheiro static ou algum html, tenho que colocar
    # dentro desses fodlers!!!
    random_number: int = randint(0, 1000)
    data_time = datetime.now().strftime('%d-%m-%Y')
    # Atenção, eu próprio chamei de num, mas se quisesse, podia chamar de número, etc.
    return render_template('index3.html', num=random_number, date=data_time)


@app.route('/guess/<name>')
def information(name: str):
    parameters: dict = {
        'name': name.title()
    }

    idade = requests.get('https://api.agify.io', params=parameters).json()['age']
    gender = requests.get('https://api.genderize.io', params=parameters).json()['gender']

    return render_template('index4.html', idade=idade, name=name.title(), gender=gender)


@app.route('/blog')
def get_blog():
    texts = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()

    return render_template('index5.html', posts=texts)


if __name__ == '__main__':
    app.run(debug=True)
