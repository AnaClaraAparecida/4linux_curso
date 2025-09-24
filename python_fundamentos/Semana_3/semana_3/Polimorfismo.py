class Pofissao:
    def __init__(self):
        self.classe = ''
        self.habilidade = ''

class Mago:
    def __init__(self):
        self.classe = 'Mago'
        self.habilidade = 'Magia'

    def atacar(self):
        return 'Ataque com Magia'

class Soldado(Mago):
    def __init__(self):
        self.classe = 'Soldado'
        self.habilidad = 'Uso de espada'
    def atacar(self):
        return 'Ataque de espada'

class Arqueiro:
    def __init__(self):
        self.classe = 'Arqueiro'
        self.habilidade = 'Uso de arco e flechas'

    def atacar(self):
        return 'Ataque a distancia em arco e flecha'

m1 = Mago()
s1 = Soldado()
a1 = Arqueiro()

print(m1.atacar())
print(s1.atacar())
