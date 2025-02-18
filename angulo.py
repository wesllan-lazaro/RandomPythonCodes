import math
a = float(input('digite o ângulo que você deseja: '))
b = math.radians(a)
print(f'o angulo de {a} tem o seno de {math.sin(b):.2f}')
print(f'o angulo de {a} tem o conseno de {math.cos(b):.2f}')
print(f'o angulo de {a} tem o tangente de {math.tan(b):.2f}')