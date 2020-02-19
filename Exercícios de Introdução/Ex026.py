from unicodedata import normalize

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

if __name__ == '__main__':
    from doctest import testmod
    testmod()

frase = input(('Digite uma frase: ')).lower().strip()
frase = remover_acentos(frase)
print('Quantidade de A: {}'.format(frase.count('a')))
print('Primeiro A na posição {}'.format(frase.find('a')+1))
print('Último A na posição {}'.format(frase.rfind('a')+1))