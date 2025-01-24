import tinydb

def save_data(context:str,data:dict) -> None:
    td = tinydb.TinyDB(context)
    td.insert(data)
    

def load_data(context:str) -> None:
    td = tinydb.TinyDB(context)
    return td.all()
    

print(load_data("tintas.json"))
    