from conexao import criar_conexao, fechar_conexao

def insere_consumo(con, id_consumo, valores, quantidades):
    cursor = con.cursor()
    sql= "INSERT INTO consumo (id_consumo, valores, quantidades) values (%s, %s, %s)"
    valores = (id_consumo, valores, quantidades)
    cursor.execute(sql, valores)
    cursor.close()
    con.comit()

def main():
    con = criar_conexao("localhost", "root", "", "hotelaria")


    fechar_conexao(con)

if __name__ == '__main__':

   main()
   print('con')

