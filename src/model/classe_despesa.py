from src.control.classe_conexao import Conexao


class Despesa:
    def __init__(self, id_placa:str, id_despesa:int, descricao:str, valor:float, id_prestador:int, data_servico:str):
        self.id_placa = id_placa
        self.id_despesa = id_despesa
        self.descricao = descricao
        self.valor = valor
        self.id_prestador = id_prestador
        self.data_servico = data_servico

    def set_info(self, id_placa:str, id_despesa:int, descricao:str, valor:float, id_prestador:int, data_servico:str):
        self.id_placa = id_placa
        self.id_despesa = id_despesa
        self.descricao = descricao
        self.valor = valor
        self.id_prestador = id_prestador
        self.data_servico = data_servico

    def listar(self, conexao:Conexao):
        sql = "SELECT * FROM despesa"
        resultado = conexao.retornar(sql)
        return resultado

    def cadastrar(self, conexao:Conexao):
        sql = f"""
            INSERT INTO despesa (idplaca, iddespesa, descricao, valor, idprestador, data_servico)
            VALUES ('{self.id_placa}', {self.id_despesa}, '{self.descricao}', {self.valor}, {self.id_prestador}, '{self.data_servico}');
        """
        conexao.executar(sql)

    def alterar(self, conexao:Conexao, id_despesa:int):
        sql = f"""
            UPDATE despesa 
            SET idplaca = '{self.id_placa}', descricao = '{self.descricao}', valor = {self.valor}, idprestador = {self.id_prestador}, data_servico = '{self.data_servico}'
            WHERE iddespesa = {id_despesa};
        """
        conexao.executar(sql)

    def buscar_id(self, conexao:Conexao, id_despesa:int):
        sql = f"""
            SELECT * FROM despesa WHERE iddespesa = {id_despesa};
        """
        resultado = conexao.retornar(sql)
        return resultado

    def buscar_placa(self, conexao:Conexao, id_placa:str):
        sql = f"""
            SELECT * FROM despesa WHERE idplaca = '{id_placa}';
        """
        resultado = conexao.retornar(sql)
        return resultado

