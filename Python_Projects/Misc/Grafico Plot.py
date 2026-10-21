from matplotlib import pyplot

categorias = []
valores = []

while True:
    try:
        categoriasqty = int(input("Inserir o número de categorias desejadas: "))
        if categoriasqty > 0:
            break
        else:
            print("Inserir número maior que 0.")
            continue
    except ValueError:
        print("Inserir apenas um número inteiro!")


for i in range(categoriasqty):
    current = str(input(f"Insere a {i + 1}ª categoria: "))
    categorias.append(current)

for categoria in categorias:
    while True:
        try:
            valor = float(input(f"""Insere o valor da categoria "{categoria}": """))
            if valor > 0:
                valores.append(valor)
                break
            else:
                print("Inserir valor maior que 0.")
                continue
        except ValueError:
            print("Inserir apenas um valor inteiro!")

tipodegrafico = int(input(
    "Escolhe o tipo de gráfico de barras:\n"
    "1 - Frequência absoluta\n"
    "2 - Fequência Relativa\n"
))

match tipodegrafico:
    case 1:
        pyplot.bar(categorias, valores, color = "blue")
        pyplot.xlabel("Categorias")
        pyplot.ylabel("Valores")
        pyplot.title("Frequência Absoluta")
    case 2:
        novosvalores = []
        for valor in valores:
            novosvalores.append(valor / sum(valores) * 100)
        pyplot.bar(categorias, novosvalores, color="blue")
        pyplot.xlabel("Categorias")
        pyplot.ylabel("Valores (%)")
        pyplot.title("Frequência Relativa")
    case _:
        print("Opção Inválida!")



pyplot.show()