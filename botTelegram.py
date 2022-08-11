import requests
import time
import json
import os
from somasql import soma_venda_itens, selecionar_ID_cliente, selecionar_total_venda_itens, selecionarProdutos, selecionarQuantidade, valorPedido, vendaCliente, totaldeVendas

soma = soma_venda_itens.x
selecionar_cliente = selecionar_ID_cliente.a
venda_total_itens = selecionar_total_venda_itens.b
selecionar_produtos = selecionarProdutos.c
selecionar_quantidade = selecionarQuantidade.d
valor_pedido = valorPedido.e
venda_cliente = vendaCliente.f


class TelegramBot:
    def __init__(self):
        iTOKEN  = '5454576162:AAEE5B_kUqux8RH5VHD0KVbhoen8nuCJHOA'
        self.iURL = f'https://api.telegram.org/bot{iTOKEN}/'

    def Iniciar(self):
        iUPDATE_ID = None
        while True:
            iATUALIZACAO = self.ler_novas_mensagens(iUPDATE_ID)
            IDADOS = iATUALIZACAO["result"]
            if IDADOS:
                for dado in IDADOS:
                    iUPDATE_ID = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    primeira_mensagem = int(dado["message"]["message_id"]) == 1
                    resposta = self.gerar_respostas(mensagem, primeira_mensagem)
                    self.responder(resposta, chat_id)

    def ler_novas_mensagens(self, iUPDATE_ID):
        iLINK_REQ = f'{self.iURL}getUpdates?timeout=5'
        if iUPDATE_ID:
            iLINK_REQ = f'{iLINK_REQ}&offset={iUPDATE_ID + 1}'
        iRESULT = requests.get(iLINK_REQ)
        return json.loads(iRESULT.content)


    def gerar_respostas(self, mensagem, primeira_mensagem):
        print('mensagem do cliente: ' + str(mensagem))
        if primeira_mensagem == True or mensagem.lower() in ('total', {venda_cliente}):
            return f'''Olá seja bem vindo a Tabela da Loja Ok, informe os dados solicitados:{os.linesep}
            Digite 1 para o valor de todas as vendas{os.linesep}
            Digite o ID do cliente para aferição da última venda do mesmo{os.linesep}'''
        if mensagem == '1':
            return f'''O valor total de vendas foi: R${soma}{os.linesep}'''
        if mensagem == {venda_cliente}:
            return f'''O cliente comprou {venda_cliente} no total de {venda_total_itens} o item {selecionar_produtos} na quantidade {selecionar_quantidade} dando o valor {valor_pedido} {os.linesep} '''
        else:
            return 'Para consultar o valor total de vendas digite 1 ou o valor da última venda digite o ID do cliente'

    def responder(self, resposta, chat_id):
        iLINK_REQ = f'{self.iURL}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(iLINK_REQ)
        print("respondi: " + str(resposta))

bot = TelegramBot()
bot.Iniciar() 