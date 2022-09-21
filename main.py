from flask import Flask, render_template, request, redirect, session, flash, url_for
class Jogo:
    
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


class Users:

    def __init__(self, nome, nickname, senha):
        self.nome = nome 
        self.nickname = nickname
        self.senha = senha

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack on Slash', 'PS2')
lista = [jogo1, jogo2]  

usuario1 = Users('RobertoAntunes', 'Roh', 'alohomora')
usuario2 = Users('RobertoSouza', 'Rohzin', 'pao')

usuarios = {
    usuario1.nickname : usuario1,
    usuario2.nickname : usuario2
    }


app = Flask(__name__)
app.secret_key = 'alura'

@app.route('/')
def index(): 
    return render_template('index.html', titulo = 'Jogos', jogos=lista)

@app.route('/novo')
def novo():

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima = url_for('novo')))
    return render_template('novo.html', titulo = 'Criação Jogos')

@app.route('/criar', methods= ['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogos = Jogo(nome, categoria, console)
    lista.append(jogos)
    return redirect(url_for('index'))
 
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods = ['POST', ])
def autenticar():

    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash('Bem Vindo %s' % usuario.nickname)
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Erro na autenticação !')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout Efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(debug = True)
