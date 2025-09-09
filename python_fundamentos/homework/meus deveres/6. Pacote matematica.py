from matematica.aritmetica import *
from matematica.geometria import *

n1 = int(input('n1: '))
n2 = int(input('n2: '))

print(f''
      f' + : {soma(n1, n2)}\n',
      f'- : {subtraçao(n1, n2)}\n',
      f'x : {multiplicaçao(n1, n2)}\n',
      f'/ : {divisao(n1, n2)}'
      )

n3 = float(input('Raio do circulo: '))
n4 = float(input('Lado do quadrado: '))

print(f''
      f'Area circulo: {area_circulo(n3)}\n',
      f'Area lado: {area_quadrado(n4)}')