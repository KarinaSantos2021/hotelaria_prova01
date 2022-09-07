from data.conexao import getConexao


class Consumo:
    def _init_(self, descricao, valores, quantidades, id_quarto):
        self.descricao = descricao
        self.valores = valores
        self.quantidades = quantidades
        self.id_quarto = id_quarto

    def realizar_consumo():
        print('----- Realizar Consumo -----')
        Consumo.descricao = input('Digite uma descrição: ')
        Consumo.valores = input('Digite o valor: ')
        Consumo.quantidades = input('Digite a quantidade: ')
        Consumo.lista_quartos()
        Consumo.id_quarto = input('Digite o index do Quarto: ')

        con = getConexao()
        cursor = con.cursor()
        sql = "INSERT INTO consumo (descricao, valores, quantidades,id_quarto) values (%s, %s, %s, %s)"
        cursor.execute(sql, (Consumo.descricao, Consumo.valores,
                       Consumo.quantidades,  Consumo.id_quarto))
        con.commit()
        con.close()
        print('Consumo lançado!')

    def lista_quartos():
        print("---- Quartos ----")
        con = getConexao()
        cursor = con.cursor()
        cursor.execute(
            "SELECT id, descricao FROM quartos where reservado = true")
        list = cursor.fetchall()
        for row in list:
            print(row[0], " -> ", row[1], "\n")
        print("-------------")
