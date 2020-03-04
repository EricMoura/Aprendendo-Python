x = 0
soma = 0
entradas = 0
while True:
    n = int(input('Digite um número (999 para parar): '))

    if n == 999:
        print('\n')
        break

    entradas += 1
    soma += n

print(f'Tentativas: {entradas}')
print(f'Soma das tentativas: {soma}')


