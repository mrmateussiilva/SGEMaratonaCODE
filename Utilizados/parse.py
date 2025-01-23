import csv
import json

t = dict()
data = dict()
with open('estoque_tintas.csv', 'r') as filecsv:
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

with open('EstoqueTintasDB.json', 'w') as file:
    json.dump(data, file, indent=4)