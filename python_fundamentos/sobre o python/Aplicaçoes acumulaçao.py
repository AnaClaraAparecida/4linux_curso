## lista de compras

lista_de_compras = [
    ('Camiseta', 19.90),
    ('Calça Jeans', 20.50),
    ('Meia G', 5.90)
]

# problema: qual é o total desse carrinho de compras?

# tupla[0] => nome item
# tupla[1] => preço

print('resoluçao com o While')

#1: Definir as variaveis de controle
indice = 0
#2: armazenar o total
total_de_compras = 0

#3: cada linha da lista
while indice < len(lista_de_compras):
    #3.1: acessar o valor de preços de cada item acumulado na variavel total_de_compras
    total_de_compras += lista_de_compras[indice][1]
    indice += 1

print(f'O total de compras do seu carrinho: {total_de_compras}')

print('resoluçao com o For')

total = 0

for compra in lista_de_compras:
    total += compra[1]

print(f'Total de compras com o for: {total}')

#1: compra = lista_de_compra[0]
#    total += compra[1]
#2: compra = lista_de_compras[1]
#    total += compra[1]