from src.control.classe_conexao import Conexao



class Cliente:
    def __init__(self, nome:str, endereco:str, cidade:str, uf:str, cep:str):
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.uf = uf
        self.cep = cep

    def listar(self, conexao: Conexao):
        sql = "SELECT * FROM cliente"
        resultado = conexao.retornar(sql)
        return resultado

    def set_info(self, nome:str, endereco:str, cidade:str, uf:str, cep:str):
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.uf = uf
        self.cep = cep

    def cadastrar(self, conexao: Conexao):
        sql = f"""
        INSERT INTO cliente (nome, endereco, cidade, uf, cep)
        VALUES ('{self.nome}', '{self.endereco}', '{self.cidade}', '{self.uf}', '{self.cep}')
        """
        conexao.executar(sql)

    def alterar(self, conexao: Conexao, id_cliente: int):
        sql = f"""
        UPDATE cliente 
        SET nome = '{self.nome}', endereco = '{self.endereco}', cidade = '{self.cidade}', uf = '{self.uf}', cep = '{self.cep}'
        WHERE id = {id_cliente}
        """
        conexao.executar(sql)


    def buscar_nome(self, conexao: Conexao):
        sql = f"""
        SELECT * FROM cliente WHERE nome = '{self.nome}'
        """
        resultado = conexao.retornar(sql)
        return resultado

    def buscar_id(self, conexao: Conexao, id_cliente: int):
        sql = f"""
        SELECT * FROM cliente WHERE id = {id_cliente}
        """
        resultado = conexao.retornar(sql)
        return resultado


    def __str__(self):
        return f"Cliente(nome={self.nome}, endereco={self.endereco}, cidade={self.cidade}, uf={self.uf}, cep={self.cep})"