import sqlite3

db = r"app/db/db.sqlite"

class Fornecedores:
    def __init__(self):
        pass

    def ler(self):
        def fetch_all_as_dict(cursor):
            colunas = [col[0] for col in cursor.description]
            return [dict(zip(colunas, row)) for row in cursor.fetchall()]
        
        with sqlite3.connect(db) as con:
            cursor = con.cursor()
            cursor.execute("""SELECT ROW_NUMBER() OVER (ORDER BY nome_fornecedor) AS ID, 
            nome_fornecedor, 
            nome_produto, 
            numero_de_contato
            FROM fornecedores;""")
            resultado = fetch_all_as_dict(cursor)
            return resultado
        
    def inserir(self, nome_fornecedor, nome_produto, numero_de_contato):
        with sqlite3.connect(db) as con:
            cursor = con.cursor()
            cursor.execute("""INSERT INTO fornecedores (nome_fornecedor, nome_produto, numero_de_contato)
                        VALUES (?, ?, ?)""", (nome_fornecedor, nome_produto, numero_de_contato))
            con.commit()
        
print(Fornecedores().ler())