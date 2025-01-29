import json

def LerFornecedores():    
    with open('app/db/fornecedores.json', 'r') as file:
        db = json.load(file)
        file.close()

    return db

def SalvarFornecedores(fornecedores):
    with open("app/db/fornecedores.json", "w", encoding="utf-8") as f:
        json.dump(fornecedores, f, indent=4, ensure_ascii=False)