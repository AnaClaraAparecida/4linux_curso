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


#class Gerente(Colaborador): -> apenas dessa forma, ele ja copia as infos do primeiro init
#    pass