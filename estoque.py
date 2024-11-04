import streamlit as st
import pandas as pd
import os


estoque_locais = "estoque_locais.csv"
estoque_papeis = "estoque_papeis.csv"


def load_data(file):
    if os.path.exists(file):
        return pd.read_csv(file)
    else:
        return pd.DataFrame(columns=["Nome", "Quantidade(unidade)"])

st.title("Controle de Estoque -SAF-v0.0.1")

data_locais = load_data(file=estoque_locais)
data_papeis = load_data(file=estoque_papeis)


st.subheader("Estoque Tecido Locais")
st.dataframe(data_locais)
st.subheader("Estoque Papeis")
st.dataframe(data_papeis)


