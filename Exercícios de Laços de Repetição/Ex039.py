from datetime import date
atual = date.today().year

data = int(input('Informe seu ano de nascimento: '))

x = atual-data

if x == 18:
    print('Você tem que se alistar!')
elif x < 18:
    print('Você ainda vai se alistar!')
    quantidade_anos = 18 - x
    print(f'Faltam {quantidade_anos} anos')
else:
    print('Já passou o tempo de se alistar!')
    quantidade_anos = x - 18
    print(f'Passou {quantidade_anos} anos')


