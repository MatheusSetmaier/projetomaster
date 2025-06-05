from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'master',
    'password': 'Teste@Master',
    'database': 'banco_matheus'
}

# Página inicial com o formulário
@app.route('/')
def formulario():
    return render_template('cadastro.html')

# Rota para tratar a inserção
@app.route('/inserir', methods=['POST'])
def inserir():
    nome = request.form['nome']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = "INSERT INTO clientes (nome) VALUES (%s)"
    cursor.execute(query, (nome,))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
