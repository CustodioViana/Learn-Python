print('Exercício Enunciados')
print(20 * '-')

"""
First Step
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

print('First Step')

number = input('Please, enter a integer number: ')

try:
    # number_int = number.isdigit()
    number_int = int(number)
    if (number_int % 2) == 0:
        print(f'{number} your number is EVEN')
    else:
        print(f'{number} your number is ODD')
except ValueError:
    print('You have not entered an integer number')

print(20 * '-')



"""
Second step
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

print('Second Step')

hh = input('Please, inform the hour:')
error = 'Sorry, but you entered wrong hours or minutes, try again!'

try:
    hh = float(hh)
    dia = (hh >= 0 and hh <= 11)
    tarde = (hh >= 12 and hh <= 17)
    noite = (hh >= 18 and hh <= 23)
    if dia:
        print(f"Good morning, it's exactly {hh}:00 o'clock ")
    elif tarde:
        print(f"Good afternoon, it's exactly {hh}:00 o'clock ")
    elif noite:
        print(f"Good night, it's exactly {hh}:00 o'clock ")
    else:
        print(error)  
except ValueError:
    print(error)

print(20 * '-')

"""
Third Step
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

print('Third Step')

name = input('Please, enter your name: ')
cont_name = len(name)

if cont_name <= 4:
    print('your name is too short!')
elif cont_name >= 5 and cont_name <= 6:
    print('your name is normal!')
elif cont_name > 5:
    print('Your name is too big')

print(20 * '-')