# 1. Capacidade de criar tipos de dados de acordo com o contexto
# 2. Os tipos de dados poderem manipular funções
# 3. Poder fazer uso de uma determinada funcionalidade sem precisar saber como ela é
# codiﬁcada

# neste caso qualquer tipo de dado pode manipular uma funçao
# Um exemplo dado na apostila, foi do principio de empilhar pratos, quando
# fazemos uma pila temos uma ordem caso querermos retirar algo da mesma. Se tentarmos
# retirar um prato que esta no  meio, seria mais complicado surgindo divergencias como,
# a pilhas desequilibrando e os pratos indo ao chao, assim como existe uma forma de retirar
# e formar, temos uma de adicionar, quando adicionamos um prato a pilha,
# o mesmo deve seguir a ordem de sempre ir ao fim da fila, sendo
# mais complicado tentar adicionar os pratos do inicio da pilha, tendo as mesma
# divergencias antes mensionadas

# De forma explicativa
# • Uma coleção de ítens (no exemplo, eram pratos)
# • Uma forma especíﬁca de adicionar ítens na pilha (sempre ao ﬁnal, ou no topo da pilha)
# • Uma forma especíﬁca de retirar ítens na pilha (também sempre ao ﬁnal, ou no topo da
# pilha

# De forma funcional
# 1. Criar uma coleção (poderia ser uma lista)
# 2. Criar uma função para adicionar ítens na pilha
# 3. Criar uma função para remover ítens da pilha
