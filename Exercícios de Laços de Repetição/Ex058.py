import random
print('Vou pensar em um número entre 0 e 10... Tente adivinhar!!')
rnum = random.randint(0,10)
acertou = False
palpite = 0

while not acertou:
    n = int(input('Dê seu palpite: '))
    if n == rnum:
        acertou = True
    palpite +=1

print(f'Você venceu com {palpite} palpite(s)')