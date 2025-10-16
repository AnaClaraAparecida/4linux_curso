def primeiros_quadrados(i):
    quadrados = []
    for num in range(i):
        quadrados.append(num * num)
    return quadrados

lista_quadrados = [num * num for num in range(10)]

lista_quadrados_pares = [num * num for num in range(10) if num % 2 == 0]

def aplica_desconto(lista_de_compras, desconto_aplicado):
    return [(preco if preco < 100 else preco * desconto_aplicado) for preco in lista_de_compras]

preco = [88, 50, 110, 150, 10, 12, 90]
precos_com_desconto = aplica_desconto(preco, 0.9)