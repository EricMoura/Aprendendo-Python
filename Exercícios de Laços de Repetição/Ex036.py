vcasa = float(input('Qual o valor da casa?: '))
salario = float(input('Qual o salário do comprador?: '))
anos = float(input('Em quantos anos ele vai pagar?: '))

vprestacao = vcasa/(anos*12)
csalario = salario*0.3

print(f'Valor da prestação {vprestacao}.')

if vprestacao > csalario:
    print('Empréstimo negado!')
else:
    print('Empréstimo autorizado!')