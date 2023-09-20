# Mensagem de boas-vindas
print("Bem Vindo à Loja do Marilio Cesar Freitas Santos Vieira")

# Entrada do valor unitário e quantidade de produtos
valor_unitario = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

# Cálculo do valor total sem desconto
valor_total_sem_desconto = valor_unitario * quantidade

# Cálculo do desconto com base na quantidade
if quantidade < 200:
    desconto = 0
elif quantidade < 1000:
    desconto = 5
elif quantidade < 2000:
    desconto = 10
else:
    desconto = 15

# Cálculo do valor total com desconto
valor_total_com_desconto = valor_total_sem_desconto * (1 - desconto / 100)

# Saída 
print(f"Valor total sem desconto: R${valor_total_sem_desconto:.2f}")
print(f"Desconto aplicado: {desconto}%")
print(f"Valor total com desconto: R${valor_total_com_desconto:.2f}")
