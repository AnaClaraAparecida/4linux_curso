
from random import randint
import pymongo


client = pymongo.MongoClient()
db = client.python_fundamentos 

nome = ['Guilherme', 'Luciana', 'Julio', 'hector', 'leticia', 'luana', 'felipe' ]
uf = ['BA', 'MA', 'SP', 'MG', 'RS', 'MS']

def gerador_documentos(quantidade):
    for parte in quantidade:
        dic = {
            'id': f'{randint(0,9)}{randint(0,9)}{randint(0,9)}',
            'nome': f'{nome[randint(0, len(nome)-1)]}',
            'idade': randint(0,55),
            'UF': f'{uf[randint(0,len(uf)-1)]}'
        }

        yield dic