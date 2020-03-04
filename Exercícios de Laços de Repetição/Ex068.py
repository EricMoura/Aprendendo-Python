from random import randint

print('','=-'*20,'\n\t\tVAMOS JOGAR PAR OU ÍMPAR\n','=-'*20)
vit = 0

while True:
    valor = int(input('Diga um valor: '))
    pi = input('Par ou Ímpar?[P/I]: ').upper().rstrip()

    comp = randint(0,10)

    soma = valor+comp

    if pi == 'I':
        if soma%2 != 0:
            print('_'*40)
            print(f'Você jogou {valor} e o computador {comp}. Total de {soma} DEU ÍMPAR')
            print('_' * 40)
            print('Você ganhou!!!')
            vit +=1
        if soma%2 == 0:
            print('_' * 40)
            print(f'Você jogou {valor} e o computador {comp}. Total de {soma} DEU PAR')
            print('_' * 40)
            print('Você perdeu!!!')
            break
    elif pi == 'P':
        if soma%2 != 0:
            print('_' * 40)
            print(f'Você jogou {valor} e o computador {comp}. Total de {soma} DEU ÍMPAR')
            print('_' * 40)
            print('Você perdeu!!!')
            break
        if soma%2 == 0:
            print('_' * 40)
            print(f'Você jogou {valor} e o computador {comp}. Total de {soma} DEU PAR')
            print('_' * 40)
            print('Você ganhou!!!')
            vit += 1
    else:
        print('Entrada inválida')

print('=-'*20)
print(f'GAME OVER! Você ganhou {vit} vezes')
print('=-'*20)


