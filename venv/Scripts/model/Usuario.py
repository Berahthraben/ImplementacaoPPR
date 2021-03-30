from json import JSONEncoder
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request

from model import Usuario, UsuarioSchema, Endereco

from Endereco import BancoEndereco

app = Flask(__name__)
db = SQLAlchemy(app)

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

class BancoUsuario:
    def addUsuario(request):
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
        db.session.close()

        return jsonify({"status": "successful"})
