dist = float(input('Digite a distância da viagem em KM: '))

if dist<=200:
    preço = 0.5*dist
    print(f'Preço da passagem: R${preço}')
else:
    preço = 0.45*dist
    print(f'Preço da passagem: R${preço}')