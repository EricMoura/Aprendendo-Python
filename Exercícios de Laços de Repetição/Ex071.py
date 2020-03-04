x = 0
print('='*50)
print('\t\t\t\t Banco Moura ')
print('='*50)
while True:
    valor = int(input('Qual valor a ser sacado?: R$ '))

    resto = 0

    nota50 = valor//50
    resto = valor%50

    nota20 = resto//20
    resto = resto%20

    nota10 = resto//10
    resto = resto%10

    nota1 = resto//1

    print('Serão entregues: ')
    print(f'{nota50} notas de R$ 50,00')
    print(f'{nota20} notas de R$ 20,00')
    print(f'{nota10} notas de R$ 10,00')
    print(f'{nota1} notas de R$ 1,00')

    esc = input('Deseja fazer outro saque?[S/N]: ').upper()

    while True:
        if esc in 'Ss':
            break
        if esc in 'Nn':
            x = 1
            break
        if esc not in 'SsNs':
            print('Entrada Inválida!!!')

    if x == 1:
        break

print('Volte sempre ao Banco Moura! Tenha um bom dia!!!')

