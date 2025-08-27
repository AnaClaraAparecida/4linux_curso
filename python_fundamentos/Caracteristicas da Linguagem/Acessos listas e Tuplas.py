# Tuplas e listas
#        0  1  2  3             4                  5
lista = [0, 1, 2, 3, ('11-11-2020', 88.50), [5, 6, 7, 8]]

# posiçao 4 -> n-1 -> 4 -1 = 3

print(lista[0]) #0
print(lista[-1]) #[5, 6, 7, 8]
print(lista[-1][2]) # 7

matriz = [
    [ 0, 1, 2], # l0
    [ 3, 4, 5], # l1
    [ 6, 7, 8]  # l2
#    c0 c1 c2
]

soma = 0
for l in range(len(matriz)): # loop linha
    for c in range(len(matriz[l])):
        soma += matriz[l][c] # linha e coluna

print(soma)

# Dicionarios

dic = {
    'nome': 'guilherme',
    'idade': 32,
    'dados': [0, 1, 2, 3, 4],
    'tuplas': (0, 1, 2, 3)
}

print(dic['tupla']) # (0, 1, 2, 3)
print(dic['tupla'][2]) # 2

                    # ('nome', 'idade', 'dados', 'tuplas')
for chave in dic.keys():
    if chave == 'idade':
        print(f'achei - ', dic[chave])

                    # 'guilherme', 32, [0, 1, 2, 3, 4], (0, 1, 2, 3)
for valor in dic.values():
    if valor =='32':
        print('achei a idade')

                    # [('nome', 'guilherme'), ('idade', 32), ('dados', [0, 1, 2, 3, 4]), (tupla', (0, 1, 2, 3))]
for chave, valor in dic.items():
    print(f'key: {chave} - value: {valor }')

# 1: chave, valor =('nome', 'guilherme')

a,b,c = 1, 2, 3
print(f'a => {a} - b => {b} - c => {c}') # a => 1, b => 2. c => 3