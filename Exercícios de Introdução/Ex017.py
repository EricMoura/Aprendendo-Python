import math
catop = float(input('Digite o cateto oposto: '))
catadj = float(input('Digite o cateto adjacente: '))

hip = math.sqrt(pow(catop,2)+pow(catadj,2))

print(f'Valor da hipotenusa: {hip}')