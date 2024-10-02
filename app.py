from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app= Flask(__name__)
app.secret_key= 'your_secret_key_here'

@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
    if request.method == 'POST':
        nome= request.form['nome']
        data_nascimento= request.form['data_nascimento']
        idade= request.form['idade']
        endereço= request.form['endereço']
        numero= request.form['numero']
    return render_template('cadastro.html')
    
if __name__=='__main__':
    app.run(debug='true')   