vel = int(input('Digite a velocidade do carro: '))

if vel>80:
    multa = (vel-80)*7
    print(f'Você foi multado em R${multa}')
    print('Respeite os limites de velocidade')
else:
    print('Tenha um bom dia!')