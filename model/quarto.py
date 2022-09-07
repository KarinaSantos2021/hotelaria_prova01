from data.conexao import getConexao


class Quartos:
    def _init_(self, simples, duplo, casal, luxo):
        self.descricao = simples
        self.reservado = duplo
        self.valor = casal
    pass


    def inserir_quarto():
        print('----- Cadastro de Quarto -----')
        Quartos.descricao = input('Digite a descrição do quarto: ')
        Quartos.valor = input('Digite o valor da diária: ')
        con = getConexao()
        cursor = con.cursor()
        sql = "INSERT INTO quartos (descricao, valor, reservado) values (%s, %s, false)"
        cursor.execute(sql, (Quartos.descricao, Quartos.valor))
        con.commit()
        con.close()
        print('Quarto Cadastrado!')
