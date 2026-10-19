from statistics import median

listadenotas = []

for i in range(5):
    listadenotas.append(int(input(f"Nota {i + 1}: ")))
print("Notas: ", listadenotas)
media = sum(listadenotas) / len(listadenotas)
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