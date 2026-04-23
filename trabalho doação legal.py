doacoes = []
pessoas = []

def cadastrar_doacao():
    print("\n--- Cadastro de Doação ---")
    
    nome = input("Nome do doador: ")
    alimento = input("Alimento: ")
    try:
        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            print("Quantidade inválida!")
            return
    except:
        print("Digite um número válido!")
        return
    doacoes.append({
        "nome": nome,
        "alimento": alimento,
        "quantidade": quantidade
    })

    print("Doação cadastrada!")


def cadastrar_pessoa():
    print("\n--- Cadastro de Pessoa ---")
    
    nome = input("Nome: ")
    
    try:
        idade = int(input("Idade: "))
        familia = int(input("Tamanho da família: "))
        
        if idade < 0 or familia <= 0:
            print("Dados inválidos!")
            return
    except:
        print("Digite números válidos!")
        return

    prioridade = familia
    if idade >= 60:
        prioridade += 5

    pessoas.append({
        "nome": nome,
        "idade": idade,
        "familia": familia,
        "prioridade": prioridade
    })

    print("Pessoa cadastrada!")

def listar_doacoes():
    print("\n--- Doações ---")
    if not doacoes:
        print("Nenhuma doação.")
        return
    
    for i, d in enumerate(doacoes):
        print(f"{d['alimento']} ({d['quantidade']}) - {d['nome']}")

def listar_pessoas():
    print("\n--- Pessoas ---")
    if not pessoas:
        print("Nenhuma pessoa.")
        return
    
    for i, p in enumerate(pessoas):
        print(f"{p['nome']} | Idade: {p['idade']} | Família: {p['familia']} | Prioridade: {p['prioridade']}")

def remover_doacao():
    listar_doacoes()
    try:
        i = int(input("Digite o índice para remover: "))
        doacoes.pop(i)
        print("Doação removida!")
    except:
        print("Índice inválido!")

def remover_pessoa():
    listar_pessoas()
    try:
        i = int(input("Digite o índice para remover: "))
        pessoas.pop(i)
        print("Pessoa removida!")
    except:
        print("Índice inválido!")

def buscar_pessoa():
    nome = input("Digite o nome para buscar: ").lower()
    
    encontrado = False
    
    for p in pessoas:
        if nome in p["nome"].lower():
            print(f"{p['nome']} | Idade: {p['idade']} | Família: {p['familia']}")
            encontrado = True
    
    if not encontrado:
        print("Pessoa não encontrada!")

def relatorio():
    total_doacoes = len(doacoes)
    total_pessoas = len(pessoas)
    
    soma_alimentos = 0
    for d in doacoes:
        soma_alimentos += d["quantidade"]

    print("\n--- RELATÓRIO ---")
    print(f"Total de doações: {total_doacoes}")
    print(f"Total de pessoas: {total_pessoas}")
    print(f"Total de alimentos: {soma_alimentos}")

def distribuir():
    if not doacoes or not pessoas:
        print("Dados insuficientes!")
        return

    pessoas_ordenadas = sorted(pessoas, key=lambda x: x["prioridade"], reverse=True)

    print("\n--- Distribuição ---")

    for pessoa in pessoas_ordenadas:
        if not doacoes:
            print("Acabaram as doações!")
            break

        doacao = doacoes[0]

        if doacao["quantidade"] > 0:
            print(f"{pessoa['nome']} recebeu 1 unidade de {doacao['alimento']}")
            doacao["quantidade"] -= 1

        if doacao["quantidade"] == 0:
            doacoes.pop(0)

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar doação")
    print("2 - Cadastrar pessoa")
    print("3 - Listar doações")
    print("4 - Listar pessoas")
    print("5 - Remover doação")
    print("6 - Remover pessoa")
    print("7 - Buscar pessoa")
    print("8 - Relatório")
    print("9 - Distribuir")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        cadastrar_doacao()
    elif op == "2":
        cadastrar_pessoa()
    elif op == "3":
        listar_doacoes()
    elif op == "4":
        listar_pessoas()
    elif op == "5":
        remover_doacao()
    elif op == "6":
        remover_pessoa()
    elif op == "7":
        buscar_pessoa()
    elif op == "8":
        relatorio()
    elif op == "9":
        distribuir()
    elif op == "0":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")