def incrementa_um(x):
    #f(x) = x + 1
    res = x + 1
    print(res)

incrementa_um(5)  # 6
incrementa_um()

#f(x) = 1
def saudaçao():
    print('Ola!')

def soma(n1, n2):
    return n1 +n2

x = 10
y = 15
print(soma(x, y))# 15

## valor padrão

def outra_soma(x1 = 0, x2 = 0):
    return x1 + x2

print(outra_soma())
print(outra_soma(33, 66))

def multiplicaçao(n1 = 1, n2 = 1):
    return n1 * n2

a = multiplicaçao(2, 4)
b = multiplicaçao(3)
c = multiplicaçao()

##
                          # args -> arguments
def soma_multiplos_valores(*args):
    print(type(args))
    print(args)
    soma = 0
    for num in args:
        soma += num

    return soma

                # keyword arguments -> kwargs
def soma_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)

    soma = 0
    for value in kwargs.values():
        soma += value

    return soma
   