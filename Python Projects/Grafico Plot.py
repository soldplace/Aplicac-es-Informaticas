from matplotlib import pyplot

categorias = []
valores = []



categoriasqty = int(input("Inserir o número de categorias desejadas: "))

for i in range(categoriasqty):
    categorias.append(str(input(f"Insere a {i + 1}ª categoria: ")))

for categoria in categorias:
    valores.append(int(input(f"""Insere o valor da categoria "{categoria}": """)))
print(categorias, valores)

tipodegrafico = int(input(
    "Escolhe o tipo de gráfico de barras:\n"
    "1 - Frequência absoluta\n"
    "2 - Fequência Relativa\n"
))

titulo = str(input("Inserir o titulo do gráfico: "))

match tipodegrafico:
    case 1:
        pyplot.bar(categorias, valores, color = "blue")
    case 2:
        novosvalores = []
        for valor in valores:
            novosvalores.append(categoriasqty / valor * 10)
        pyplot.bar(categorias, novosvalores, color="blue")

pyplot.xlabel("Categorias")
pyplot.ylabel("Valores")
pyplot.title(titulo)
pyplot.show()