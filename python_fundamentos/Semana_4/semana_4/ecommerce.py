class Produto:
    def __init__(self,
        nome = '',
        preço = 0.0
    ):
        self.nome = nome
        self.preço = preço

class CarrinhoDeCompra:
    def __init__(self):
        self.carrinho = []

    def adicionaProduto(self, produto):
        self.carrinho.append(produto)

    def calculaTotalCompras(self):
        total = 0
        for produto in self.carrinho:
            total += produto.preço

        return total

