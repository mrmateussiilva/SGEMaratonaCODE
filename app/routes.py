from app import app
from flask import render_template, redirect ,url_for, request

from app.funcoes import Fornecedores, FornecedoresDB

@app.route('/')
@app.route('/fornecedores')
def index():
    fornecedores_db = FornecedoresDB().ler()
    return render_template('fornecedores.html', fornecedores=fornecedores_db)

@app.route('/excluir_fornecedor/<int:id>')
def excluir_fornecedor(id):
    FornecedoresDB().excluir_fornecedor(id=id)
    return redirect(url_for('index'))

@app.route('/adicionar_fornecedores')
def adicionar_fornecedores():
    print('OK2')
    return render_template('adicionar_fornecedores.html')
    
@app.route('/editar_fornecedor')
def editar_fornecedor():
    return render_template('editar_fornecedor.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

