linha = 50 * '-'
import os
"""
Faça uma lista de comprar com listas
- O usuário deve ter possibilidade de inserir, apagar e listar valores da sua lista
- Não permita que o programa quebre com erros de ídices inexistenste na lista
"""

# alimento = ['arroz', 'feijoa', 'macarrao', 'batata']
# bebida = ['coca', 'agua', 'suco', 'cafe']


alimento = []
bebida = []
lista = ' '
ind_lis = range(len(lista))
while True:

    print(linha)
    print(lista)
    print(alimento)
    print(bebida)
    print(linha)
    entrada = input('Escolha uma função desejada:\n'
                    '[I]nserir\n'
                    '[A]pagar\n'
                    '[V]erificar\n'
                    '[S]air\n').upper()
    
    try:
        if entrada == 'I':  # inserir item
            
            produto = input('Oque deseja inseir? ')
            categoria = int(input('Em qual lista?\n'
                            '[1]Alimento\n'
                            '[2]Bebidas\n'))
            
            if categoria == 1:
                alimento.append(produto)
                print(f'Você adicionou {produto} na categoria ALIMENTO')
            elif categoria == 2:
                bebida.append(produto)
                print(f'Você adicionou {produto} na categoria BEBIDA')
            else:
                print('Escreva um númeor válido')
                continue
            os.system('cls')
        elif entrada == 'A': 
            for ver in ind_lis:
                print(ver, lista[ver]) 
            opcao = input('Selecione uma opção:\n'
                  '[A]pagar\n'
                  '[S]air\n').upper()

            if opcao == 'B':           
                apg = int(input('Digite o número para apagar: '))
                lista.pop(apg)
            
            elif opcao == 'S':
                sair = input('Deseja sair?\n'
                            'Digite [S]air ou [C]ontinuar: ').upper()
            continue
            os.system('cls')
        elif entrada == 'V':
            for ver in ind_lis:
                print(ver, lista[ver])            
            continue
            os.system('cls')
        elif entrada == 'S':
            sair = input('Deseja sair?\n'
                 'Digite [S]air ou [C]ontinuar: ').upper()
            if 'S' in sair:
                break
        else:
            print('teste com else')
            continue

    
    except:
        print('Digite o valor da função ou categoria carrote!')
        os.system('cls')

