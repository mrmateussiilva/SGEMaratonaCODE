import os
import pandas as pd
import csv

def load_data(file):
    if os.path.exists(file):
        return pd.read_csv(file)
    else:
        return pd.DataFrame(columns=["Nome", "Quantidade(unidade)"])




def insert_data(data):
    with open(data, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            print(row)



