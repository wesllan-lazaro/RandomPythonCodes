import random
a = str(input('digite o nome do primeiro aluno: '))
b = str(input('digite o nome do segundo aluno: '))
c = str(input('do terceiro: '))
d = str(input('e do quarto: '))
lista = [a, b, c, d]
random.shuffle(lista)
print(f'a ordem da apresentação será  {lista}')