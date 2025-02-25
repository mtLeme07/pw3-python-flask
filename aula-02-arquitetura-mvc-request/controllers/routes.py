from flask import render_template, request

jogadores= ['Matheus', 'Larissa', 'Kenzo', 'Fred Barbosa', 'Kanisu']


def init_app(app):
    # Cria a primeira rota do site
    @app.route("/")
    #Cria uma função
    def home():
        return render_template('index.html')

    @app.route("/games", methods=['GET', 'POST'])
    #Cria uma função
    def games():

        # Dicionario (Objeto) em python
        jogo = {
        'titulo': 'Rimworld',
        'ano': 2018,
        'categoria': 'Gerenciamento (Simulador de Côlonia)',
    }

        if request.method == 'POST':
            if request.form.get('jogador'):
                #.append adiciona um item a o array
                jogadores.append(request.form.get('jogador'))
                
            

        jogos = ['CS 2', 'Team Fortress 2', 'Gmod', 'Dwarf Fortress', 'Stardew Valley', 'Dead by Daylight']
        return render_template('games.html', 
                               jogo=jogo,
                               jogadores=jogadores,
                               jogos=jogos
        )
