import random

num = int(input('Vou pensar em um número entre 0 e 5... Tente adivinhar: '))

rnum = random.randint(0,5)

print(f'Você venceu' if num==rnum else f'Você perdeu, eu pensei no número {rnum}')


