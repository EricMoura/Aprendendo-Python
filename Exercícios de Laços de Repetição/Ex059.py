op = 0

while op!=5:
    n1 = float(input('\nInsira o 1° número: '))
    n2 = float(input('Insira o 2° número: '))

    print(' '*3,'[1] Somar')
    print(' '*3,'[2] Multiplicar')
    print(' '*3,'[3] Maior')
    print(' '*3,'[4] Novos números')
    print(' '*3,'[5] Sair')
    op = int(input('Opção: '))

    if (op==4):
        print('Informe os valores novamente:')
    elif op > 0 and op < 4:
        if op == 1:
            soma = n1+n2
            print(f'Soma = {soma} \n')
        elif op == 2:
            mult = n1*n2
            print(f'Multiplicação = {mult} \n')
        elif op == 3:
            if n1 > n2:
                print(f'O número {n1} é maior que {n2} \n')
            else:
                print(f'O número {n2} é maior que {n1} \n')

    else:
        print('Opção inválida!!')
print('Fim')