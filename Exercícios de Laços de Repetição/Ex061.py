print(' '*5,'Progressão Aritmética',' '*5)
pa = int(input('Insira o termo inicial: '))
const = int(input('Qual a razão de progressão?: '))
range = int(input('Tamanho da progressão: '))

while range>0:
    print(pa, end=' → ')
    pa +=const
    range -=1
print('FIM')