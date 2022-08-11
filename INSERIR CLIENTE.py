import mysql.connector
from mysql.connector import Error

#Inserir registros no banco 

try:
    con = mysql.connector.connect(host='localhost', port='3310', database='lojaok', user='root', password='c4rl0s91')

    
    inserir_clientes = """INSERT INTO Clientes (ID, NOME) VALUES (21856,'Jar Jar Binks'), (39550,'R2D2'), (44993,'C-3PO'), (49400,'Jabba the Hutt')"""

    
    cursor = con.cursor()
    cursor.execute(inserir_clientes)
    con.commit()
    print(cursor.rowcount, "Registros adicionados a tabela!")

except Error as erro:
    print("Falha ao inserir dados no SQL: {}".format(erro))
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL finalizada")
