# # Objetivo: Criar uma função que retorna um valor. Enunciado: Crie uma função chamada soma_dois_numeros(n1, n2)
# que receba dois números e retorne a soma deles. Depois, armazene o resultado em uma variável e imprima:
# "O resultado da soma é: [resultado]"

def soma_tres(n1, n2, n3):
    resp = n1 + n2 + n3
    return resp

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Informe mais um valor: '))

resp = soma_tres(n1, n2, n3)
print(f'O resultado da soma é: {resp}')