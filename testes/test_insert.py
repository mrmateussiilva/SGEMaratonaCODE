
from utils import load_data,insert_data

data_estoque = {
    "tecido_locais":load_data("model_csv/estoque_locais.csv"),
    "papeis":load_data("model_csv/estoque_papeis.csv"),
    "tecidos":load_data("model_csv/estoque_papeis.csv"),
    "tintas":load_data("model_csv/estoque_tintas.csv"),
}


TIPOS_PAPEIS = set(map(lambda x:x,data_estoque["papeis"]["Nome"]))
TIPOS_LOCAIS = set(map(lambda x:x,data_estoque["tecido_locais"]["Nome"]))
NOMES_TINTAS = set(map(lambda x:x,data_estoque["tintas"]["Cor"]))
TIPOS_TINTAS = set(map(lambda x:x,data_estoque["tintas"]["Tipo"]))


insert_data(data_estoque["tecido_locais"],("Sousplats MALHA - 38x38",20000))
