import mysql.connector

try:
    #Criação da conexão com o banco
    con = mysql.connector.connect(host='localhost', port='3310', database='lojaok', user='root', password='c4rl0s91')

    # declarar SQL a ser executada
    criar_tabela_SQL = """CREATE TABLE Venda_Itens ( ID INT, VENDA_ID INT, PRODUTO_ID INT, VALOR VARCHAR(4000), QUANTIDADE VARCHAR(4000), PRIMARY KEY (ID), 
    CONSTRAINT FK_venda FOREIGN KEY (VENDA_ID) REFERENCES Venda(ID), CONSTRAINT FK_produto FOREIGN KEY (PRODUTO_ID) REFERENCES Produtos(ID))"""

    #Criação cursor e execução do SQL no banco
    cursor = con.cursor()
    cursor.execute(criar_tabela_SQL)
    print("Tabela de venda de itens criada com sucesso!")

except mysql.connector.Error as erro:
    print("Falha ao criar tabela no SQL: {}".format(erro))
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL finalizada")
