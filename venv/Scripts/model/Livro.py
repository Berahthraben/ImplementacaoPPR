from json import JSONEncoder
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request

from model import *

db = SQLAlchemy(app)

livro_schema = LivrosSchema()
livros_schema = LivrosSchema(many=True)

class BancoLivro:
    def addLivro(request):

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

    def getLivros():
        livros = Livro.query.all()
        result = livros_schema.dump(livros)

        return jsonify(result)
