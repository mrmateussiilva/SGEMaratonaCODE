import streamlit as st
import sqlite3

st.title("Forncedores", )

con = sqlite3.connect("DB.sqlite")
cursor = con.cursor()
res = cursor.execute("""SELECT * FROM fornecedores""")
res = res.fetchmany()

st.dataframe(res, use_container_width=True)
