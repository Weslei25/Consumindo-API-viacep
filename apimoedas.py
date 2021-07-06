import requests
import json

# O endereço da Api para ser consumida
try:
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
# Transformando em json
    cotacoes = cotacoes.json()
# Passando parametros a ser acessados nessa caso o dolar
    cotacao_dolar = cotacoes['USDBRL']['bid']

    print('A cotação do dolar é:', cotacao_dolar)
# Excessão caso ocorra algun erro na consulta 
except Exception as erro:
    print('Ocorreu um erro na consulta da cotação, {}'.format(erro))
