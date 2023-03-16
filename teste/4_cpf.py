# caso queira somente os números

# cpf = '746.824.890-70'
# cpf = ''.join(filter(str.isdigit, cpf))

# print(cpf)




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