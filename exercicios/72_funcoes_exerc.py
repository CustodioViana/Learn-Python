# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.
# Criar uma função que retorne se o número é par ou impar.


def multiplicador(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total
    
def comparador(resul):
    if resul % 2 == 0: 
        return f'Esse número {resul} é par'
    return f'Esse número {resul} é ímpar'

mult = multiplicador(1, 2, 3, 4, 5, 6)
comp = comparador(mult)

print(mult)
print(comp)