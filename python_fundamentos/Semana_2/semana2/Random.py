import random
from time import sleep

lista = [
    ('123', 'Ana'),
    ('456', 'Annie'),
    ('789', 'Vera'),
    ('101', 'Art'),
    ('112', 'Iasmin'),
    ('123', 'Jack')
]

# sorteio simples
# primeiro_sorteado = lista[random.randint(0, len(lista)-1)]

num_cadeiras = len(lista) -1

while len(lista) > 1:
    print('musica tocando...')
    sleep(1)
    print('musica parou!')
    sleep(1)
    print('jogadores se movimentam')
    sleep(2)
    # sortear alguem para sair do jogo
    random.shuffle(lista)
    print(f'O jogador {lista.pop()[1]} saiu do jogo!')

    # segunda forma:
    #num_participantes = len(lista)-1
    # indicie_saida = random.randint(0, num_participantes)
    # del lista[indicie_saida]

print(f'O jogador {lista[0][1]} venceu a partida')