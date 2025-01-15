import csv


t = dict()
data = dict()
with open('estoque_locais.csv', 'r') as filecsv:
    for i,row in enumerate(csv.DictReader(filecsv)):
        t = {
            "name":row.get("Nome"),
            "quantidade":row.get(" Quantidade(unidade)"),

        }
        # print(t)
        data[i] = t.copy()
        t.clear()
        
from pprint import pprint as print
print(data)