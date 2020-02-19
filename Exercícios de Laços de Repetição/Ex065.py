x=1
maior = 0
menor = 0
n = 0
soma = 0

while x!=0:
    num = float(input('Digite um número: '))
    n +=1
    soma += num

    if maior == 0 and menor==0:
        maior = num
        menor = num
    elif maior > num:
        maior = num
    elif menor < num:
        menor = num

    y = 0
    while y==0:
        r = str(input('Quer digitar outro valor?[S/N]: ')).upper()

        if r != 'S' and r != 'N':
            print('Resposta inválida')
            y = 1
        elif r=='S':
            x=1
            y=1
        elif r=='N':
            x=0
            y=1

md = soma/n

print(f'\nMédia dos números: {md}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')