num = int(input('Digite um número inteiro: '))
base = int(input('Qual a base da conversão?(1-Binário, 2-Octal, 3-Hexadecimal): '))

if base > 3 or base <=0:
    print('Você informou um valor incorreto')
elif base == 1:
    print(f'O valor {num} convertido para Binário é:', bin(num))
elif base == 2:
    print(f'O valor {num} convertido para Octal é: ', oct(num))
else:
    print(f'O valor {num} convertido para Hexadecimal é: ', hex(num))



