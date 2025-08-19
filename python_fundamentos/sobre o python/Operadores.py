# Anotaçoes ->

# 2.5 operadores lógicos
#
# texto = 'um texto qualquer
# texto.startswitch('um') -> True
#
# 5 > 5 -> false
# 5 >= 5 -> True
#
# AND
# ( 5 >= 5 ) and ( 4 > 3 ) -> True
# ( 5 >= 5 ) and ( 4 < 3 ) -> False
# ( 5 > 5 ) and ( 4 < 3 ) -> False
#
# True and True => True
# True and False => False
# False and True => False
# False and False => False
#
# OR
# ( 5 >= 5 ) or ( 4 > 3 ) -> True
# ( 5 > 5 ) or ( 4 < 3 ) -> True
# ( 5 > 5 ) and ( 4 < 3 ) -> False
#
# True or True => True
# True or False => True
# False or True => True
# False or False => False
#
# NOT
# 5 > 5 -> False
# not ( 5 > 5) -> True
#
# 5 == 5 -> True

# 2.6 operadores de pertencimento
#
# 'um texto qualquer'
# 'qualquer' in texto -> True
# 'xxx' in texto -> False
# 'xxx' not in texto -> True
#
# texto.split()
# ['um', 'texto', 'qualquer']
# 'um' in texto.split() -> True