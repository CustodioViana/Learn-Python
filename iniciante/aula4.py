#Tipos int e float

#int -> Número Inteiro
#O tipo int representa qualquer número
#posito ou negativo. 
#int sem sina é considerado positivo

print('int = Números inteiros')
print(11, -11, 0)

#float -> Número com ponto flutuante
#O tipo float representa qualquer número
#posito ou negativo com ponto flutuante
#floar sem sina é considerado positivo

print('float = Números Fracionados')
print(11.0, -11.0, 0.0)
print()

#A função type mostra o tipo que o Python inferiu o valor
print(11, end="")
print(type(11))
print(-11, end="")
print(type(-11))
print(0, end="")
print(type(0))
print(11.0, end="")
print(type(11.0))
print(-11.0, end="")
print(type(-11.0))
print(0.0, end="")
print(type(-11.0))