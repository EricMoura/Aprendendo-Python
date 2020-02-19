salario = float(input('Qual o valor do salário? '))
reajuste = float(input('Qual a porcentagem do reajuste? '))

news = salario*(1+reajuste/100)

print(f'Novo salário: R$ {news:.2f}')