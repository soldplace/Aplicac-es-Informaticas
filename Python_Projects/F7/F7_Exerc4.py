def media(a, b, c):
    if 0 <= a <= 20 and 0 <= b <= 20 and 0 <= c <= 20:
        return (a + b + c) / 3
    else:
        return -1

A = float(input("Inserir valor de A: "))
B = float(input("Inserir valor de B: "))
C = float(input("Inserir valor de C: "))

print(media(A, B, C))