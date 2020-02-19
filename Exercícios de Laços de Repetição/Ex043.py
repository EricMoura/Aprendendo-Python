import os

print('Cálculo IMC')
peso = float(input('Qual seu peso?: '))
altura = float(input('Qual sua altura?: '))

imc = peso/altura**2

print('Seu IMC é: %.4f' % imc )

if imc < 18.5:
	print("Abaixo do Peso")
elif imc < 25:
	print("Peso Ideal")
elif imc < 30:
	print("Sobrepeso")
elif imc < 40:
	print("Obesidade")
else:
	print("Obesidade Mórbida")

os.system("pause")