maior = 0
menor = 0
for x in range (5):
    peso = int(input(f'Digite o peso da {x+1}° pessoa: '))

    if peso<0:
        print('Peso Inválido')
        x -= 1
    elif peso>maior:
        maior = peso
        if menor == 0:
            menor = peso
    elif peso<menor:
        menor=peso


print(f'Maior peso: {maior}')
print(f'Menor peso: {menor}')