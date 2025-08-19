# >>> # cria um dicionário
# ...
# >>> dic = {'João':'551155558877', 'Felipe':'551988776633', 'Rafael':'551136879985'}
# >>> # copia um dicionário para outra variável
# ...
# >>> copia = dic.copy()
# >>> print(copia)
# {'João':'551155558877', 'Felipe':'551988776633', 'Rafael':'551136879985'}
# >>> # retorna um valor a partir de uma chave utilizando o método get
# ...
# >>> copia.get('Rafael')
# '551136879985'
# >>> # remove um par chave e valor a partir de uma chave informada através do método pop
# ...
# >>> copia.pop('João')
# '551155558877'
# >>> print(copia)
# {'Felipe':'551988776633', 'Rafael':'551136879985'}
# >>> # remove o último par chave e valor utilizando o método popitem
# ...
# >>> copia.popitem()
# 'Rafael':'551136879985'
# >>> # retorna os valores de um dicionário
# ...
# >>> copia['Marcella'] = '551144668578'
# >>> copia.values()
# dict_values(['551988776633','551144668578'])
# >>> # remove todos os valores de um dicionário
# ...
# >>> copia.clear()
# >>> print(copia)
# {}

dic = {}
dic['nome'] = 'Guilherme Zanelato Correa'
print(dic)