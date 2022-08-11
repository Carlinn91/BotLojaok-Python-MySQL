import mysql.connector

try:
    #Criação da conexão com o banco
    con = mysql.connector.connect(host='localhost', port='3310', database='lojaok', user='root', password='c4rl0s91')

    # declarar SQL a ser executada
    criar_tabela_SQL = """CREATE TABLE Clientes ( ID INT, NOME VARCHAR(4000), PRIMARY KEY (ID));"""

    #Criação cursor e execução do SQL no banco
    cursor = con.cursor()
    cursor.execute(criar_tabela_SQL)
    print("Tabela de Clientes criada com sucesso!")

except mysql.connector.Error as erro:
    print("Falha ao criar tabela no SQL: {}".format(erro))
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL finalizada")