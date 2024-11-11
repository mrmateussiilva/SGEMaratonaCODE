import streamlit as st
import pandas as pd

from materiais import PAPEIS
from utils.utils import load_data


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


st.title("Controle de Estoque -SAF-v0.0.3")


with st.sidebar:
    select_tipo_entrada = st.selectbox(
        "Selecione o Tipo de Material",
        options=["","Papel","Tinta","Tecido"]
    )

        #  TINTA
    if select_tipo_entrada == "Tinta":
        cor_tinta = st.selectbox(
            "Selecione a Cor",
            options=NOMES_TINTAS
        )
        tipo_tinta = st.selectbox(
            "Tipo de tint",
            options=TIPOS_TINTAS
        )
        qtd_unidade = st.number_input("Quantide(Unidade)",placeholder="1",min_value=1,step=1)
        qtd_litros = st.number_input("Quantide(Litros)",placeholder="1",min_value=1,step=1)
        submit = st.button("Inserir")


    elif select_tipo_entrada == "Papel":
        tipos_tecidos = st.selectbox(
            "Selecione o Papel",
            options=TIPOS_PAPEIS
        )
        metros = st.number_input("Quantide(Metros no Rolo)",placeholder="100",min_value=250,step=10)
        qtd_unidade = st.number_input("Quantide(Unidade)",placeholder="1",min_value=1,step=1)
        submit = st.button("Inserir")


    elif select_tipo_entrada == "Tecido Locais":
        tipos_tecidos = st.selectbox(
            "Selecione o Tecido Local",
            options=TIPOS_LOCAIS
        )
        qtd_unidade = st.number_input("Quantide(Unidade)",placeholder="1",min_value=1,step=1)
        submit = st.button("Inserir")

    elif select_tipo_entrada == "Tecido":
        st.write("Selecionando Tecido")



def view_previsão():
    st.title("Previsão de gasto de materias")


def view_gastos():
    st.title("Previsão de gasto de materias")


def view_data_estoque():
    st.subheader("Estoque Tecido Locais")
    st.data_editor(data_estoque["tecido_locais"])
    st.subheader("Estoque Papeis")
    st.data_editor(data_estoque["papeis"])    
    st.subheader("Estoque Tintas")
    st.data_editor(data_estoque["tintas"])




pg = st.navigation([
    st.Page(view_data_estoque, title="Estoque", icon=""),
    st.Page(view_previsão, title="Previsão de Gastos", icon=""),
])


pg.run()