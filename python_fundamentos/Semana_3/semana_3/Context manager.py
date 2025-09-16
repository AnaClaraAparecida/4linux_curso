
# arquivo = open('novo_arquivo.txt', 'x')
# arquivo.write('Nova linha\n')
# arquivo.close()

## context manager -> evitando assim, esquecer de fechar o arquivo

with open('arquivo.txt') as arquivo:
    conteudo = arquivo.read()

conteudo += 'qualquer coisa \n'

with open('arquivo.txt', 'a') as arquivo:
    arquivo.write(conteudo)

print(conteudo)