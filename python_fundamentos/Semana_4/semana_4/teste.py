import unittest
from ecommerce import Produto, CarrinhoDeCompra

class TesteEcommerce(unittest.TestCase):
    def setUp(self): # preparaçao do experimento
        self.p1 = Produto('Camiseta', 9.90)
        self.p2 = Produto('Calça Jeans', 10.90)
        self.c1 = CarrinhoDeCompra()

    def adiciona_produtos_no_carrinho(self): # açao 1 a ser valida
        self.c1.adicionaProduto(self.p1)
        self.c1.adicionaProduto(self.p2)

    def calcula_total_de_compras(self): # açao 1
        self.total_de_compras = self.c1.calculaTotalCompras()

    def make_assertions(self): # checagem dos resultados
        self.assertEqual(2, len(self.c1.carrinho))
        self.assertEqual(self.p1.preço + self.p2, self.total_de_compras)

    def test_ecommerce(self): # executa passo a passo e valida o teste
        self.adiciona_produtos_no_carrinho()
        self.calcula_total_de_compras()
        self.make_assertions()








