import flask
from src.control.classe_conexao import Conexao

"""
CONEXÃO COM O BANCO DE DADOS
"""

conexao = Conexao("concessionaria", "root", "ifsp", "localhost", 3306)
conexao.abrirConexao()

"""
FIM CONEXÃO COM O BANCO DE DADOS
"""


app = flask.Flask(__name__)





if __name__ == 'main':
    app.run(debug=True)