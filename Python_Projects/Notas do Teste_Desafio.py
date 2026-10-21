listadenotas = []

for i in range(5):
    entrada = int(input(f"Nota {i + 1}: "))
    while not 0 <= entrada <= 20:
        print("Nota inválida")
        entrada = int(input(f"Nota {i + 1}: "))
    listadenotas.append(entrada)



print("Notas: ", listadenotas)

soma = 0
for nota in listadenotas:
    soma += nota

media = soma / len(listadenotas)

print("Média: ", media)
print("Maior Nota: ", max(listadenotas))
print("Menor Nota: ", min(listadenotas))

notaspositivas = []
for nota in listadenotas:
    if nota >= 10:
        notaspositivas.append(nota)
print("Notas Positivas: ", len(notaspositivas))
listadenotas.sort()
print("Por ordem crescente", listadenotas)
print("Posição da maior nota na lista: ", listadenotas[-1])