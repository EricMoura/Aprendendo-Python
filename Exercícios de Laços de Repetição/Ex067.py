print(' '*5,'Tabuada',' '*5)
x = 1

while True:
    num = int(input('Quer ver a tabuada de qual valor?: '))
    if num > 0:
        tam = int(input('Qual o tamanho da tabuada?: '))
        print('-'*20)
        while x <= tam:
            print(num, 'x', x, '=', x * num)
            x+=1
        print('-'*20)
    else:
        print('A tabuada foi encerrada')
        break