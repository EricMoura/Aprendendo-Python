x=0
while (x==0):
    valor = float(input('Insira o valor do produto: '))
    if valor>=0:
        x=1
    else:
        print('Valor Inválido')

while(x==1):
    metodo = int(input('Método a pagar (1-à vista, 2-parcelado): '))
    if metodo==1 or metodo==2:
        if metodo==1:
            f = int(input('1-Dinheiro/Cheque  2-Cartão:    '))
            y=0
            while (y==0):
                if f==1:
                    desconto = valor*0.9
                    print(f'Valor final com desconto: R$ {desconto}')
                    x=2
                    y=1
                elif f==2:
                    desconto = valor*0.95
                    print(f'Valor final com desconto: R$ {desconto}')
                    x=2
                    y=1
                else:
                    print('Opção não existe!')
        elif metodo==2:
            f = int(input('Somente cartão => 1-Parcelar em 2x,  2-Parcelar em 3x ou mais:  '))
            y=0
            while (y==0):
                if f==1:
                    print(f'Valor final parcelado em 2x: R$ {valor}')
                    y=1
                    x=2
                elif f==2:
                    desconto = valor*1.2
                    print(f'Valor final parcelado em 3x ou mais: R$ {desconto}')
                    y=1
                    x=2
                else:
                    print('Opção não existe!')





