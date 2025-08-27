# Crie uma função chamada saudacao que receba dois parâmetros: nome e hora_do_dia. A função deve imprimir uma mensagem como:
#
# "Bom dia, João!" ou "Boa noite, Maria!" Use print() para exibir a saudação.

from datetime import datetime

def saudaçao(nome, hora_atual, hora_24h):
    if hora_atual <= 11.59:
        print(f'Agora sao {hora_24h}, entao tenha um Bom dia {nome}')
    elif hora_atual <= 18.59:
        print(f'Agora sao {hora_24h}, entao tenha uma Boa tarde {nome} ')
    else:
        print(f'Agora sao {hora_24h}, entao tenha uma Boa noite {nome}')

nome = str(input('Qual o seu nome? '))

agr = datetime.now()
hora_atual = agr.hour + agr.minute / 60 # faz com q o horario fique em decimal
hora_24h = agr.strftime('%H:%M')  # estilo 24hs, H -> hora M -> minutos

saudaçao(nome, hora_atual, hora_24h)


