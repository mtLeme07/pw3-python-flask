from flask import render_template, request, redirect, url_for
from models.database import Game, Console, db

# Lista de jogadores
jogadores = ['Miguel José', 'Miguel Isack', 'Leaf',
             'Quemario', 'Trop', 'Aspax', 'maxxdiego']

# Array de objetos - Lista de games
gamelist = [{'Título': 'CS-GO',
            'Ano': 2012,
             'Categoria': 'FPS Online'}]


def init_app(app):
    # Criando a primeira rota do site
    @app.route('/')
    # Criando função no Python
    def home():
        return render_template('index.html')

    # Rota de games
    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gamelist[0]
        # Tratando se a requisição for do tipo POST
        if request.method == 'POST':
            # Verificar se o campo 'jogador' existe
            if request.form.get('jogador'):
                # O append adiciona o item a lista
                jogadores.append(request.form.get('jogador'))
            return redirect(url_for('games'))

        jogos = ['Jogo 1', 'Jogo 2', 'Jogo 3', 'Jogo 4', 'Jogo 5', 'Jogo 6']
        return render_template('games.html',
                               game=game,
                               jogadores=jogadores,
                               jogos=jogos)
    
    # Rota de cadastro de jogos (em dicionário)
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Título' : request.form.get('titulo'), 'Ano' : request.form.get('ano'), 'Categoria' : request.form.get('categoria')})
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html',
                               gamelist=gamelist)
    
    @app.route('/estoque', methods=['GET', 'POST']) #ACESSAR PAGINA = GET
    @app.route('/estoque/<int:id>')
    def estoque(id=None):
        if id:
                game=Game.query.get(id)
                db.session.delete(game)
                db.session.commit()
                return redirect(url_for('estoque'))
        # = - Atribuição
        # == - Comparação Simples (apenas o valor)
        # === - Comparação Complexa (valor e tipo)
        if request.method == 'POST':
                newgame = Game(request.form['titulo'],
                           request.form['ano'],
                           request.form['categoria'],
                           request.form['plataforma'],
                           request.form['preco'],
                           request.form['quantidade'],)
                db.session.add(newgame)
                db.session.commit()
                return redirect(url_for('estoque'))
        gameestoque = Game.query.all()
        return render_template('estoque.html', gameestoque = gameestoque)
    
    @app.route('/estoqueconsole', methods=['GET','POST'])
    @app.route('/estoqueconsole/<int:id>')
    def estoqueconsole(id=None):
        if id:
                console=Console.query.get(id)
                db.session.delete(console)
                db.session.commit()
                return redirect(url_for('estoqueconsole'))
        if request.method == 'POST':
            newconsole = Console(
                    request.form['nome'],
                    request.form['fabricante'],
                    request.form['preco'],
                    request.form['quantidade'],)
            db.session.add(newconsole)            
                 # Confirmando as alterações
            db.session.commit()
            return redirect(url_for('estoqueconsole'))
        consoleestoque = Console.query.all()
        return render_template('estoqueconsole.html', consoleestoque = consoleestoque)
        
    @app.route('/editConsole/<int:id>', methods=['GET', 'POST'])
    def editConsole(id):
        console = Console.query.get(id)
        
        if request.method == "POST":
            console.nome = request.form['nome']
            console.fabricante = request.form['fabricante']
            console.preco = request.form['preco']
            console.quantidade = request.form['quantidade']
            
            db.session.commit()
            
            return redirect(url_for('estoqueconsole', console=console))
                        
        return render_template('editConsole.html', console=console)

        
