sdi = 0
hmaior = 0
qm20 = 0

for x in range(4):
    nome = input('Digite seu nome: ').strip()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo [m/f]:')

    sdi +=idade

    if idade<=0:
        print('Idade Inválida')
        x -= 1

    if idade>hmaior and sexo in 'Mm':
        hmaior = idade
        nvelho = nome

    if sexo=='f' and idade<20:
        qm20 += 1

    print('\n')

mdi = sdi/4

print(f'Média da idade do grupo: {mdi}')
print(f'Nome do homem mais velho: {nvelho}')
print(f'Mulheres com menos de 20 anos: {qm20}')