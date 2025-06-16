from src.control.classe_conexao import Conexao

class Compra:
    def __init__(self, id_placa:str, id_cliente:int, data:str, valor_total:float, forma_pagamento:str):
        self.id_placa = id_placa
        self.id_cliente = id_cliente
        self.data = data
        self.valor_total = valor_total
        self.forma_pagamento = forma_pagamento


    def set_info(self, id_placa:str, id_cliente:int, data:str, valor_total:float, forma_pagamento:str):
        self.id_placa = id_placa
        self.id_cliente = id_cliente
        self.data = data
        self.valor_total = valor_total
        self.forma_pagamento = forma_pagamento

    def cadastrar(self, conexao:Conexao):
        sql = f"""
            INSERT INTO compra (id_placa, id_cliente, data, valor_total, forma_pagamento) 
            VALUES ('{self.id_placa}', {self.id_cliente}, '{self.data}', {self.valor_total}, '{self.forma_pagamento}')
        """
        conexao.executar(sql)

    def alterar(self, conexao:Conexao, id_compra:int):
        sql = f"""
            UPDATE compra 
            SET id_placa = '{self.id_placa}', id_cliente = {self.id_cliente}, data = '{self.data}', 
                valor_total = {self.valor_total}, forma_pagamento = '{self.forma_pagamento}'
            WHERE id = {id_compra}
        """
        conexao.executar(sql)

    def buscar_id(self, conexao:Conexao, id_compra:int):
        sql = f"""
            SELECT * FROM compra WHERE id = {id_compra}
        """
        resultado = conexao.retornar(sql)
        return resultado

    def buscar_id_cliente(self, conexao:Conexao, id_cliente:int):
        sql = f"""
            SELECT * FROM compra WHERE id_cliente = {id_cliente}
        """
        resultado = conexao.retornar(sql)
        return resultado

    def buscar_data(self, conexao:Conexao, data:str):
        sql = f"""
            SELECT * FROM compra WHERE data = '{data}'
        """
        resultado = conexao.retornar(sql)
        return resultado

    def listar(self, conexao:Conexao):
        sql = "SELECT * FROM compra"
        resultado = conexao.retornar(sql)
        return resultado

