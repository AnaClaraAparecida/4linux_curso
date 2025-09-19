# Escreva um programa em python que conte as vogais que a música ‘Faroeste Caboclo’
# tem em sua letra. Armazena a letra da música em um arquivo do tipo txt.

arq_musica = 'musica.txt'

def cont_vogais(txt):
    cont = {v: 0 for v in 'aeiouáéíóúAEIOU'}
    for caracter in txt:
         if caracter in cont:
             cont[caracter] += 1
    return cont

try:
    with open(arq_musica, 'r', encoding='utf-8') as arquivo: #encoding='utf-8' -> caracters especiais seja lidos
        letra = arquivo.read()
        resul = cont_vogais(letra)
        total = sum(resul.values()) #-> o sum é um operandor de soma, assim ele soma os valores da letra

        print('Contagem de vogais: ')
        for vogal, cont in resul.items():
            print(f'{vogal}: {cont}')
        print(f'total de vogais: {total}')

except FileNotFoundError:
    print('Arquivo nao encontrado :/')



