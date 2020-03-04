sdi = 0
qm20 = 0
qh = 0
x = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo [m/f]:').rstrip()

    if idade<=0:
        print('Idade Inválida')

    if idade>=18:
        sdi += 1

    if sexo in 'Mm':
        qh += 1

    elif sexo in 'Ff' and idade<20:
        qm20 += 1

    else:
        print('Sexo inválido!')
    print('\n')

    while True:
        esc = input('[S] sair ou [C] continuar: ').rstrip()

        if esc in 'Cc':
            break
        if esc in 'Ss':
            x = 1
            break

    if x == 1:
        break

print(f'Pessoas com mais de 18 anos: {sdi}')
print(f'Quantidade de homens: {qh}')
print(f'Mulheres com menos de 20 anos: {qm20}')