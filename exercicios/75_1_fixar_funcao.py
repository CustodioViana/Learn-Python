print('Exerciocio 1')
"""
Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Farenheit ou vice-versa. 
Para cada opção, crie uma função. Crie uma terceira, que é um menu para o usuário escolher a opção desejada, 
onde esse menu chama a função de conversão correta.
"""
print('Conversão de Temperatura')

def C_para_F(cel):
    f = (cel * 5/9) + 32
    return print(f)

def F_para_C(far):
    c = (5/9) * (far-32)
    return print(c)

def menu():
    while True:
        escolha_1 = int(input('Qual unidade de temperatura deseja converter\n'
                  '[1] Celsius para Farenheit\n'
                  '[2] Farenheit para Celsius\n'
                  '[3] Sair\n'
                  ': '))

        if escolha_1 == 1:
            temp_C = int(input('Digite a temperatura em Celcius: '))
            Farenheit = C_para_F(temp_C)
            C_para_F
            print()
            continue

        elif escolha_1 == 2:
            temp_F = int(input('Digite a temperatura em Farenheit: '))
            Celcius = F_para_C(temp_F)
            F_para_C
            print()
            continue

        elif escolha_1 == 3:
            break

        else:
            print('Opção inválida')

menu()


print()
print(30*'-')
print('Exerciocio 2')
"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos através de uma função. 
Seu script também deve fornecer a média dos três números, através de uma segunda função que chama a primeira.
"""
print('3 Argumentos')




print()
print(30*'-')
print('Exerciocio 3')
"""
Faça um programa que recebe três números do usuário, e identifica o maior através de uma função e o menor número através de outra função.
"""

print()
print(30*'-')
print('Exerciocio 4')
"""
A probabilidade de dar um valor em um dado é 1/6 (uma em 6). Faça um script em Python que simule 1 milhão de lançamentos de dados e 
mostre a frequência que deu para cada número.
"""

print()
print(30*'-')
print('Exerciocio 5')
"""
A série de Fibonacci é uma sequência de números, cujos dois primeiros são 0 e 1. O termo seguinte da sequência é obtido somando os dois anteriores. 
Faça uma script em Python que solicite um inteiro positivo ao usuário, n. Então uma função exibe todos os termos da sequência até o n-ésimo termo. 
Use recursividade.
"""

print()
print(30*'-')
print('Exerciocio 6')
"""
Crie uma função que recebe um inteiro positivo e teste para saber se ele é primo ou não. Faça um script que recebe um inteiro 'n' e 
mostra todos os primos, de 1 até n.
"""

print()
print(30*'-')
print('Exerciocio 7')
"""
Um número é dito perfeito quando ele é igual a soma de seus fatores. Por exemplo, os fatores de 6 são 1, 2 e 3 (ou seja, podemos 
dividir 6 por 1, por 2 e por 3) e 6=1+2+3, logo 6 é um número perfeito. Escreva uma função que recebe um inteiro e dizer se é perfeito ou não. 
Em outra função, peça um inteiro n e mostre todos os números perfeitos até n.
"""
