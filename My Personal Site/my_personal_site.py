# todo Em certos browsers, quando entro num website, o browser instala o styles.css e outras items que são importantes
#  para o site. Pois se formos outra vez para esse site no mesmo dia, vai abrir o q intalá-mos. Por um lado é excelente,
#  pois não é preciso instalar os items sempre que abrirmos o site, mas por outro, se fizermos alguma alteração no
#  styles.css, por exemplo, e se atualizarmos a página, a página vai continuar com o antigo styles.css. Para atualizar
#  direito, tenho que carregar em shift + o botão de atualizar!!!

# todo Se quiser fazer altereções diretamente no chrome, posso ir à console no inspecionar elementos e escrever:
#   document.body.contentEditable=true
#   Faço as alterações e dps instalo o html e substituo no templates
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    # https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
    # Eu sou mesmo obrigado a criar os folders: static e templates. Pois, como flask its a infrastructure e não a
    # library, flask tem regras, e uma dessas regras é se tiver algum ficheiro static ou algum html, tenho que colocar
    # dentro desses fodlers!!!
    return render_template('index2.html')


if __name__ == '__main__':
    app.run(debug=True)
