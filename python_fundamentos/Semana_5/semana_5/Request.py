import requests

cep = '04101300'
url = f'https://viacep.com.br/ws/{cep}/json/'

resposta = requests.get(url)

# Verifica se a resposta foi bem-sucedida
if resposta.status_code == 200:
    dados = resposta.json()
    print(dados)
else:
    print(f'Erro ao buscar o CEP: {resposta.status_code}')
