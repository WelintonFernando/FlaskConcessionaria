from src.control.classe_conexao import Conexao

class Veiculo:
    def __init__(self, id_placa:str, ano:int, modelo:int, preco_fipe:float, fabricante:str,
                 modelo_veiculo:str,  cor:str, preco_venda:float, total_despesa:str):
        self.id_placa = id_placa
        self.ano = ano
        self.modelo = modelo
        self.preco_fipe = preco_fipe
        self.fabricante = fabricante
        self.modelo_veiculo = modelo_veiculo
        self.cor = cor
        self.preco_venda = preco_venda
        self.total_despesa = total_despesa

    def listar(self, conexao:Conexao):
        sql = "SELECT * FROM veiculo"
        resultado = conexao.retornar(sql)
        return resultado

    def set_info(self, id_placa:str, ano:int, modelo:int, preco_fipe:float, fabricante:str,
                 modelo_veiculo:str, cor:str, preco_venda:float, total_despesa:str):
        self.id_placa = id_placa
        self.ano = ano
        self.modelo = modelo
        self.preco_fipe = preco_fipe
        self.fabricante = fabricante
        self.modelo_veiculo = modelo_veiculo
        self.cor = cor
        self.preco_venda = preco_venda
        self.total_despesa = total_despesa

    def cadastrar(self, conexao:Conexao):
        sql = f"""
            INSERT INTO veiculo (id_placa, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda, total_despesa) 
            VALUES ('{self.id_placa}', {self.ano}, {self.modelo}, {self.preco_fipe}, '{self.fabricante}', 
                    '{self.modelo_veiculo}', '{self.cor}', {self.preco_venda}, '{self.total_despesa}')
        """
        conexao.executar(sql)

    def alterar(self, conexao:Conexao, id_placa:str):
        sql = f"""
            UPDATE veiculo 
            SET ano = {self.ano}, modelo = {self.modelo}, preco_fipe = {self.preco_fipe}, 
                fabricante = '{self.fabricante}', modelo_veiculo = '{self.modelo_veiculo}', 
                cor = '{self.cor}', preco_venda = {self.preco_venda}, total_despesa = '{self.total_despesa}'
            WHERE id_placa = '{id_placa}'
        """
        conexao.executar(sql)

    def buscar_id(self, conexao:Conexao, id_placa:str):
        sql = f"""
            SELECT * FROM veiculo WHERE id_placa = '{id_placa}'
        """
        resultado = conexao.retornar(sql)
        return resultado

    def buscar_ano(self, conexao:Conexao, ano:int):
        sql = f"""
            SELECT * FROM veiculo WHERE ano = {ano}
        """
        resultado = conexao.retornar(sql)
        return resultado

    def buscar_modelo(self, conexao:Conexao, modelo:int):
        sql = f"""
            SELECT * FROM veiculo WHERE modelo = {modelo}
        """
        resultado = conexao.retornar(sql)
        return resultado

    def buscar_fabricante(self, conexao:Conexao, fabricante:str):
        sql = f"""
            SELECT * FROM veiculo WHERE fabricante = '{fabricante}'
        """
        resultado = conexao.retornar(sql)
        return resultado

