# 1) Escreva um programa que receba o ano de nascimento, e que ele retorne à geração
# a qual a pessoa pertence. Para deﬁnir a qual geração uma pessoa pertence temos a
# seguinte tabela:

# Geração       Intervalo
# Baby Boomer   Até 1964
# Geração X     1965 - 1979
# Geração Y     1980 - 1994
# Geração Z     1995 - Atual

# Para testar se seu script está funcionando, considere os seguintes resultados esperados:
#

ano = int(input('Informe seu ano de nascimento: '))

if ano <= 1964:
    print(f'Ano de nascimento: {ano} = Geração: "Baby Boomer"')
elif ano < 1979:
    print(f'Ano de nascimento: {ano} = Geração: "X"')
elif ano < 1994:
    print(f'Ano de nascimento: {ano} = Geração: "Y"')
else:
    print(f'Ano de nascimento: {ano} = Geração "Z"')