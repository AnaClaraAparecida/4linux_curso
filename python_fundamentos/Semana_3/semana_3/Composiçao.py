# Clientes -> produto {nome, preço, sku} <-> caarrinho {add item, remover item, consolidar compra}

class Produto:
    def __init__(self):
        sku = ''
        nome = ''
        desc = ''
        preço = 0.0

        self.sku = sku
        self.nome = nome
        self.desc = desc
        self.preço = preço

class CarrinhoDeCompras:
    def __init__(self):
        self.carrinho = []
        self.quant_produto = 0

    def adicionar_produto(self, produto):
        self.carrinho.append(produto)
        self.quant_produto += 1
        return f'Produto {produto.nome} adicionado com sucesso'

    def remover_produto(self, nome_produto):
        removido = ''

        for produto in self.carrinho and not removido:
            if produto.nome == nome_produto:
                self.carrinho.remove(produto)
                self.quant_produto -= 1
                return f'O produto {produto.nome}, foi removido com sucesso'
        return f'O produto {nome_produto}, nao foi encontrado'

    def calculaTotal(self):
        soma = 0
        for produto in self.carrinho:
            soma += produto.preço

        return soma

p1 = Produto()
p1.nome = 'pera'
p1.preço =  6.50

p2 = Produto()
p2.nome = 'maça'
p2.preço =  4.50

p3 = Produto()
p3.nome = 'melao'
p3.preço =  7.50

c1 = CarrinhoDeCompras()
print(c1.adicionar_produto(p1))
print(c1.adicionar_produto(p2))
print(c1.adicionar_produto(p3))

print(c1.calculaTotal())
print(c1.remover_produto('maça'))
c1.calculaTotal()