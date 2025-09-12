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