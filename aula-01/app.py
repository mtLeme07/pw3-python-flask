#Importa o Flask:
from flask import Flask

#cria uma variavel "app", aonde o Flask é carregado:
app = Flask(__name__)

# Cria a primeira rota do site
@app.route("/")
#Cria uma função
def home():
    return '<h1>Bem-vindo aaaaazaaaaaaaaaaaaaaa</h1>'


#Inicia o servidor no localhost: (com debug)
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

#

