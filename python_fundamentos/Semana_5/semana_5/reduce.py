from functools import reduce
from random import randint

# 1: realizar a leitura do arquivo 
with open('/home/ana-clara/Área de trabalho/sacramento.csv') as arquivo:
    conteudo = arquivo.readlines()

# 2: coletar infos de cabeçalho
cabec = conteudo[0].split(',')

# 3: coletar infos de registro 
dados = [conteudo[indice].split(',') for indice in range(1, len(conteudo))]

# 4: gerar uma amostra aleatoria de 100 registros de venda
amostra = [dados[randint(0, len(dados)-1)] for x in range(100)]

# 5: filtrar os imoveis com preços acima de $100.000
imoveis_100k = [registro for registro in dados if float(registro[9]) > 100000]


# ex de uso do map 
def adiciona_faixa_preco(registro_venda):
    novo_registro = registro_venda
    preco = float(novo_registro[9])

    if preco < 50000: 
        novo_registro.append('ate 50k')
    elif preco < 100000:
        novo_registro.append('50k - 100k')
    elif preco < 150000:
        novo_registro.append('100k - 150k')
    elif preco < 200000:
        novo_registro.append('150k - 200k')
    else:
        novo_registro.append('mais que 200k')

    return novo_registro

def conta_faixas(dados):
    return {
        '< 50k' : reduce(lambda x,y: x+y, 
                         list(map(
                             lambda registro: 1 if registro[-1] == ' < 50k' else 0,
                           dados))),
        '50k - 100k' : reduce(lambda x,y: x+y,
                          list(map(
                              lambda registro: 1 if registro[-1] == '50k - 100k' else 0,
                            dados))),
        '100k - 150k' : reduce(lambda x,y: x+y,
                          list(map(
                              lambda registro: 1 if registro[-1] == '100k - 150k' else 0,
                            dados))),  
        '150k - 200k' : reduce(lambda x,y: x+y,
                          list(map(
                              lambda registro: 1 if registro[-1] == '150k - 200k' else 0,
                            dados))), 
        '> 200k' : reduce(lambda x,y: x+y,
                          list(map(
                              lambda registro: 1 if registro[-1] == '> 200k' else 0,
                            dados))),                                     
    }