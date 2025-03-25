#Importa o Flask:
from flask import Flask, render_template

from controllers import routes

#cria uma variavel "app", aonde o Flask é carregado:
app = Flask(__name__, template_folder='views')

#Chamando as rotas
routes.init_app(app)

#Inicia o servidor no localhost: (com debug)
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

#

