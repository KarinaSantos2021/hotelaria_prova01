from data.conexao import getConexao


class Funcionario:
    def _init_(self, nome, endereco, cargo, cpf):
        self.nome = nome
        self.endereco = endereco
        self.cargo = cargo
        self.cpf = cpf

    def inserir_funcionario():
        print('----- Cadastro de Funcinário -----')
        Funcionario.nome = input('Digite seu nome: ')
        Funcionario.endereco = input('Digite seu endereço: ')
        Funcionario.cargo = input('Digite seu cargo: ')
        Funcionario.cpf = input('Digite seu Cpf: ')
        con = getConexao()
        cursor = con.cursor()
        sql = "INSERT INTO funcionario (nome, endereco, cargo, cpf) values (%s, %s, %s, %s)"
        cursor.execute(sql, (Funcionario.nome, Funcionario.endereco,
                       Funcionario.cargo,  Funcionario.cpf))
        con.commit()
        con.close()
        print('Funcinário Cadastrado!')
