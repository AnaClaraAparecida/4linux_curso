# Escreva uma função que receba um nome e que tenha como saída uma saudação.O
# argumento da função deverá ser o nome, e saída deverá ser como a seguir:
# chamada da função: saudacao('Lalo')
# saída: 'Olá Lalo! Tudo bem com você?'

def saudaçao(nome):
    resp = f'Olá {nome}! Tudo bem com você?'
    return resp

nome = str(input('Qual o seu nome? '))
print(saudaçao(nome))