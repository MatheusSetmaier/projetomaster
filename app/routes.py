from flask import Blueprint, render_template, request
from .db import get_connection

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return "✅ Aplicação rodando!"

@routes.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        nome = request.form['nome']
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (nome) VALUES (%s)", (nome,))
            conn.commit()
            return f"Nome '{nome}' inserido com sucesso!"
        except Exception as e:
            return f"Erro ao inserir: {e}"
    return render_template('form.html')

@routes.route('/db')
def testar_banco():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tabelas = cursor.fetchall()
        return f"Tabelas: {tabelas}"
    except Exception as e:
        return f"Erro: {e}"

