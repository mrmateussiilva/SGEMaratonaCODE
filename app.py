import streamlit as st


pg = st.navigation([
    st.Page("paginas/home_page.py", title="Estoque", icon=""),
    st.Page("paginas/data_entry.py", title="Entradas", icon=""),
])
pg.run()