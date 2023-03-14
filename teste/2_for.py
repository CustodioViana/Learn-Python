palavra_secreta = input(': ')
letra_ok = ''

while True:
    letra = input('Digite uma letra: ')
    for i in range(len(palavra_secreta)):
        if letra == palavra_secreta[i]:
            letra_ok = letra

    print(letra_ok)

