## Modo de escrita (write)

## abre o arquivo antes, e capture o conteudo do arquivo em uma variavel
#arquivo = open('arquivo.txt')

#conteudo = arquivo.readlines()

#arquivo.close()

#conteudo.append('\nnova linha de exemplo')

## altera esse conteudo
#1: abertura do arquivo (conexao)
#arquivo = open('arquivo.txt', 'w')

#arquivo.writelines(['Outro exemplo\n'])

#arquivo.close()


##  Modo de leitura a (append)

#arquivo = open('arquivo.txt', 'a')

#arquivo.write('\nadd nova linha\n')

#arquivo.close()


## Modo de leitura com o 'x' -> criar um novo arquivo, e possibilita escrever nele tbm

arquivo = open('novo_arquivo.txt', 'x')

arquivo.write('Nova linha\n')

arquivo.close()

# ANOTAÇAOOO
# • r: abre aquivo para leitura (modo padrão - caso o arquivo não existir, ele o cria)
# • w: abre o aquivo para escrita, sobrescrevendo o arquivo (truncate)
# • x: cria um novo arquivo e o abre para escrita (caso arquivo existir, o Python retornará
# erro (arquivo já existente))
# • a: abre um arquivo para escrita, e posiciona o cursor no ﬁnal de arquivo o
# • +: abre um arquivo para atualização (leitura e escrita)

# readlines: ele irá converter cada linha do arquivo em string, e separadamente,
# irá adicionar tais strings em uma lista