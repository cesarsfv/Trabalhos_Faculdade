# Função para cadastrar um colaborador
def cadastrar_colaborador(id):
    nome = input("Digite o nome do colaborador: ")
    setor = input("Digite o setor do colaborador: ")
    salario = float(input("Digite o salário do colaborador: "))
    colaborador = {"id": id, "nome": nome, "setor": setor, "salario": salario}
    lista_colaboradores.append(colaborador)
    print("Colaborador cadastrado com sucesso!")

# Função para consultar colaboradores
def consultar_colaborador():
    opcao = int(input("Escolha uma opção:\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Setor\n4. Retornar ao menu\nOpção: "))
    
    if opcao == 1:
        for colaborador in lista_colaboradores:
            print("ID:", colaborador["id"])
            print("Nome:", colaborador["nome"])
            print("Setor:", colaborador["setor"])
            print("Salário:", colaborador["salario"])
            print("--------------------------")
    elif opcao == 2:
        id_consulta = int(input("Digite o ID do colaborador: "))
        for colaborador in lista_colaboradores:
            if colaborador["id"] == id_consulta:
                print("ID:", colaborador["id"])
                print("Nome:", colaborador["nome"])
                print("Setor:", colaborador["setor"])
                print("Salário:", colaborador["salario"])
                print("--------------------------")
                return
        print("Colaborador não encontrado.")
    elif opcao == 3:
        setor_consulta = input("Digite o setor: ")
        for colaborador in lista_colaboradores:
            if colaborador["setor"] == setor_consulta:
                print("ID:", colaborador["id"])
                print("Nome:", colaborador["nome"])
                print("Setor:", colaborador["setor"])
                print("Salário:", colaborador["salario"])
                print("--------------------------")
    elif opcao == 4:
        return
    else:
        print("Opção inválida!")

# Função para remover um colaborador
def remover_colaborador():
    id_remover = int(input("Digite o ID do colaborador a ser removido: "))
    for colaborador in lista_colaboradores:
        if colaborador["id"] == id_remover:
            lista_colaboradores.remove(colaborador)
            print("Colaborador removido com sucesso!")
            return
    print("Colaborador não encontrado.")

# Variáveis globais
lista_colaboradores = []
id_global = 1

# Menu principal
while True:
    print("Software de Marilio César Freitas Santos Vieira")
    print("1. Cadastrar Colaborador")
    print("2. Consultar Colaborador")
    print("3. Remover Colaborador")
    print("4. Encerrar Programa")
    opcao_menu = int(input("Escolha uma opção: "))
    
    if opcao_menu == 1:
        cadastrar_colaborador(id_global)
        id_global += 1
    elif opcao_menu == 2:
        consultar_colaborador()
    elif opcao_menu == 3:
        remover_colaborador()
    elif opcao_menu == 4:
        break
    else:
        print("Opção inválida!")

# Exemplos de entrada de dados para preencher a saída de console
cadastrar_colaborador(1)
cadastrar_colaborador(2)
cadastrar_colaborador(3)

print("\nConsulta de todos os colaboradores:")
consultar_colaborador()

print("\nConsulta por código (ID) de colaborador:")
consultar_colaborador()

print("\nConsulta por setor:")
consultar_colaborador()

print("\nRemoção de um colaborador:")
remover_colaborador()
