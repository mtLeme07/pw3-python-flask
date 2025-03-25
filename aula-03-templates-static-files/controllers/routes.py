from flask import render_template, request, redirect, url_for

# Array de Objetos
game = [
    {
        'titulo': 'Rimworld',
        'ano': 2018,
        'categoria': 'Gerenciamento (Simulador de Côlonia)'
    },
    {
        'titulo': 'Rimworld',
        'ano': 2018,
        'categoria': 'Gerenciamento (Simulador de Côlonia)'
    }
    ]
consolelist=[{
    'nome':'Xbox 360',
    'fabricante':'Microsoft',
    'ano':2007,
    'preco':360
}]
def init_app(app):
    # Cria a primeira rota do site
    @app.route("/")
    #Cria uma função
    def home():
        return render_template('index.html')
  

    @app.route("/games")
    def games():
        return render_template('games.html',
                               game=game)
    

    @app.route("/cadgames")
    def cadgamesp():
        return render_template('cadgames.html')