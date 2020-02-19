from datetime import date
now = date.today().year
ano = int(input('Digite o ano de nascimento: '))

dif = now-ano
if dif < 100:
    if dif < 9:
        print(f' {dif} anos: Categoria Mirim')
    elif dif < 14:
        print(f' {dif} anos: Categoria Infantil')
    elif dif < 19:
        print(f' {dif} anos: Categoria Junior')
    elif dif < 20:
        print(f' {dif} anos: Categoria Sênior')
    else:
        print(f' {dif} anos: Categoria Master')
else:
    print('Ano Inválido')