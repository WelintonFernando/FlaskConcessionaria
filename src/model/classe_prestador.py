from src.control.classe_conexao import Conexao

class Prestador:
    def __init__(self, nome_empresa:str, cidade:str, uf:str, cep:str):
        self.nome_empresa = nome_empresa
        self.cidade = cidade
        self.uf = uf
        self.cep = cep

    def set_info(self, nome_empresa:str, cidade:str, uf:str, cep:str):
        self.nome_empresa = nome_empresa
        self.cidade = cidade
        self.uf = uf
        self.cep = cep

    def listar(self, conexao:Conexao):
        sql = "SELECT * FROM prestador"
        resultado = conexao.retornar(sql)
        return resultado

    def cadastrar(self, conexao:Conexao):
        sql = f"""
            INSERT INTO prestador (nome_empresa, cidade, uf, cep)
            VALUES ('{self.nome_empresa}', '{self.cidade}', '{self.uf}', '{self.cep}');
        """
        conexao.executar(sql)

    def alterar(self, conexao:Conexao, id_prestador:int):
        sql = f"""
            UPDATE prestador 
            SET nome_empresa = '{self.nome_empresa}', cidade = '{self.cidade}', uf = '{self.uf}', cep = '{self.cep}'
            WHERE id = {id_prestador};
        """
        conexao.executar(sql)

    def buscar_id(self, conexao:Conexao, id_prestador:int):
        sql = f"""
            SELECT * FROM prestador WHERE id = {id_prestador};
        """
        resultado = conexao.retornar(sql)
        return resultado

    def buscar_nome(self, conexao:Conexao, nome_empresa:str):
        sql = f"""
            SELECT * FROM prestador WHERE nome_empresa = '{nome_empresa}';
        """
        resultado = conexao.retornar(sql)
        return resultado


