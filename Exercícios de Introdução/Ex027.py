nome = input('Digite seu nome: ')

lista = nome.strip().split()

print(f'Seu primeiro nome: {lista[0]}')
print(f'Seu último nome: {lista[len(lista)-1]}')