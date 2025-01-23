import sqlite3

con = sqlite3.connect('DB.sqlite')

cursor = con.cursor()

cursor.execute("""CREATE TABLE fornecedores(
               Nome var(100),
               descricao var(200),
               produtos var(50),
               contato var(20))""")