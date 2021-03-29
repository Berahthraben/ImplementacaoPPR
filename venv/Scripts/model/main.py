from flask import Flask, render_template, request
from json import JSONEncoder
from flask_sqlalchemy import SQLAlchemy

from Usuario import BancoUsuario
from Livro import BancoLivro

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@127.0.0.1:3306/emprestimo_livros"
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template("index.html")

@app.route("/addUsuario", methods=["POST"])
def addUsuario():
    return BancoUsuario.addUsuario(request=request)  
    
@app.route("/addLivro", methods=["POST"])
def addLivro():
    return BancoLivro.addLivro(request=request)

@app.route("/getLivros", methods=["GET"])
def getLivros():
    return BancoLivro.getLivros()

if __name__ == '__main__':
    app.run(debug=True)
