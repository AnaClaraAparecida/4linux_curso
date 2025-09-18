import json

file = open('json.txt')
arquivo = json.load(file)
print(arquivo)
print(type(arquivo))

print(arquivo['torneio'])
print(arquivo['ano'])
print(arquivo['estado'])
print(arquivo['estádio'])
print(arquivo['mandante'])
print(arquivo['visitante'])
print(arquivo['placar_mandante'])
print(arquivo['placar_visitante'])
print(arquivo['gols'])
print(arquivo['gols'][0])