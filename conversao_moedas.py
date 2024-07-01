import json
import requests

api_dolar = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
dolar = api_dolar.json()


valor_d = float((dolar ['USDBRL']['bid']))
print(f'O valor atual do dolar é R${round(valor_d,2)}')


api_euro = requests.get('https://economia.awesomeapi.com.br/last/EUR-BRL')
euro = api_euro.json()

valor_e = float((euro ['EURBRL'] ['bid']))
print(f'O valor atual do euro é R${round(valor_e,2)}')

api_bitcoin = requests.get('https://economia.awesomeapi.com.br/last/BTC-BRL')
bitcoin = api_bitcoin.json()

valor_b = float((bitcoin ['BTCBRL'] ['bid']))
print(f'O valor atual do bitcoin é R${round(valor_b,2)}')

real = float(input('Informe o valor em reais desejado para conversão: '))
conversao = (input('Para dolar, euro ou bitcoin: '))

if conversao == 'dolar' :
  valor = real / valor_d
  print(f'Valor totar é {round(valor, 2)}$')
elif conversao == 'euro':
  valor = real / valor_e
  print(f'Valor totar é {round(valor, 2)}€')
elif conversao == 'bitcoin':
  valor = real / valor_b
  print(f'Valor totar é {round(valor,10)}₿')
else :
  print('Valores inválidos')

