import streamlit as st

st.title("Inserir ao Banco de Dados")

st.selectbox("", options=['Produto', 'Fornecedor'])
st.text_input("Produto")
st.text_input("Descrição")
st.text_input("Quantidade")
st.text_input(".")