dias = int(input('Por quantos dias ele foi alugado? '))
km = float(input('Qual a distância percorrida (KM)? '))

valor = (60*dias)+(0.15*km)

print(f'Valor a pagar: R$ {valor:.2f}')