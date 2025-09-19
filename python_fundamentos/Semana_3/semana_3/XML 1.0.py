# <> o valor da tag estará entre a abertura e fechamento de tags
# => <ano>2002</ano>

# pacote defusedxml ->  par ser utilizxado é necessaria instalação do pacote através do pip:
# => sub-pacote ElementTree
# O ElementTree possui um metodo chamdo "parse" que carrega o arquivo xml

# from defusedxml import ElementTree as ET
# arquivo_xml = ET.parse('arquivo.xml')

# => Para armazenar o conteúdo da raiz ou seja o nivel principal do arquivo, pode-se utilizar
# o "getroot"

# 1: importando o modulo XML
# from defusedxml import ElementTree as ET
# 2: Carregando o arquivo XML
# arquivo_xml = ET.parse('arquivo.xml')
# 3: armazenando o conteudo da raiz do XML
# root = arq_xml.getroot()

# no terminal:
# instalaçao do defusedxml no pip
# pip3 install defusedxml
