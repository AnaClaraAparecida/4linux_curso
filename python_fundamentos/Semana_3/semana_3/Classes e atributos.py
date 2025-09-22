# objetos a serem empilhados (algum lugar para empilhar isso) <> atributos
# o ultimo elemento da pilha, sempre é o primeiro a sair dela <> metodos

class Pilha: # primeira letra em maiusculo
    def __init__(self): # variaveis <> atributos self -> o próprio objeto que está sendo criado
        self.pilha = []
        self.topo = 0
