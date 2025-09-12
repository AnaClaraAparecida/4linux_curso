## Leitura de um arquivo

#1: abertura do arquivo (conexao)
arquivo = open('arquivo.txt', 'r')

#2: efetuar a leitura
conteudo = arquivo.read()

#### !!!OBRIGATORIO
arquivo.close()

#3: apresentar o conteudo
print(conteudo)

