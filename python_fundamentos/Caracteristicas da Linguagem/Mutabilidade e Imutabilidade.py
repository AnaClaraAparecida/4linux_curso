# dados imutaveis

tuplas = (0, 1, 2, 3)
tuplas += 4 ,5 ,6 , 7
string = ''
inteiros = 1
floats = 10.5

def soma(n1, n2, resp):
    resp = n1 + n2
    return resp

n1, n2, n3 = 10, 20, 0

print(soma(n1, n2, n3))

# a) = 0
# b) = 70
# c) Vai acontecer um erro
# d) nenhuma das anteriores

# dados mutaveis

list = [0, 1, 2, 3, 'jujuba']
dic = {}
dic['nova_chave']= 1

def adiciona_item(lista, item):
    lista.append(item)

adiciona_item(list, 'macarrao')

# list
# a) [0, 1, 2, 3, 'jujuba', 'macarrao']
# b) estara do mesmo jeito
# c) Vai acontecer um erro
# d) nenhuma das anteriores