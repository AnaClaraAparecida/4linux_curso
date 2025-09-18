from xml.etree.ElementTree import Element, SubElement, ElementTree, Comment

# Raiz do XML
raiz = Element('partida')

raiz.append(Comment('Partida realizada em 2002 com o gol antologico do meia atacante '))

# aidiconar os elementos a arvore
ano = SubElement(raiz, 'ano')

# definir o 'valor' => text
ano.text = '2002'

torneio = SubElement(raiz, 'torneio')
torneio.text = 'Rio Sao Paulo'

# tag times
times = SubElement(raiz, 'times')

mandante = SubElement(times, 'mandante')
mandante.text = 'Sao Paulo'

visitante = SubElement(times, 'visitante')
visitante.text = 'Palmeiras'

resultado = SubElement(raiz, 'resultado')
resultado.text = '2X4'

# gols mandante
gols = SubElement(resultado, 'gols')
gols_mandante = SubElement(gols, 'mandante')

gols_mandante_jogador1 = SubElement(gols_mandante, 'jogador1')
gols_mandante_jogador1.text = 'França'

gols_mandante_jogador2 = SubElement(gols_mandante, 'jogador2')
gols_mandante_jogador2.text = 'Kaka'

# gols_visitante
gols_visitante = SubElement(gols, 'visitante')

gols_visitante_jogador1 = SubElement(gols_visitante, 'jogador1')
gols_visitante_jogador1.text = 'Marao'

gols_visitante_jogador2 = SubElement(gols_visitante, 'jogador2')
gols_visitante_jogador2.text = 'Claudecir'

gols_visitante_jogador3 = SubElement(gols_visitante, 'jogador3')
gols_visitante_jogador3.text = 'Alex'

gols_visitante_jogador4 = SubElement(gols_visitante, 'jogador4')
gols_visitante_jogador4.text = 'Arce'

ElementTree(raiz).write('saida.xml')