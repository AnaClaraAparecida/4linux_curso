
def leitura(objeto_arquivo, ):
    while True:
        registro = objeto_arquivo.readline()
        if not registro:
            break
        yield registro 

lista = []

with open('/home/ana-clara/Área de trabalho/sacramento.csv') as arquivo:
    for linha in leitura(arquivo):
        lista.append(linha.split(','))

        #... tratamento serializar
        #... armazenar em banco 