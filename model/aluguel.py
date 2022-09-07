from data.conexao import getConexao


class Aluguel:
    def _init_(self, id_cliente, diarias, id_quarto):
        self.id_cliente = id_cliente
        self.diarias = diarias
        self.id_quarto = id_quarto

    def realizar_aluguel():
        print('----- Realizar Aluguel -----')
        Aluguel.diarias = input('Digite as Diárias: ')
        Aluguel.lista_cliente()
        Aluguel.id_cliente = input('Digite o index do Cliente: ')
        Aluguel.lista_quartos()
        Aluguel.id_quarto = input('Digite o index do Quarto: ')
    
        con = getConexao()
        cursor = con.cursor()
        upadete_quarto = "UPDATE quartos set reservado = true where id = %s"
        cursor.execute(upadete_quarto, (Aluguel.id_quarto,))
        sql = "INSERT INTO aluguel (id_cliente, diarias, id_quarto) values (%s, %s, %s)"
        cursor.execute(sql, (Aluguel.id_cliente, Aluguel.diarias,
                       Aluguel.id_quarto))
        con.commit()
        con.close()
        print('Aluguel Realizado!')

    def lista_quartos():
        print("---- Quartos ----")
        con = getConexao()
        cursor = con.cursor()
        cursor.execute("SELECT id, descricao FROM quartos where reservado = false")
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
