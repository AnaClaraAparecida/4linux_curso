# as SGBDs (Sistemas Gerenciados de Banco de Dados), foram criadas pelo fato de muitas empresas investirem
# em softwares dedicadcos a gestao dos dados, porem comoo esse processo deveria portar as informaçoes, ja que cada
# software lida com um padrao e estrutura de dados especifico?

# para a soluçao do probelma Peter Chen propros um modelo de padronagem chamado Entidade- Relacionamento,
# que se utiliza graficos ára representar:

# Entidade -> que representam as 'coisas' ou objetos que o sistema deve armazenar
# Atributos -> eles caracterizam as coisas ou os objetos citados antes
# Relacionamentos -> descreve a associaçao ou ligamento entre dois objetos

# Como exemplo para a abordagem relacional:

# -> Uma cafeteria minimalista, existe um totem de auto atendimento e um barista re faz e entrega os pedidos de forma
# direta ao cliente

# a partir desse contexto e necesssairo que identifiquemos quem sao as ENTIDADES relevantes para armazenar as infos.
# e para isso é necessario identificar o contexto e o funcionamento das tividades

# -> 1. O cliente pode escolher entre doces ou bebidas contando que esteja no cardapio
# -> 2. Apos escolher sera necessario o pagamento por debito ou credito
# -> 3. Depois do pagamento um nome sera requisitado para a retirada do pedido
# -> 4. O barista recebe o pedido e o faz, entregando diretamento ao cliente

# Observando o primerio ponto, os itens em destaque sao:
# -> BEBIDAS, DOCES e CARDAPIO

# Para cada elemento, precisamos definir o atributo principal que os definem
# -> BEBIDAS:
#           Nome da bebida,
#           Tipo da bebida (quente ou fria),
#           Receita da bebida (quantidade de ingredientes),
#           Preço
# -> DOCES:
#           Nome do doce, Tipo de doce,
#           Receita,
#           Preço
# -> CARDAPIO:
#           Exibir os doces e bebidas disponiveis

# Obeservando, consegimos ver a similaridade entre bebidas e doces, sendo um produto que pode ser composto por:
# nome, tipo, receita e preço.
