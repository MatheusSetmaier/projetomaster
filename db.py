
import mysql.connector

def get_connection():
    
    return mysql.connector.connect(
        host='teste.hiperconnect.me',
        port=8500,
        user='master',
        password='Teste@Master',
        database='banco_matheus'
    )
