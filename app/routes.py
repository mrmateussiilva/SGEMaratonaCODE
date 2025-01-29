from app import app
from flask import render_template
from app.funcoes import Fornecedores

@app.route('/')
@app.route('/fornecedores')
def index():
    fornecedores_db= Fornecedores()
    return render_template('fornecedores.html', fornecedores=fornecedores_db)

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')