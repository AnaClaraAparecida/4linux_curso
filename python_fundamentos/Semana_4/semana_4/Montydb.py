import montydb 

#1: conectar com o banco 
client = montydb.MontyClient('cafe')

# 2: criar uma collection 
db = client.ingrediente 

#3: inserir um novo documento 
doc = {
    'nome': 'agua',
    'descriçao': 'xpto',
    'tipo': 'liquido',
    'unidade_medida': 'ml'
}

db.ingrediente.insert_one(doc) 

import montydb

client = montydb.MontyClient('cafe')

db = client.ingrediente

# find 

for documento in db.ingrediente.find():
    print(documento)

print(documento['nome'])


import montydb 

# conexao 
client = montydb.MontyClient('cafe')

# escolha o banco 
db = client.ingrediente

filtro = {'nome': 'cafe'}

# acessar a collection e executa atualizaçao 
db.ingrediente.update_one({'nome':'cafe'}, {'$set': {}})