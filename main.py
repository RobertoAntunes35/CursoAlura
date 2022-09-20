from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
        
app = Flask(__name__)

@app.route('/inicio')
def helloWord():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('God of War', 'Rack on Slash', 'PS2')
    
    lista = [jogo1, jogo2]
    return render_template('index.html', titulo = 'Jogos', jogos=lista)

app.run(port=8080)
