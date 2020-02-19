num = int(input('Digite um número de 0 a 9999: '))
if num >=0 and num <=9999:
    print(f'Milhar:{num // 1000 % 10} Centena:{num // 100 % 10} Dezena:{num //10 % 10} Unidade:{num // 1 % 10}')
