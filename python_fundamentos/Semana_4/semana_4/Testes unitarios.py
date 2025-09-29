
from random import randint
import unittest
import calculo

def soma (x, y):
    return x + y


class TesteCalculadora(unittest.TestCase): # -> pode ser definido como um arquivo teste, antecedendo com 'test' no inicio
    def test_soma(self):
        n1 = randint(0,999)
        n2 = randint(0,999)
        soma = n1 + n2
        self.assertEqual(soma, calculo.soma(n1,n2))

    def test_divisao_esperada(self):
        n1 = randint(0,999)
        n2 = randint(1,999)
        div = n1 / n2
        self.assertEqual(div, calculo.divisao(n1,n2))

    def test_divisao_por_zero(self):
        n1 = randint(0,999)
        n2 = 0
        div_zero = 'Erro ao divir por zero'
        self.assertEqual(div_zero, calculo.divisao(n1, n2))