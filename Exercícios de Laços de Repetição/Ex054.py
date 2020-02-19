from datetime import date

maior = 0
menor = 0
for x in range (7):
    nasc = int(input(f'Digite o ano de nascimento da {x+1}° pessoa: '))
    hj = date.today().year

    if hj-nasc>18:
        maior +=1
    else:
        menor +=1

print(f'Maiores de idade: {maior}')
print(f'Menores de idade: {menor}')
