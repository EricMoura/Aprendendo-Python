import random

m = ('='*8)
print(f'{m} Jokenpö {m}')
print(f'{" "*4} Vença a Máquina')
maq = random.randint(1,3)

esc = int(input('1-Pedra   2-Papel   3-Tesoura:  '))

if maq==1:
    if esc==1:
        print('Empate!')
    elif esc==2:
        print('Você ganhou! Papel ganha de pedra.')
    else:
        print('Você perdeu! Tesoura perde para pedra.')
elif maq==2:
    if esc == 2:
        print('Empate!')
    elif esc == 3:
        print('Você ganhou! Tesoura ganha de papel.')
    else:
        print('Você perdeu! Papel ganha de pedra.')
elif maq==3:
    if esc==3:
        print('Empate!')
    elif esc == 1:
        print('Você ganhou! Pedra ganha de tesoura.')
    else:
        print('Você perdeu! Tesoura ganha de papel.')
else:
    print('Opção Inválida')