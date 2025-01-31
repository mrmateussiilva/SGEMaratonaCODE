from app import app
from flask import render_template, redirect ,url_for

from app.funcoes import Fornecedores

@app.route('/')
@app.route('/fornecedores')
def index():
    fornecedores_db = Fornecedores().ler()
    return render_template('fornecedores.html', fornecedores=fornecedores_db)

@app.route('/excluir_fornecedor/<int:id>')
def excluir_fornecedor(id):
    fornecedores_db = Fornecedores().ler()

    fornecedores_db = [f for f in fornecedores_db if f['id'] != id]

    for index, fornecedor in enumerate(fornecedores_db, start=0):
        fornecedor['id'] = index

    Fornecedores().salvar(fornecedores_db)

    return redirect(url_for('index'))

@app.route('/adicionar_fornecedores')
def adicionar_fornecedores():   
    return render_template('adicionar_fornecedores.html')
    
@app.route('/editar_fornecedor')
def editar_fornecedor():
    return render_template('editar_fornecedor.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

