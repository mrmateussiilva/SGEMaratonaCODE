import streamlit as st
from materiais import TIPOS_TINTAS,TECIDOS,TINTAS,PAPEIS 




container = st.container()

select_tipo_entrada = container.selectbox(
    "Selecione o Tipo de Material",
    options=["","Papel","Tinta","Tecido"]
)

    #  TINTA
if select_tipo_entrada == "Tinta":
    cor_tinta = container.selectbox(
        "Selecione a Cor",
        options=TINTAS
    )
    tipo_tinta = container.selectbox(
        "Tipo de tint",
        options=TIPOS_TINTAS
    )
    qtd_unidade = container.number_input("Quantide(Unidade)",placeholder="1",min_value=1,step=1)
    qtd_litros = container.number_input("Quantide(Litros)",placeholder="1",min_value=1,step=1)
    submit = container.button("Inserir")


elif select_tipo_entrada == "Papel":
    tipos_tecidos = container.selectbox(
        "Selecione o Papel",
        options=PAPEIS
    )
    metros = container.number_input("Quantide(Metros no Rolo)",placeholder="100",min_value=250,step=10)
    qtd_unidade = container.number_input("Quantide(Unidade)",placeholder="1",min_value=1,step=1)
    submit = container.button("Inserir")


elif select_tipo_entrada == "Tecido":
    container.write("Selecionando Tecido")


# elif select_tipo_entrada == "Tecido Locais":
#     tipos_tecidos = st.selectbox(
#         "Selecione o Tecido Local",
#         options=TIPOS_LOCAIS
#     )
#     qtd_unidade = st.number_input("Quantide(Unidade)",placeholder="1",min_value=1,step=1)
#     submit = st.button("Inserir")

