import montydb

client = montydb.MontyClient('cafe')

db = client.ingrediente

# find 

for documento in db.ingrediente.find():
    print(documento)

print(documento['nome'])
