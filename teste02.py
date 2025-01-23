a = input("digite alguma coisa: ")
print("você digitou um(a): ", type(a))
if ' ' in a:
    print("tem espaço!")
else: 
    print('não tem espaço!')
if a in a.__str__:
    print('tem letras alfabeticas!')
else:
    print('não tem letras alfabeticas')