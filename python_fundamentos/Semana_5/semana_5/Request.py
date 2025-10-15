import requests

url = 'https://viacep.com.br/ws/{cep}/json/'

teste = '04101300'

resposta = requests.get(url.format(cep=teste))