from data.conexao import getConexao


class Cliente:
    def _init_(self, nome, cpf, email, telefone, data_reserva, fim_reserva):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.data_reserva = data_reserva
        self.fim_reserva = fim_reserva

    def inserir_hospede():
        print('----- Cadastro de Cliente -----')
        Cliente.nome = input('Digite seu nome: ')
        Cliente.cpf = input('Digite seu cpf: ')
        Cliente.telefone = input('Digite seu telefone: ')
        Cliente.email = input('Digite seu email: ')
        con = getConexao()
        cursor = con.cursor()
        sql = "INSERT INTO clientes (nome, cpf, telefone, email) values (%s, %s, %s, %s)"
        cursor.execute(sql, (Cliente.nome, Cliente.cpf,
                       Cliente.telefone,  Cliente.email))
        con.commit()
        con.close()
        print('Cliente Cadastrado!')
