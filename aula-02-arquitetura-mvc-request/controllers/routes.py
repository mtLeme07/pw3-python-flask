from flask import render_template, request, redirect, url_for

jogadores= ['Matheus', 'Larissa', 'Kenzo', 'Fred Barbosa', 'Kanisu']

# Array de Objetos
gamelist = [
    {
        'titulo': 'Rimworld',
        'ano': 2018,
        'categoria': 'Gerenciamento (Simulador de Côlonia)',
    },
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

    @app.route("/games", methods=['GET', 'POST'])
    #Cria uma função
    def games():
        game = gamelist[0]
        

        if request.method == 'POST':
            if request.form.get('Jogador'):
                #.append adiciona um item ao array
                jogadores.append(request.form.get('Jogador'))
                
            

        games = ['CS 2', 'Team Fortress 2', 'Gmod', 'Dwarf Fortress', 'Stardew Valley', 'Dead by Daylight']
        return render_template('games.html', 
                               game=game,
                               jogadores=jogadores,
                               games=games
        )

#Rota de cadastro de jogos (em dicionario)
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        
        if request.method == 'POST':            
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                
                gamelist.append({'titulo': request.form.get('titulo'),
                                 'ano': request.form.get('ano'),
                                 'categoria': request.form.get('categoria')
                                 })
            return  redirect(url_for('cadgames'))
        
        return render_template('cadgames.html',
                               gamelist=gamelist,
                               )
    
#Rota de casdastro de consoles:
    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        
        if request.method == 'POST':            
            if request.form.get('nome') and request.form.get('ano') and request.form.get('fabricante') and request.form.get('preco'):
                
                consolelist.append({'nome': request.form.get('nome'),
                                 'ano': request.form.get('ano'),
                                 'fabricante': request.form.get('fabricante'),
                                 'preco': request.form.get('preco')
                                 })
            return  redirect(url_for('consoles'))
        
        return render_template('consoles.html',
                               consolelist=consolelist)                                                                                                                                                                                            
        