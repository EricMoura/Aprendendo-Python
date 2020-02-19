sl = float(input('Digite o valor do salário: '))

if sl>1250:
    reajuste=sl*1.1
    print(f'Novo salário: R${reajuste:.2f}')
else:
    reajuste=sl*1.15
    print(f'Novo salário R${reajuste:.2f}')