import os  # só pra limpar o terminal

def classifica_idade():
    idade = 0
    while True:    
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("--- Classificador de Idade ---")
            idade = int(input("Digite sua idade para começarmos: "))
            if idade < 0:
                print("Você mentiu :(")
                input("\nPressione qualquer tecla para continuar....")
                continue
            elif 0 <= idade <= 12:
                print("Você é uma Criança :3")
            elif 13 <= idade <= 17:
                print("Você é um Adolescente >:)")
            elif 18 <= idade <= 59:
                print("Você já é um adulto :(")
            elif 60 <= idade:
                print("Você já é um(a) idoso(a)")
            input("\nPressione qualquer tecla para continuar....")
            break
        except ValueError:
            print("\nSomente números são permitidos")
            input("\nPressione qualquer tecla para continuar....")
            break


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

def calculadora_imc():
    peso = 0
    altura = 0
    os.system('cls' if os.name == "nt" else 'clear')
    print("[Calculadora IMC]")
    peso = ler_float('Por favor informe o seu peso em quilogramas(Kg): ')
    altura = ler_float("\nPor favor informe sua altura em metros(Ex: 1.80): ")
    imc =  peso / (altura * altura)
    if imc < 18.5:
        resultado = " abaixo do seu peso ideal, consulte um nutricionista"
    elif imc < 25:
        resultado = "no seu peso ideal"
    elif imc < 30:
        resultado = "Sobrepeso, consulte um nutricionista"
    else: 
        resultado = "obeso, consulte um nutricionista "

    os.system('cls' if os.name == 'nt' else 'clear')
    print("[Calculadora IMC]")
    print(f"O seu índice de Massa Corporal é de: {imc:.2f}")
    print(f"De acordo com a tabela padrão de IMC você está {resultado}")
    input("\nPressione qualquer tecla para continuar....")


            

def conversor_temperatura():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[Conversor de Temperatura]")
        print("[1] Celsius -> Fahrenheit")
        print("[2] Celsius -> Kelvin")
        print("[3] Fahrenheit -> Celsius")
        print("[4] Fahrenheit -> Kelvin")
        print("[5] Kelvin -> Celsius")
        print("[6] Kelvin -> Fahrenheit")
        print("[0] Voltar ao Menu")

        try:
            opcao = int(input("\nEscolha uma opção:"))
        except ValueError:
            print("\nOpção Inválida.")
            input("\nPressione Enter para continuar...")
            continue

        if opcao == 0:
            return
        
        if opcao == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Conversor de Temperatura]\n")
            celsius = ler_float("Digite a temperatura emm °C: ")
            resultado = (celsius * 1.8) +32
            print(f"\n{celsius:.2f} °C = {resultado:.2f} °F")

        elif opcao == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Conversor de Temperatura]\n")
            celsius = ler_float("Digite a temperatura em °C: ")
            if celsius < -273.15:
                print("\nValor inválido: abaixo do zero absoluto (-273,15 °C).")
            else:
                resultado = celsius + 273.15
                print(f"\n{celsius:.2f} °C = {resultado:.2f} K")

        elif opcao == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Conversor de Temperatura]\n")
            fahrenheit = ler_float("Digite a temperatura em °F: ")
            resultado = (fahrenheit - 32) * (5/9)
            print(f"\n{fahrenheit:.2f} °F = {resultado:.2f} °C")

        elif opcao == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Conversor de Temperatura]\n")
            fahrenheit = ler_float("Digite a temperatura em °F: ")
            if fahrenheit < -459.67:
                print("\nValor inválido: abaixo do zero absoluto (-459,67 °F).")
            else:
                resultado = (fahrenheit - 32) * (5/9) + 273.15
                print(f"\n{fahrenheit:.2f} °F = {resultado:.2f} K")

        elif opcao == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Conversor de Temperatura]\n")
            kelvin = ler_float("Digite a temperatura em °K: ")
            if kelvin < 0:
                print("\nValor inválido: Kelvin não pode ser negativo.")
            else:
                resultado = kelvin - 273.15
                print(f"\n{kelvin:.2f} K = {resultado:.2f} °C")

        elif opcao == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Conversor de Temperatura]\n")
            kelvin = ler_float("Digite a temperatura em °K: ")
            if kelvin < 0:
                print("\nValor inválido: Kelvin não pode ser negativo.")
            else:
                resultado = (kelvin - 273.15) * 1.8 + 32
                print(f"\n{kelvin:.2f} K = {resultado:.2f} °F")
        else:
            print("\nOpção Inválida")

        input("\nPressione Enter para continuar....")


def calculadora_ano_bissexto():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            print("[Ano Bissexto?]")
            ano = int(input("Digite o ano para descobrir se ele é bissexto ou não: "))
        except ValueError:
            print("\nOpção inválida, por favor selecione uma Opção do menu\n\n")
            input("\nPressione Enter para continuar....")
            continue
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400  == 0:
            print(f"\nO Ano {ano} é bissexto!!!")
        else:
            print("\nNão é >:(")

        input("\nPressione Enter para continuar....")
        break

# mapa de opções do menu para funções
ferramentas = {
    1: classifica_idade,
    2: calculadora_imc,
    3: conversor_temperatura,
    4: calculadora_ano_bissexto
}

def menu():
    # loop principal do menu
    opcao_escolhida = None
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- Utilitários ---")
        print("Bem vindo ao  Menu Principal")
        print("[1] Classificador de Idade")    
        print("[2] Calculadora de IMC")
        print("[3] Conversor de Temperatura")
        print("[4] Verificador de Ano Bissexto")
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