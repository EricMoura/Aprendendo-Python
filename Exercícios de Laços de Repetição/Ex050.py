soma = 0
for x in range(0,6):
    y = int(input(f'Digite o {x+1}° número: '))
    if y%2==0:
        soma += y
print(f'Soma dos números pares: {soma}')