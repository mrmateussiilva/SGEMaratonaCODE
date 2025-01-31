import json

db = r"app/db/db_fornecedores.json"

class Fornecedores:
    def __init__(self):
        pass
    
    def salvar(self,fornecedores):
        with open(db, "w", encoding="utf-8") as file:
            json.dump(fornecedores, file, indent=4, ensure_ascii=False)

    def ler(self):    
        with open(db, 'r') as file:
            db = json.load(file)
            file.close()

        return db