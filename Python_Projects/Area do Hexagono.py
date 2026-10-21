from math import sqrt

a = 3 * sqrt(3)
c = a / 2

l = float(input("Inserir o valor do lado do hexagono: "))
l = l ** 2
final = round(c * l, 2)

print("resultado: ", final)