import random
print('=' * 154)
il = '|{}|'.format('-*-' * 7)
print('\033[96m{:^154}'.format(il))
print('\033[1:97m{:^154}'.format('| LISTA DE APRESENTAÇÃO |'))
print('\033[0:96m{:^154}\033[97m\n'.format(il))
n1 = str(input('{:>78}'.format('Primeiro aluna(o): ')).strip().title())
n2 = str(input('{:>78}'.format('Segundo aluna(o): ')).strip().title())
n3 = str(input('{:>78}'.format('Terceiro aluna(o): ')).strip().title())
n4 = str(input('{:>78}'.format('Quarto aluna(o): ')).strip().title())
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('\n\033[97m{:^154}'.format('|{}|'.format('-*-' * 13)))
print('{:^154}'.format('A ordem de apresentação será:'))
resultado = '{:>77}    \033[96m{}\033[97m'
print(resultado.format('Primeira(o)    |', lista[0]))
print(resultado.format('Segunda(o)    |', lista[1]))
print(resultado.format('Terceira(o)    |', lista[2]))
print(resultado.format('Quarta(o)    |', lista[3]))
print('\033[97m{:^154}'.format('|{}|'.format('-*-' * 13)))
