import os  # só pra limpar o terminal

def calculadora_soma():
    # limpa a tela e inicia
    os.system('cls' if os.name == 'nt' else 'clear')
    numeros = []  # lista para armazenar os números digitados
    sair = False  # flag para controlar a saída da calculadora
    while True:
        try:
            #  leitura do número
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Calculadora de Soma]")
            valor = int(input("\nDigite um número: "))
            numeros.append(valor)  # adiciona o número válido à lista
        except ValueError:
            # trata entrada não numérica e volta ao início do loop
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Calculadora de Soma]")
            print("\nSomente números são permitidos")
            input("\nPressione Enter para continuar....")
            continue

        # loop interno apenas para validar a resposta 's/n'
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Calculadora de Soma]")
            continuar = input("\nDeseja adicionar mais um número? [s/n]:  ")
            if continuar.strip().lower() == 's':
                # 's' -> volta ao loop externo para pedir outro número
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            elif continuar.strip().lower() == 'n':
               # 'n' -> sinaliza saída e encerra a calculadora
               sair = True
               break
            else:
                # qualquer outra resposta -> avisa e repete a pergunta
                os.system('cls' if os.name == 'nt' else 'clear')
                print("[Calculadora de Soma]")
                print("Opção Inválida, selecione s ou n")
                continue
        if sair == True:
            # resultado final e pausa antes de voltar ao menu
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Calculadora de Soma]")
            print("\nA soma dos números é : ", sum(numeros))
            input("\nPressione Enter para voltar ao menu....")
            break

def ler_float(prompt):
    # le um float com validação e repete até entrada válida
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Calculadora de Volume]")
            return float(input(prompt))  # retorna assim que for válido
        except ValueError:
            # Mensagem de erro e pausa para tentar novamente
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Calculadora de Volume]")
            print("\nSomente números são permitidos")
            input("\nPressione qualquer tecla para continuar....")

def calculadora_volume():
    print("[Calculadora de Volume]")
    comprimento = ler_float("Digite o comprimento da Caixa: ")
    largura = ler_float("Digite a Largura da Caixa: ")
    altura = ler_float("Digite a Altura da Caixa: ")

    os.system('cls' if os.name == 'nt' else 'clear')
    volume = comprimento * largura * altura  # cálculo do volume

    print("[Calculadora de Volume]")
    print(f"\nO Volume da Caixa é de {volume:.2f} cm³")
    input("\nPressione Enter para voltar ao menu....")

def calculadora_preco_total():
    quantidade = 0  # quantidade de itens no carrinho
    nome_produto = "Cadeira Infantil"
    cadeira = 12.40  # preço unitário
    sair = False  # controla quando finalizar a compra
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Calculadora de Preço Total]")
            print(" 1 - Cadeira Infantil R$12.40")
            produto = int(input("Escolha qual produto deseja comprar: "))
            if produto != 1:
                # só um produto
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Só temos um produto em estoque, por favor o selecione :)")
                input("Pressione Enter para continuar...")
                continue
            else:
                quantidade += 1
        except ValueError:
            # validação de entrada
            print("Somente números são permitidos")
            input("Pressione Enter para continuar...")
            continue

        # loop interno para decidir adicionar mais ou finalizar
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Calculadora de Preço Total]")
            continuar = input("\nDeseja adicionar mais produtos? [s/n]:  ")
            if continuar.strip().lower() == 's':
                # 's' -> volta ao loop externo e escolhe produto novamente
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            elif continuar.strip().lower() == 'n':
               # 'n' -> sinaliza finalização da compra
               sair = True
               break
            else:
                # resposta inválida -> instrui e repete a pergunta
                os.system('cls' if os.name == 'nt' else 'clear')
                print("[Calculadora de Preço Total]")
                print("Opção Inválida, selecione s ou n")
                input("Pressione Enter para continuar...")
                continue
        if sair == True:
            # resumo da compra com total e pausa antes de voltar ao menu
            total = cadeira * quantidade
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Calculadora de Preço Total]")
            print(f"\nVocê colocou no carrinho {quantidade} {nome_produto}\nPreço Unitário: R${cadeira:.2f}\nO total da sua compra é R${total:.2f}")
            input("\nPressione Enter para voltar ao menu....")
            break

# mapa de opções do menu para funções
ferramentas = {
    1: calculadora_soma,
    2: calculadora_volume,
    3: calculadora_preco_total
}

def menu():
    # loop principal do menu
    opcao_escolhida = None
    while True:
        print("\n--- Olá Mundo ---")
        print("Bem vindo ao  Menu Principal")
        print("[1] Calculadora de Soma")    
        print("[2] Calculadora de Volume")
        print("[3] Calculadora de Preço Total")
        print("[0] Sair")
        try:
            # converte a entrada para inteiro
            opcao_escolhida = int(input("Escolha uma opção: "))
        except ValueError:
            print("\nOpção inválida, por favor selecione uma Opção do menu\n\n")
            continue

        if opcao_escolhida == 0:
            # mata o programa
            break

        # recupera a função pelo dicionário (emula um switch) e executa se existir
        func = ferramentas.get(opcao_escolhida)
        if func:
            func()
        else:
            print("Opção inválida, por favor selecione uma Opção do menu")
            continue

# inicialização
menu()
