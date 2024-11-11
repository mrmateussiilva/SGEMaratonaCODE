
from utils import utils
data_estoque = {
    "tecido_locais":utils.load_data("model_csv/estoque_locais.csv"),
    "papeis":utils.load_data("model_csv/estoque_papeis.csv"),
    "tecidos":utils.load_data("model_csv/estoque_papeis.csv"),
    "tintas":utils.load_data("model_csv/estoque_tintas.csv"),
}


TIPOS_PAPEIS = set(map(lambda x:x,data_estoque["papeis"]["Nome"]))
TIPOS_LOCAIS = set(map(lambda x:x,data_estoque["tecido_locais"]["Nome"]))
NOMES_TINTAS = set(map(lambda x:x,data_estoque["tintas"]["Cor"]))
TIPOS_TINTAS = set(map(lambda x:x,data_estoque["tintas"]["Tipo"]))


utils.insert_data(data_estoque["papeis"])
