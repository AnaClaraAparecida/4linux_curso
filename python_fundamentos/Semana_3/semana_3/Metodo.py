# Quando conseguimos generalizar um grupo a partir de características que os distinguem dos
# demais, dizemos que criamos uma classe

# class Pilha:
#     pass

# construtor a partir da instrução __init__

# class Pilha:
#     def __init__(self):
#         self.pilha = []

# armazenar uma informação a qual nos indica a posição do topo da
# lista, tendo em vista que ele é nosso indicador se um elemento pode ser retirado ou nao

# class Pilha:
#     def __init__(self):
#         self.pilha = []
#         self.topo = 0 -> o atributo top, esta zerado pois a lista esta vazia

# Comportamentos, são funções que realizam tarefas. Assim como os
# atributos, as funções em orientação à objetos são denominadas métodos.
# Vamos abaixo, criar um método que empilha ítens:

# class Pilha:
#    def __init__(self):
#        self.pilha = []
#        self.topo = 0
#    def empilhar(self, item):
#        self.pilha.append(item)
#        self.topo += 1

# Utilizamos o parâmetro item no método empilhar
# para que seja possível informar o ítem a ser incluído em nossa pilha.

# Vamos agora incluir outro comportamento, o de remover ítens de nossa lista:

# class Pilha:
#    def __init__(self):
#        self.pilha = []
#        self.topo = 0
#    def empilhar(self, item):
#        self.pilha.append(item)
#        self.topo += 1
#    def desempilhar(self):
#        if self.topo != 0:
#            item_removido = pilha[-1]
#            del self.pilha[-1]
#            self.topo -= 1
#            return item_removido
#         else:
#            return 'pilha vazia'

# Para saber se temos ítens empilhados, olhamos para nosso atributo topo.
# Se ele for diferente de zero, signiﬁca que já empilhamos algo
# Caso a pilha não estiver vazia, utilizamos da instrução del para remover um ítem da pilha com
# referência índice -1 da pilha, que sempre faz referência ao último elemento de uma coleção.
# Além disso, retiramos uma unidade do topo para indicar que a última posição diminuiu, e
# retornamos o ítem removido da pilha

# Veja abaixo como criar uma instância
# da pilha, ou um objeto da mesma:

# >>> class Pilha:
# ...
# ...
# ...def __init__(self):
# self.pilha = []
# self.topo = 0
# ...
# ...
# ...def empilhar(self, item):
# self.pilha.append(item)
# self.topo +=1
# ...
# def desempilhar(self):
# ...
# if self.topo !=0:
# ...
# item_removido = pilha[-1]
# ...
# del self.pilha[-1]
# ...
# self.topo -= 1
# ...
# return item_removido
# ...
# >>> p1 = Pilha() # Cria um objeto da classe Pilha
# >>> p1.
# p1.desempilhar( p1.empilhar(
# p1.pilha
# >>> # empilhar itens
# >>> p1.empilhar('prato de porcelana')
# >>> p1.empilhar('prato de vidro')
# >>> p1.empilhar('prato de sobremesa')
# >>> # desempilhar itens:
# >>> p1.desempilhar()
# 'prato de sobremesa'
# >>> p1.desempilhar()
# 'prato de vidro'
# >>> p1.desempilhar()
# 'prato de porcelana'
# >>> p1.desempilhar()
# 'pilha vazia'
# >>> p1.desempilhar()
# 'pilha vazia'