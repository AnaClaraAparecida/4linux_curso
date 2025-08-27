## estruturas de repetiçao


## lista de compras

lista_de_compras = [
    ('Camiseta', 19.90),
    ('Calça Jeans', 20.50),
    ('Meia G', 5.90),
    ('camiseta', 10.00)
]

# Problema: totalizar o carrinho de compras aplicando 10% de desc. na camiseta
total = 0
desconto = 0.9

for compra in lista_de_compras:
    if 'camiseta' in compra[0].lower():
        total += compra[1] * desconto
    else:
        total += compra[1]

print(f'Valor total de compras aplicando o desconto: {total:.2f}')