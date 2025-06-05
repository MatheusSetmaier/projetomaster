import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",     
        port=3307,            
        user="master",
        password="Teste@Master",
        database="banco-matheus"
    )
