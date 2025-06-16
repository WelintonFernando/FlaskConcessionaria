from src.control.classe_conexao import Conexao

class Venda:
    def __init__(self, data:str, valor_vendido_float, id_cliente:int, id_placa:int):
        self.data = data
        self.valor_vendido_float = valor_vendido_float
        self.id_cliente = id_cliente
        self.id_placa = id_placa

    def listar(self, conexao:Conexao):
        sql = "SELECT * FROM venda"
        resultado = conexao.retornar(sql)
        return resultado


    def set_info(self, data:str, valor_vendido_float, id_cliente:int, id_placa:int):
        self.data = data
        self.valor_vendido_float = valor_vendido_float
        self.id_cliente = id_cliente
        self.id_placa = id_placa

    def cadastrar(self, conexao:Conexao):
        sql = f"""
            INSERT INTO venda (data, valor_vendido_float, id_cliente, id_placa)
            VALUES ('{self.data}', {self.valor_vendido_float}, {self.id_cliente}, {self.id_placa});
        """
        conexao.executar(sql)

    def alterar(self, conexao:Conexao, id_venda:int):
        sql = f"""
            UPDATE venda 
            SET data = '{self.data}', valor_vendido_float = {self.valor_vendido_float}, id_cliente = {self.id_cliente}, id_placa = {self.id_placa}
            WHERE id = {id_venda};
        """
        conexao.executar(sql)

    def buscar_id(self, conexao:Conexao, id_venda:int):
        sql = f"""
            SELECT * FROM venda WHERE id = {id_venda};
        """
        resultado = conexao.retornar(sql)
        return resultado

    def buscar_cliente(self, conexao:Conexao, id_cliente:int):
        sql = f"""
            SELECT * FROM venda WHERE id_cliente = {id_cliente};
        """
        resultado = conexao.retornar(sql)
        return resultado

    def buscar_data(self, conexao:Conexao, data:str):
        sql = f"""
            SELECT * FROM venda WHERE data = '{data}';
        """
        resultado = conexao.retornar(sql)
        return resultado

