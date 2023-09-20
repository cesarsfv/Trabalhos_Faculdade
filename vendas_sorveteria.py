# Mensagem de boas-vindas
print("Bem Vindo à Sorveteria do Marilio César Freitas Vieira")

while True:
    # Entrada do sabor e quantidade de bolas de sorvete desejado
    sabor = input("Digite o sabor do sorvete (tr/pr/es): ")
    quantidade = int(input("Digite o número de bolas de sorvete (1/2/3): "))

    # Verificação de sabor de sorvete
    if sabor not in ["tr", "pr", "es"]:
        print("Sabor de Sorvete Inválido")
        continue

    # Verificação de quantidade de bolas de sorvete
    if quantidade not in [1, 2, 3]:
        print("Quantidade de Bolas de Sorvete Inválida")
        continue

    # Cálculo do preço com base no sabor e quantidade
    if sabor == "tr":
        if quantidade == 1:
            preco = 6
        elif quantidade == 2:
            preco = 11
        else:
            preco = 15
    elif sabor == "pr":
        if quantidade == 1:
            preco = 7
        elif quantidade == 2:
            preco = 13
        else:
            preco = 18
    else:
        if quantidade == 1:
            preco = 8
        elif quantidade == 2:
            preco = 15
        else:
            preco = 21

    # Saída de console com o valor total
    print(f"Valor total: R${preco:.2f}")

    # Perguntar se o cliente quer pedir mais alguma coisa
    resposta = input("Deseja pedir mais alguma coisa? (S/N): ")
    if resposta.upper() != "S":
        break
