# O processo de encapsulamento, seria a forma como a python tem de 'proteger' informaçoes,
# o python tem a funcionalidade, baseado no processo de agrupar informaçoes e funcionalidades,
# e manipular esses dados para que sejam escondidos de outros usuarios
class A:
    def __init__(self):
        self.pilha = []
        self.topo = 0
        self._uso_interno = True
        self.__mangled = True  #-> esconder realmente

objeto = A()
print(objeto.pilha)
print(objeto.topo)