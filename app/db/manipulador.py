import sqlite3

db = r"app/db/db.sqlite"
con = sqlite3.connect(db)
cursor = con.cursor()

class BancoDeDados():
    def __init__(self):
        pass

    def criar_fornecedores(self):
        cursor.execute("""CREATE TABLE IF NOT EXISTS fornecedores (
                    id INTEGER PRIMARY KEY,
                    nome_fornecedor TEXT NOT NULL,
                    nome_produto TEXT NOT NULL,
                    numero_de_contato TEXT NOT NULL)""")
        
    def excluir_todos_dados(self, nome_tabela):
        while True:
            resultado = input(f'Tem certeza que deseja excluir todos os dados da tabela "{nome_tabela}" (S/N): ').upper().strip()
            if resultado == 'S':
                try:
                    cursor.execute(f"""DELETE FROM {nome_tabela}""")
                except:
                    print('Tabela não encontrada.')
                    break
                else:
                    print(f'Dados da tabela "{nome_tabela}" foram excluídos com Sucesso.')
                    break
            elif resultado == 'N':
                break
            else:
                print('Escolha inválida. Tente novamente.')

    def excluir_tabela(self, nome_tabela):
        while True:
            resultado = input(f'Tem certeza que deseja excluir a tabela "{nome_tabela}" do banco de dados (S/N): ').upper().strip()
            if resultado == 'S':
                try:
                    cursor.execute(f"""DROP TABLE {nome_tabela}""")
                except:
                    print('Tabela não encontrada.')
                    break
                else:
                    print(f'Tabela "{nome_tabela}" excluída com Sucesso.')
                    break
            elif resultado == 'N':
                break
            else:
                print('Escolha inválida. Tente novamente.')
        

BancoDeDados().criar_fornecedores()