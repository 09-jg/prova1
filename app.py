from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def home():
    return render_template('bem_vindo.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        idade = request.form['idade']
        endereco = request.form['endereco']
        numero = request.form['numero']
        
        # Validação da data
        try:
            datetime.strptime(data_nascimento, '%Y-%m-%d')
        except ValueError:
            flash("A data de Nascimento deve estar no formato YYYY-MM-DD")
            return redirect(url_for('cadastro'))
        
        # Aqui você pode adicionar a lógica para salvar os dados no banco de dados
        flash("Cadastro realizado com sucesso!")
        return redirect(url_for('sucesso'))

    return render_template('homepage.html')

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

if __name__ == "__main__":
    app.run(debug=True)

        