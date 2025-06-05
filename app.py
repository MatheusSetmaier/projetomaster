
from flask import Flask, render_template, request, redirect
from db import get_connection

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/inserir', methods=['POST'])
def inserir():
    
    nome = request.form.get('nome')

    if not nome:
        return "Erro: nome não pode estar vazio", 400

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome) VALUES (%s)", (nome,))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')
    except Exception as e:
        return f"Erro ao inserir no banco: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
