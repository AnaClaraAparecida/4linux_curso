# comando if (se):
if 5 < 4:
    print('Cinco é maior do que quatro')
    print('Segunda linha dentro do if')

print('Print fora da indentação')

# uso de variaveis com if:
x = 10
y = 12

if x > y:
    print()

# multiplos testes com if:
nome = 'Tiago'
idade = 27

if nome == 'Tiago' and idade < 25:
    print('Tiago ainda é jovem!')

#Anotações ->
# decisões aninhadas
# calculo do IMC
# formula: peso (kg) / (altura ** 2)

#capturar peso e altura
peso = float(input('Digite seu peso: '))
altura = float(input('Informe seu peso: '))

#calcular o imc
imc = peso / (altura ** 2)

#classificar o imc
if imc < 18.5:
    print(f'Baixo peso - IMC: {imc}')
elif imc < 24.9:
    print(f'Peso normal - IMC: {imc}')
elif imc < 29.9:
    print(f'Pre Obesidade - IMC: {imc}')
elif imc < 34.9:
    print(f'Obesidade Grau I -IMC: {imc}')
elif imc < 39.9:
    print(f'Obesidade Grau II -IMC: {imc}')
else:
    print(f'Obesidade Grau III -IMC: {imc}')