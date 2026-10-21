n = int(input("Inserir Número: "))

primo = True
divisores = 0

for i in range(2, n):
    if n % i == 0:
        primo = False

for i in range(1, n + 1):
    if n % i == 0:
        divisores += 1

print(divisores)
if primo:
    print(f"O número {n} é primo.")
else:
    print(f"O número {n} não é primo.")