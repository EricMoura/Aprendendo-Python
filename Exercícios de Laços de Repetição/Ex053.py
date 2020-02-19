frase = input('Digite uma frase: ').upper().replace(' ','')

x = len(frase)

if frase == frase[::-1]:
    print('A frase é palíndroma')
else:
    print('A frase não é palíndroma')
