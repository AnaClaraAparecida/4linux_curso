# Ex 1
class Colaborador:
    def __init__(self):
        self.nome = ''
        self.endereço = ''
        self.idade = 0
        self.salario = 0.0
        self.cargo = ''
        self.encargos = 0.25

    def apresentaColaborador(self):
        return (f'Colaborador: {self.nome}\n'
                f'Cargo: {self.cargo}\n'
                f'Salario: {self.salario:.2f}\n')

c1 = Colaborador()
c1.nome = 'Guilherme'
c1.cargo = 'Instrutor'
c1.salario = 10.50
print(c1.apresentaColaborador())


#class Gerente(Colaborador): -> apenas dessa forma, ele ja copia as infos do primeiro init 'Herança'
#    pass

class Gerente(Colaborador):
    def calcular_salario(self, bonus):
        return self.salario * bonus


# Ex 2
class Mae:
    def __init__(self):
        self.nome = ''
        self.nacionalidade = 'Francesa'

    def falar_frances(self):
        return 'Bounjour!'

class Pai:
    def __init__(self):
        self.nome = ''
        self.nacionalidade  = 'Ingles'

    def falar_ingles(self):
        return 'Good morning!'

class Filha(Mae, Pai):
    pass

f1 = Filha()
print(f1.falar_ingles(), f1.falar_frances())