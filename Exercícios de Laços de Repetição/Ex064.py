x = 0
soma = 0
entradas = 0
while x!= 999:
    n = int(input('Digite um número: '))
    entradas +=1

    if n == 999:
        x = n
    else:
        soma += n

print(f'Tentativas: {entradas}')
print(f'Soma das tentativas: {soma}')
