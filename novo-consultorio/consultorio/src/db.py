import sqlite3

def conectar():
    conn = sqlite3.connect("consultorio.db")
    return conn
