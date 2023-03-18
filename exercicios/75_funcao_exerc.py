# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.

entrada = int(input('Digite: '))

def calculo(num_cal):
    def duplicar():
        return num_cal * 2
    
    def triplicar():
        return num_cal * 3
    
    def quadruplicar():
        return num_cal * 4
    
    return duplicar, triplicar, quadruplicar

numer = calculo(entrada)
duplicar, triplicar, quadruplicar = numer

print(duplicar())
print(triplicar())
print(quadruplicar())

print('-----------------------------------------------------------------------------')
print('Versão do professor mais simples.')

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
