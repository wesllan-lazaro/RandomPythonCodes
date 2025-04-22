import random 
a = input("escreva o nome do primeiro aluno: ")
b = input("do segundo: ")
c = input("terceiro: ")
d = input("E por ultimo o quarto: ")
list = [a, b, c, d]
e = print(f"o sorteado foi {random.choice(list)}")