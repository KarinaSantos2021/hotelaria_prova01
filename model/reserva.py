import this
from data.conexao import getConexao


class Reserva:
    def _init_(self, nome, data_check_in, data_checkout, id_quartos, id_clientes, id_funcionario):
        self.nome = nome
        self.data_check_in = data_check_in
        self.data_checkout = data_checkout
        self.id_quartos = id_quartos
        self.id_clientes = id_clientes
        self.id_clientes = id_funcionario

    def fazer_reserva():
        print('----- Realizar Reserva -----')
        Reserva.nome = input('Digite a descrição: ')
        Reserva.data_check_in = input(
            'Digite Data do Check-in (Ex.: 10-10-2022): ')
        Reserva.data_checkout = input(
            'Previsão de Check-out (Ex.: 10-10-2022): ')
        Reserva.lista_quartos()
        Reserva.id_quartos = input('Digite o index do quarto: ')
        Reserva.lista_cliente()
        Reserva.id_clientes = input('Digite o index do Cliente: ')
        Reserva.lista_funcionario()
        Reserva.id_funcionario = input('Digite o index do Funcionário: ')
        con = getConexao()
        cursor = con.cursor()
        sql = "INSERT INTO reserva (nome, data_check_in, data_checkout, id_quartos, id_clientes, id_funcionario) values (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (Reserva.nome, Reserva.data_check_in,
                       Reserva.data_checkout,  Reserva.id_quartos, Reserva.id_clientes,Reserva.id_funcionario))
        con.commit()
        con.close()
        print('Reserva Realizada com sucesso!')

    def lista_quartos():
        print("---- Quartos ----")
        con = getConexao()
        cursor = con.cursor()
        cursor.execute("SELECT id, descricao FROM quartos")
        list = cursor.fetchall()
        for row in list:
            print(row[0], " -> ", row[1], "\n")
        print("-------------")

    def lista_cliente():
        print("---- Clientes ----")
        con = getConexao()
        cursor = con.cursor()
        cursor.execute("SELECT id_clientes, nome FROM clientes")
        list = cursor.fetchall()
        for row in list:
            print(row[0], " -> ", row[1], "\n")
        print("-------------")

    def lista_funcionario():
        print("---- Funcionários ----")
        con = getConexao()
        cursor = con.cursor()
        cursor.execute("SELECT id_funcionario, nome FROM funcionario")
        list = cursor.fetchall()
        for row in list:
            print(row[0], " -> ", row[1], "\n")
        print("-------------")
