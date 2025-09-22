# objetos a serem empilhados (algum lugar para empilhar isso) <> atributos
# o ultimo elemento da pilha, sempre é o primeiro a sair dela <> metodos

class Pilha:
    def __init__(self): # variaveis <> atributos self -> o próprio objeto que está sendo criado
        self.pilha = []
        self.topo = 0

    # comportamentos
    # adicionar elementos na pilha (empilhar)
    def empilhar(self, item):
        self.pilha.append(item)
        self.topo += 1

    # remover elementos da pilha (desempilhar)
    def desempilhar(self):
        if not self.vazio():
            item_removido = self.pilha[-1]
            del self.pilha[-1]
            self.topo -= 1
            return f'o item{item_removido} foi retirado da pilha'
        return 'Pilha esta vazia'

    def vazio(self):
        return len(self.pilha) == 0