print(' '*5,'Tabuada',' '*5)
num = int(input('Digite um número: '))
tam = int(input('Qual o tamanho da tabuada?: '))

for x in range(tam+1):
    print(num,'x',x,'=',x*num)