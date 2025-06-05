from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = []

@app.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)

@app.route('/add', methods=['POST'])
def add():
    titulo = request.form['titulo']
    if titulo:
        tarefas.append({'titulo': titulo, 'feito': False})
    return redirect(url_for('index'))

@app.route('/concluir/<int:indice>')
def concluir(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]['feito'] = not tarefas[indice]['feito']
    return redirect(url_for('index'))

@app.route('/remover/<int:indice>')
def remover(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)