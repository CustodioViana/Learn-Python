"""
Calculo do primeiro dígito do CPF
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '746.824.890-70'
cpf = ''.join(filter(str.isdigit, cpf))

soma = 0


while True:
    try:
        resultado = int(input('Deseja buscar valor final com 9 ou 11 digitos?\n'
                        '[1] para 9 digitos\n'
                        '[2] para 11 digitos:  '))

        if resultado == 1:
            for i in range(9):
                numero = int(cpf[i])
                mult = 10 - i
                soma += numero * mult
            break
        elif resultado == 2:

            for i in range(len(cpf)):
                numero = int(cpf[i])
                mult = len(cpf) - i
                soma += numero * mult
            break

    except:
        print('-')
        print('Tente um operador válido')
        print('-')

print('-')
print(f'Total da soma é {soma}')
print('-')

subtotal = soma * 10
print(f'Total da multiplicação é {subtotal}')
print('-')

total = subtotal % 11
print(f'A sobra é {total}')
print('-')

print('O resultado é zero' if total > 9 else 'O primeiro valor do CPF é 7')






print('Outra forma de se fazer')

cpf = '746.824.890-70'
cpf = ''.join(filter(str.isdigit, cpf))
soma = 0
print(cpf)
print('-')

for i in range(9):
    numero = int(cpf[i])
    mult = 10 - i
    soma += numero * mult

print(f'Total da soma é {soma}')
print('-')

subtotal = soma * 10
print(f'Total da multiplicação é {subtotal}')
print('-')

total = subtotal % 11
print(f'A sobra é {total}')
print('-')

print('O resultado é zero' if total > 9 else 'O primeiro valor do CPF é 7')
