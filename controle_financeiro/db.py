import sqlite3

#conectando ao banco de dados
conn = sqlite3.connect("financeiro.db")
cursor = conn.cursor()

# cria as tabelas se não tiverem sido criadas
cursor.execute("""
create table if not exists receitas (
               id interger primary key autoincrement,
               descricao TEXT NOT NULL,
               valor REAL NOT NULL,
               data TEXT NOT NULL               
               )""")
cursor.execute("""
create table if not exists DESPESAS (
               id interger primary key autoincrement,
               descricao TEXT NOT NULL,
               valor REAL NOT NULL,
               data TEXT NOT NULL               
               )""")
conn.commit()
# funçoes
def adicionar_receita(descricao, valor, data):
    cursor.execute("INSERT INTO receitas (descricao, valor, data) VALUES (?,?,?)",(descricao, valor, data)
                   
                   )
