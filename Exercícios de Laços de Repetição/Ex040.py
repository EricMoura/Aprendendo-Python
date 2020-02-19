x=0
while (x==0):
    n1 = float(input('Digite a primeira nota: '))
    if n1 < 0 or n1 > 10:
        print('Valor inválido')
    else:
        x=1
while (x==1):
    n2 = float(input('Digite a segunda nota: '))
    if n2 < 0 or n2 > 10:
        print('Valor inválido')
    else:
        x=2

md = (n1+n2)/2


if md < 5 and md >= 0:
    print(f'Reprovado! Média {md}')
elif md >= 5 and md < 7:
    print(f'Recuperação! Média {md}')
elif md >=7 and md<=10:
    print(f'Aprovado! Média {md}')