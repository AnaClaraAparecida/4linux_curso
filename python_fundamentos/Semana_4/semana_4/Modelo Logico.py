# -> Cada entidade vira uma tabela.
# Cada atributo vira uma coluna.
#
# Cada registro representa uma ocorrência da entidade.
#
# Problemas Identificados:
# Produtos podem ser registrados mais de uma vez.
#
# Dificuldade em referenciar corretamente um produto.
#
# Produtos com mesmo nome geram ambiguidade.
#
# Campo "receita" tem informações redundantes.
#
# Soluções:
# Chave Primária: Identificador único para cada produto.
#
# Normalização: Reduz redundância, separando dados em tabelas específicas.