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

