#Importa o Flask:
from flask import Flask, render_template

#cria uma variavel "app", aonde o Flask é carregado:
app = Flask(__name__, template_folder='views')

# Cria a primeira rota do site
@app.route("/")
#Cria uma função
def home():
    return render_template('index.html')

@app.route("/games")
#Cria uma função
def games():
    
    # Dicionario (Objeto) em python
    jogo = {
    'titulo': 'Rimworld',
    'ano': 2018,
    'categoria': 'Gerenciamento (Simulador de Côlonia)',
}
    jogadores= ['Matheus', 'Larissa', 'Kenzo', 'Fred Barbosa', 'Kanisu']

    jogos = ['CS 2', 'Team Fortress 2', 'Gmod', 'Dwarf Fortress', 'Stardew Valley', 'Dead by Daylight']
    return render_template('games.html', 
                           jogo=jogo,
                           jogadores=jogadores,
                           jogos=jogos
    )


#Inicia o servidor no localhost: (com debug)
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

#

