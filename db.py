
import mysql.connector

def get_connection():
    
    return mysql.connector.connect(
        host='localhost',
        user='master',
        password='Teste@Master',
        database='banco_matheus'
    )
