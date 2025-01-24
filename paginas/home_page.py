import streamlit as st


tecidos, papeis, tintas, locais = st.tabs(
    ["Tecidos", "Papeis", "Tintas", "Locais"])
with tecidos:
    st.title("Tecidos em Estoque")
