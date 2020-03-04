x=0
totalgasto = 0
p1000 = 0
pmaisb = 0
nmaisb = 0
while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))

    totalgasto += preco

    if preco >= 1000:
        p1000 +=1

    if pmaisb == 0:
        pmaisb = preco
        nmaisb = nome

    if pmaisb > preco:
        pmaisb = preco
        nmaisb = nome

    while True:
        esc = input('Deseja continuar?[S/N]: ').upper().rstrip()

        if esc in 'Nn':
            x+=1
            break
        if esc in 'Ss':
            break
        if esc not in 'SsNn':
            print('Entrada inválida!')
    if x == 1:
        break

print(f'Total gasto na compra: {totalgasto}')
print(f'Produtos que custam +R$1000: {p1000}')
print(f'Nome do produto mais barato: {nmaisb} , R${pmaisb}')