import os  # só pra limpar o terminal

def conversor_moedas():
    # limpa a tela e inicia
    os.system('cls' if os.name == 'nt' else 'clear')
    dolar = 5.37
    euro = 6.25
    valor_real = ler_float(
        "[Conversor de Moedas]\n\n"
        "Digite o valor em reais: R$"
        )
    dolar = dolar * valor_real
    euro = euro * valor_real
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[Conversor de Moedas]\n")
    print(f"--- Valores Convertidos---\nReal: R$ {valor_real:.2f}\nDólar: $ {dolar:.2f}\nEuro:  £ {euro:.2f}")
    input("\nPressione Enter para voltar ao menu....")
    os.system('cls' if os.name == 'nt' else 'clear')


def ler_float(prompt):
    # le um float com validação e repete até entrada válida
    while True:
        try:
            return float(input(prompt))  # retorna assim que for válido
        except ValueError:
            # Mensagem de erro e pausa para tentar novamente
            print("\nSomente números são permitidos")
            input("\nPressione qualquer tecla para continuar....")
            os.system('cls' if os.name == 'nt' else 'clear')

def calculadora_media_escolar():
    notas = []
    sair = False
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            print("[Calculadora de Média Escolar]")
            nota = float(input("Digite a nota do aluno: "))
            notas.append(nota)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Somente números são permitidos")
            input("Pressione Enter para continuar...")
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Calculadora de Média Escolar]")
            continuar = input("\nDeseja adicionar mais notas? [s/n]:  ")
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
                print("[Calculadora de Média Escolar]")
                print("Opção Inválida, selecione s ou n")
                input("Pressione Enter para continuar...")
                continue
        if sair == True:
            media = sum(notas) / len(notas)
            media = round(media, 2)
            # 7.5 + 8.0 + 6.5 = 7,333333
            print(f"A média do aluno é de {media}")
            input("\nPressione Enter para voltar ao menu....")
            break
            

def calculadora_desconto():
    quantidade = 0  # quantidade de itens no carrinho
    nome_produto = "Camiseta"
    camisa = 50.00  # preço unitário
    sair = False  # controla quando finalizar a compra
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Loja 20% OFF]")
            print(" 1 - Camisa R$50.00")
            produto = int(input("Escolha qual produto deseja comprar com um desconto especial: "))
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
            print("[[Loja 20% OFF]]")
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
                print("[[Loja 20% OFF]]")
                print("Opção Inválida, selecione s ou n")
                input("Pressione Enter para continuar...")
                continue
        if sair == True:
            # resumo da compra com total e pausa antes de voltar ao menu
            total = camisa * quantidade
            desconto = total * 0.8
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Loja 20% OFF]")
            print(f"\nVocê colocou no carrinho {quantidade} {nome_produto}(s)\n"
                  f"\nPreço Unitário: R${camisa:.2f}\nO total da sua compra é R${total:.2f}\n"
                  f"Preço com desconto: R${desconto:.2f}")
            input("\nPressione Enter para voltar ao menu....")
            break

def calculadora_consumo_combustivel():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[Estimativa de Consumo]")
    autonomia = float(input("Qual a distância percorrida(em Km)? "))
    distancia = float(input("Quantos litros de gasolina foram gastos? "))
    os.system('cls' if os.name == 'nt' else 'clear')
    media = autonomia / distancia
    print(f"A média de consumo do veículo foi de : {media:.2f} Km/l")
    input("\nPressione Enter para voltar ao menu....")

# mapa de opções do menu para funções
ferramentas = {
    1: conversor_moedas,
    2: calculadora_desconto,
    3: calculadora_media_escolar,
    4: calculadora_consumo_combustivel
}

def menu():
    # loop principal do menu
    opcao_escolhida = None
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- Utilitários ---")
        print("Bem vindo ao  Menu Principal")
        print("[1] Conversor de Moedas")    
        print("[2] Calculadora de Desconto")
        print("[3] Calculadora de Média Escolar")
        print("[4] Calculadora de Consumo de Combustível")
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
