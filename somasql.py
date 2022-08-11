import mysql.connector

 #Criação da conexão com o banco
con = mysql.connector.connect(host='localhost', port='3310', database='lojaok', user='root', password='c4rl0s91')

#Soma
class soma_venda_itens:
    with con.cursor() as c:
        sql = "SELECT SUM(valor) AS total_venda FROM Venda_Itens"
        c.execute(sql)
        res = c.fetchall()
        for x in res:
            print (x)

class selecionar_ID_cliente:
    with con.cursor() as c:
        sql2 = "SELECT ID FROM clientes"
        c.execute(sql2)
        res = c.fetchall()
        for a in res:
            print (a)

class selecionar_total_venda_itens:
    with con.cursor() as c:
        sql3 = "SELECT Valor FROM Venda_Itens"
        c.execute(sql3)
        res = c.fetchall()
        for b in res:
            print (b)

class selecionarProdutos:
    with con.cursor() as c:
        sql4 = "SELECT ID FROM Produtos"
        c.execute(sql4)
        res = c.fetchall()
        for c in res:
            print (c)

class selecionarQuantidade:
    with con.cursor() as c:
        sql5 = "SELECT QUANTIDADE FROM Venda_Itens"
        c.execute(sql5)
        res = c.fetchall()
        for d in res:
            print (d)

class valorPedido:
    with con.cursor() as c:
        sql6 = "SELECT valor FROM Venda_Itens"
        c.execute(sql6)
        res = c.fetchall()
        for e in res:
            print (e)

class vendaCliente:
    with con.cursor() as c:
        sql7 = "SELECT ID FROM Clientes WHERE id = 21856"
        c.execute(sql7)
        res = c.fetchall()
        for f in res:
            print (f)

class totaldeVendas:
    with con.cursor() as c:
        sql2 = "SELECT VALOR, CLIENTE_ID FROM Venda_Itens INNER JOIN Venda ON Venda.CLIENTE_ID = Venda_Itens.VALOR"
        c.execute(sql2)
        res = c.fetchall()
        for g in res:
            print (g)



    




    #sql2 = """SELECT ID FROM Venda"""
    #sql3 = """SELECT Valor FROM Venda_Itens"""
    #sql4 = """SELECT ID FROM Produtos"""
    #sql5 = """SELECT valor FROM Venda_Itens"""
    #sql6 = """SELECT QUANTIDADE FROM Venda_Itens"""
    #sql7 = """"""

    con.close()