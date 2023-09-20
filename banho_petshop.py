# Função para obter o peso do cachorro
def cachorro_peso():
    while True:
        try:
            peso = float(input("Digite o peso do cachorro em kg: "))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
                continue
            elif peso < 3:
                return 40
            elif peso < 10:
                return 50
            elif peso < 30:
                return 60
            elif peso < 50:
                return 70
            else:
                print("Desculpe, só atendemos cachorros com peso de até 50 kg. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um valor numérico válido para o peso.")

# Função para obter o tipo de pelo do cachorro
def cachorro_pelo():
    while True:
        pelo = input("Digite o tipo de pelo do cachorro (c/m/l para curto/médio/longo): ").lower()
        if pelo in ['c', 'm', 'l']:
            if pelo == 'c':
                return 1
            elif pelo == 'm':
                return 1.5
            else:
                return 2
        else:
            print("Opção de pelo inválida. Digite 'c', 'm' ou 'l'.")

# Função para obter serviços adicionais e calcular o valor extra
def cachorro_extra():
    valor_extra = 0
    while True:
        try:
            adicional = int(input("Escolha o serviço adicional (1 - Cortar unhas, 2 - Escovar dentes, 3 - Limpar orelhas, 0 - Não querer mais nada): "))
            if adicional == 0:
                return valor_extra
            elif adicional in [1, 2, 3]:
                if adicional == 1:
                    valor_extra += 10
                elif adicional == 2:
                    valor_extra += 12
                else:
                    valor_extra += 15
            else:
                print("Opção de serviço adicional inválida. Escolha entre 1, 2, 3 ou 0.")
        except ValueError:
            print("Entrada inválida. Digite um número válido para o serviço adicional.")

# Mensagem de boas-vindas
print("Boas Vindas ao Pet Shop do Marilio César Freitas Santos Vieira")

# Obter informações do cachorro
try:
    peso = cachorro_peso()
    pelo = cachorro_pelo()
    extras = cachorro_extra()
    
    # Cálculo do total a pagar
    total = (peso * pelo) + extras
    print(f"Total a pagar: R${total:.2f}")
except ValueError:
    print("Valor não numérico inserido para o peso do cachorro.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
