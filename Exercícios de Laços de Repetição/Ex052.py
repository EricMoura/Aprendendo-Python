print(' '*5,'Identificação de números primos',' '*5)
pr = int(input('Digite um número: '))
tot = 0

for c in range(1, pr+1):
    if pr%c==0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')

    print(f'{c}', end='')

print(f'\033[m\nO número {pr} foi divisível {tot} vezes.')
if tot == 2:
    print('Por isso ele é primo.')
else:
    print('Por isso ele não é primo.')