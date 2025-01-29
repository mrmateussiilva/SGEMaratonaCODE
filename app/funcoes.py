import json

def Fornecedores():    
    with open('app/db/fornecedores.json', 'r') as file:
        db = json.load(file)
        file.close()

    return db