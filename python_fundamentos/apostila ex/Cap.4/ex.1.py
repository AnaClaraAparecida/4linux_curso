# Escreva um programa em Python que simule uma dança das cadeiras. Você deverá
# importar o pacote random e iniciar uma lista com nomes de pessoas que participariam da
# brincadeira. O jogo deverá iniciar com 9 cadeiras e 10 participantes. A cada rodada,
# uma cadeira deverá ser retirada e um dos jogadores, de forma aleatória, ser eliminado. O
# jogo deverá terminar quando apenas restar uma cadeira e ao ﬁnal de todas as rodadas,
# deverá ser apresentado vencedor.


import random
from time import sleep

jogadores = [
    'Ana', 'Vera',
    'Annie', 'Iasmin',
    'Jack', 'Art',
    'Bya', 'Cris',
    'Marcos', 'Clayton'
]

while len(jogadores) > 1:
    print('jogo iniciado...')
    sleep(2)
    print('a musica parou! ')
    sleep(3)

    eliminado = random.choice(jogadores)
    jogadores.remove(eliminado)

    print(f'jogador(a) {eliminado} eliminado(a)')

print(f'jogador(a) {jogadores[0]} venceu a partida')


