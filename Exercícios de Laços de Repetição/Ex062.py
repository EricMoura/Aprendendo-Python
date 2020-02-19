print(' '*5,'Progressão Aritmética',' '*5)
pa = int(input('Insira o termo inicial: '))
const = int(input('Qual a razão de progressão?: '))
range = int(input('Tamanho da progressão: '))

while range>0:
    print(pa, end=' ')
    pa +=const
    range -=1
    x = 0
    if range == 0:
        while x==0:
            r = str(input('\nVocê quer mostrar mais alguns termos?[S/N]: ')).upper()
            if r!= 'S' and r!= 'N':
                print('Resposta inválida')
                x=1
            elif r == 'S':
                qtd = int(input('Quantos?:'))
                if qtd == 0:
                    range = -1
                    x = -1
                range = qtd
                x=1
            elif r == 'N':
                range = -1
                x=-1
print('FIM')