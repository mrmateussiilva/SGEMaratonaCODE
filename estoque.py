import streamlit as st
import pandas as pd
from model import save_data,load_data
import json
from materiais import PAPEIS,TECIDOS,TIPOS_TINTAS,TINTAS
from utils.utils import load_data


data_estoque = {
    "tecido_locais":load_data("model_csv/estoque_locais.csv"),
    "papeis":load_data("model_csv/estoque_papeis.csv"),
    "tecidos":load_data("model_csv/estoque_papeis.csv"),
    "tintas":load_data("model_csv/estoque_tintas.csv"),
}



st.title("Controle de Estoque -SAF-v0.0.3")


with st.sidebar:
    select_tipo_entrada = st.selectbox(
        "Selecione o Tipo de Material",
        options=["","Papel","Tinta","Tecidos"]
    )

        #  TINTA
    if select_tipo_entrada == "Tinta":
        cor_tinta = st.selectbox(
            "Selecione a Cor",
            options=TINTAS
        )
        tipo_tinta = st.selectbox(
            "Tipo de tint",
            options=TIPOS_TINTAS
        )
        qtd_unidade = st.number_input("Quantide(Unidade)",placeholder="1",min_value=1,step=1)
        qtd_litros = st.number_input("Quantide(Litros)",placeholder="1",min_value=1,step=1)
        if st.button("Inserir"):
            d = {
                "color":cor_tinta,
                "type":tipo_tinta,
                "qtd_unit":qtd_unidade,
                "qtd_litr":qtd_litros,
            }
            save_data("tintas.json",d.copy())
            d.clear()


    elif select_tipo_entrada == "Papel":
        tipos_papais = st.selectbox(
            "Selecione o Papel",
            options=PAPEIS
        )
        metros = st.number_input("Quantide(Metros no Rolo)",placeholder="100",min_value=250,step=10)
        qtd_unidade = st.number_input("Quantide(Unidade)",placeholder="1",min_value=1,step=1)
        if st.button("Inserir"):
            d = {
                "papel":tipos_papais,
                "qtd_unit":qtd_unidade,
                "qtd_metros_por_rolo":metros,
            }
            save_data("papeis.json",d.copy())
            d.clear()



    # elif select_tipo_entrada == "Tecido Locais":
    #     tipos_tecidos = st.selectbox(
    #         "Selecione o Tecido Local",
    #         options=TIPOS_LOCAIS
    #     )
    #     qtd_unidade = st.number_input("Quantide(Unidade)",placeholder="1",min_value=1,step=1)
    #     submit = st.button("Inserir")

    elif select_tipo_entrada == "Tecidos":
        tipos_tecidos = st.selectbox(
            "Selecione o Tecido",
            options=TECIDOS
        )
        metros = st.number_input("Quantide(Metros no Rolo)",placeholder="1",min_value=1,step=1)
        qtd_unidade = st.number_input("Quantide(Unidade)",placeholder="1",min_value=1,step=1)
        if st.button("Inserir"):
            d = {
                "tecido":tipos_tecidos,
                "qtd_unit":qtd_unidade,
                "qtd_metros_por_rolo":metros,
            }
            save_data("tecidos.json",d.copy())
            d.clear()




def view_previsão():
    st.title("Being implemented...")



def view_data_estoque():
    tecidos,tintas,papeis = st.tabs(["Tecidos","Tintas","Papeis"])
    try:
        with tintas,open("tintas.json",'r') as fp:
            data = json.load(fp)
            # dtf = pd.DataFrame(data)
            st.json(data)
            
        with tecidos,open("tecidos.json",'r') as fp:
            data = json.load(fp)
            # dtf = pd.DataFrame(data)
            st.json(data)
            
        with papeis,open("papeis.json",'r') as fp:
            data = json.load(fp)
            # dtf = pd.DataFrame(data)
            st.json(data)
    except:
        pass
        
   
    # st.subheader("Estoque Tecido Locais")
    # st.data_editor(data_estoque["tecido_locais"])
    # st.subheader("Estoque Papeis").
    # st.data_editor(data_estoque["papeis"])    
    # st.subheader("Estoque Tintas")
    # st.data_editor(data_estoque["tintas"])




pg = st.navigation([
    st.Page(view_data_estoque, title="Estoque", icon=""),
    st.Page(view_previsão, title="Previsão de Gastos", icon=""),
])


pg.run()