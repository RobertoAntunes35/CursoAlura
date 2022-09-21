from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack on Slash', 'PS2')
lista = [jogo1, jogo2]  

app = Flask(__name__)
app.secret_key = 'alura'


@app.route('/')
def index(): 
    return render_template('index.html', titulo = 'Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = 'Criação Jogos')

@app.route('/criar', methods= ['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogos = Jogo(nome, categoria, console)
    lista.append(jogos)
    return redirect('/')
 
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods = ['POST', ])
def autenticar():
    if 'alohomora'==request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash('Bem Vindo %s' % request.form['usuario'])
        return redirect('/')
    else:
        flash('Erro na autenticação !')
        return redirect('/login')


app.run(debug = True)
