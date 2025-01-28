from app import app
from flask import render_template

@app.route('/')
@app.route('/fornecedores')
def index():
    return render_template('fornecedores.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')