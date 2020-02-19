import time
import emoji
print('Contagem Regressiva')

for x in range(10, -1, -1):
    time.sleep(1)
    print(x)
print(emoji.emojize(':tada:'*5, use_aliases=True))
