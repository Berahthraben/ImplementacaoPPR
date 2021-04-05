from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, enum
from json import JSONEncoder


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@127.0.0.1:3306/emprestimo_livros"
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Usuario(db.Model):
    __tablename__ = "Usuario"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    senha = db.Column(db.String(300), nullable=False)
    idade = db.Column(db.Integer(), nullable=False)
    cpfCnpj = db.Column(db.String(30), nullable=False)
    endereco = db.relationship('Endereco', backref=db.backref('Usuario',   lazy=True))
    livro = db.relationship('UsuarioTemLivro', backref=db.backref('Usuario',   lazy=True))

    def __init__(self, nome, sobrenome, email, senha, idade, cpfCnpj):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
        self.idade = idade
        self.cpfCnpj = cpfCnpj


class Livro(db.Model):
    __tablename__ = "Livro"
    id = db.Column(db.Integer, primary_key=True)
    autor = db.Column(db.String(250), nullable=False)
    titulo = db.Column(db.String(200), nullable=False)
    editora = db.Column(db.String(200), nullable=False)
    preco = db.Column(db.Float(), nullable=False)
    status = db.Column(db.Integer(), nullable=False)
    usuario = db.relationship('UsuarioTemLivro', backref=db.backref('Livro',   lazy=True))

    def __init__(self, autor, titulo, editora, preco, status):
        self.autor = autor
        self.titulo = titulo
        self.editora = editora
        self.preco = preco
        self.status = status


class UsuarioTemLivro(db.Model):
    __tablename__ = "UsuarioTemLivro"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nullable=True)
    livro_id = db.Column(db.Integer, db.ForeignKey('Livro.id'), nullable=True)


class Status(enum.Enum):
    DISPONIVEL = 0
    EMPRESTADO = 1
    VENDIDO = 2
    TROCADO = 3


class Endereco(db.Model):
    __tablename__ = "Endereco"
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(150), nullable=False)
    bairro = db.Column(db.String(150), nullable=False)
    rua = db.Column(db.String(300), nullable=False)
    numero = db.Column(db.String(6), nullable=False)
    complemento = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float(), nullable=False)
    longetude = db.Column(db.Float(), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nullable=True)

    def __init__(self, estado, cidade, bairro, rua, numero, complemento, latitude, longetude):
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.latitude = latitude
        self.longetude = longetude


class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ("id", "nome", "sobrenome", "senha","email", "idade", "cpfCnpj")

class LivrosSchema(ma.Schema):
    class Meta:
        fields = ("id", "autor", "titulo", "editora", "preco", "status")


usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
livro_schema = LivrosSchema()
livros_schema = LivrosSchema(many=True)

@app.route("/addUsuario", methods=["POST"])
def addUsuario():

    novoUsuario = Usuario(
        request.json['nome'],
        request.json['sobrenome'],
        request.json['email'],
        request.json['senha'],
        request.json['idade'],
        request.json['cpfCnpj']
    )

    db.session.add(novoUsuario)
    db.session.commit()
    return jsonify({"status": "successful"})

@app.route("/addLivro", methods=["POST"])
def addLivro():

    
    novoLivro = Livro(
        request.json['autor'],
        request.json['titulo'],
        request.json['editora'],
        request.json['preco'],
        0
    )

    db.session.add(novoLivro)
    db.session.commit()

    return jsonify({"status": "successful"})


@app.route("/getUsuarios", methods=["GET"])
def getUsuarios():
    usuarios = Usuario.query.all()
    result = usuarios_schema.dump(usuarios)

    return jsonify(result)

@app.route("/login", methods=["POST"])
def login():
    email, senha = request.json["email"], request.json["senha"]

    usuario = Usuario.query.filter_by(email=email).first()

    print(usuario is None)

@app.route("/getLivros", methods=["GET"])
def getLivros():
    livros = Livro.query.all()
    result = livros_schema.dump(livros)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)


