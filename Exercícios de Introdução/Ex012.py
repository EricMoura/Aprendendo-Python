valor = float(input('Qual o valor do produto? '))
desc = float(input('Qual a porcentagem do desconto a ser aplicado? '))

newv = valor*(1-desc/100)

print(f'Valor do produto com desconto de {desc}%: R$ {newv:.2f}')