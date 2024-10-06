from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escola.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

class Sala(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(10), nullable=False)

class Aula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    sala_id = db.Column(db.Integer, db.ForeignKey('sala.id'), nullable=False)
    data = db.Column(db.String(20), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

# Alunos
@app.route('/alunos', methods=['GET', 'POST'])
def gerenciar_alunos():
    if request.method == 'POST':
        nome = request.form['nome']
        novo_aluno = Aluno(nome=nome)
        db.session.add(novo_aluno)
        db.session.commit()
        return redirect(url_for('gerenciar_alunos'))

    alunos = Aluno.query.all()
    return render_template('alunos.html', alunos=alunos)

@app.route('/alunos/edit/<int:id>', methods=['GET', 'POST'])
def editar_aluno(id):
    aluno = Aluno.query.get(id)
    if request.method == 'POST':
        aluno.nome = request.form['nome']
        db.session.commit()
        return redirect(url_for('gerenciar_alunos'))
    return render_template('editar_aluno.html', aluno=aluno)

@app.route('/alunos/delete/<int:id>')
def deletar_aluno(id):
    aluno = Aluno.query.get(id)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('gerenciar_alunos'))

# Salas
@app.route('/salas', methods=['GET', 'POST'])
def gerenciar_salas():
    if request.method == 'POST':
        numero = request.form['numero']
        nova_sala = Sala(numero=numero)
        db.session.add(nova_sala)
        db.session.commit()
        return redirect(url_for('gerenciar_salas'))

    salas = Sala.query.all()
    return render_template('salas.html', salas=salas)

@app.route('/salas/edit/<int:id>', methods=['GET', 'POST'])
def editar_sala(id):
    sala = Sala.query.get(id)
    if request.method == 'POST':
        sala.numero = request.form['numero']
        db.session.commit()
        return redirect(url_for('gerenciar_salas'))
    return render_template('editar_sala.html', sala=sala)

@app.route('/salas/delete/<int:id>')
def deletar_sala(id):
    sala = Sala.query.get(id)
    db.session.delete(sala)
    db.session.commit()
    return redirect(url_for('gerenciar_salas'))

# Aulas
@app.route('/aulas', methods=['GET', 'POST'])
def gerenciar_aulas():
    if request.method == 'POST':
        aluno_id = request.form['aluno_id']
        sala_id = request.form['sala_id']
        data = request.form['data']
        nova_aula = Aula(aluno_id=aluno_id, sala_id=sala_id, data=data)
        db.session.add(nova_aula)
        db.session.commit()
        return redirect(url_for('gerenciar_aulas'))

    alunos = Aluno.query.all()
    salas = Sala.query.all()
    aulas = Aula.query.all()
    return render_template('aulas.html', aulas=aulas, alunos=alunos, salas=salas)

@app.route('/aulas/edit/<int:id>', methods=['GET', 'POST'])
def editar_aula(id):
    aula = Aula.query.get(id)
    if request.method == 'POST':
        aula.aluno_id = request.form['aluno_id']
        aula.sala_id = request.form['sala_id']
        aula.data = request.form['data']
        db.session.commit()
        return redirect(url_for('gerenciar_aulas'))
    
    alunos = Aluno.query.all()
    salas = Sala.query.all()
    return render_template('editar_aula.html', aula=aula, alunos=alunos, salas=salas)

@app.route('/aulas/delete/<int:id>')
def deletar_aula(id):
    aula = Aula.query.get(id)
    db.session.delete(aula)
    db.session.commit()
    return redirect(url_for('gerenciar_aulas'))

if __name__ == '__main__':
    app.run(debug=True)