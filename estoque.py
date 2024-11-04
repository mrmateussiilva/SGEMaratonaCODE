import streamlit as st
import pandas as pd
import os
from materiais import PAPEIS


estoque_locais = "estoque_locais.csv"
estoque_papeis = "estoque_papeis.csv"


def load_data(file):
    if os.path.exists(file):
        return pd.read_csv(file)
    else:
        return pd.DataFrame(columns=["Nome", "Quantidade(unidade)"])

st.title("Controle de Estoque -SAF-v0.0.1")
with st.sidebar:
    select_tipo_entrada = st.selectbox(
        "Selecione o Tipo de Material",
        options=["","Papel","Tinta","Tecido"]
    )

    if select_tipo_entrada == "Tinta":
        st.write("Selecionando tinta")
    elif select_tipo_entrada == "Papel":
        tipos_tecidos = st.selectbox(
            "Selecione o Papel",
            options=PAPEIS
        )
        metros = st.number_input("Quantide(Metros no Rolo)",placeholder="100",min_value=10,step=10)
        qtd_unidade = st.number_input("Quantide(Unidade)",placeholder="1",min_value=1,step=1)
        
    elif select_tipo_entrada == "Tecido":
        st.write("Selecionando Tecido")

data_locais = load_data(file=estoque_locais)
data_papeis = load_data(file=estoque_papeis)


st.subheader("Estoque Tecido Locais")
st.dataframe(data_locais)
st.subheader("Estoque Papeis")
st.dataframe(data_papeis)


