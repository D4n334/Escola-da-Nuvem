import os  # só pra limpar o terminal

def ler_float(prompt):
    # le um float com validação e repete até entrada válida
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\nSomente números são permitidos")
            input("\nPressione Enter para continuar....")
            os.system('cls' if os.name == 'nt' else 'clear')

def calculadora_basica():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("[Calculadora Básica]")
        print("[1] Soma (+)")
        print("[2] Subtração (-)")
        print("[3] Multiplicação (*)")
        print("[4] Divisão (/)")
        print("[0] Voltar ao Menu")

        try:
            opcao = int(input("\nEscolha uma operação: "))
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida.")
            input("\nPressione Enter para continuar...")
            continue

        if opcao == 0:
            return

        if opcao not in [1, 2, 3, 4]:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida, selecione uma operação válida.")
            input("\nPressione Enter para continuar...")
            continue

        os.system('cls' if os.name == 'nt' else 'clear')
        print("[Calculadora Básica]\n")
        num1 = ler_float("Digite o primeiro número: ")
        num2 = ler_float("Digite o segundo número: ")

        operador = ""
        resultado = 0
        
        if opcao == 1:
            resultado = num1 + num2
            operador = "+"
        elif opcao == 2:
            resultado = num1 - num2
            operador = "-"
        elif opcao == 3:
            resultado = num1 * num2
            operador = "*"
        elif opcao == 4:
            if num2 == 0:
                print("\nErro: Divisão por zero não é permitida!")
                input("\nPressione Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            resultado = num1 / num2
            operador = "/"

        os.system('cls' if os.name == 'nt' else 'clear')
        print("[Calculadora Básica]")
        print(f"\nResultado: {num1} {operador} {num2} = {resultado:.2f}")
        input("\nPressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')


def registro_notas_alunos():
    notas = []
    sair = False
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            print("[Registro de Notas - Média da Turma]")
            nota = float(input("Digite a nota do aluno: "))
            if nota < 0 or nota > 10:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("A nota deve estar entre 0 e 10.")
                input("Pressione Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            notas.append(nota)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Somente números são permitidos")
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Registro de Notas - Média da Turma]")
            print(f"\nNotas registradas: {len(notas)}")
            continuar = input("\nDeseja adicionar mais notas? [s/n]: ")
            if continuar.strip().lower() == 's':
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            elif continuar.strip().lower() == 'n':
                sair = True
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("[Registro de Notas - Média da Turma]")
                print("Opção Inválida, selecione s ou n")
                input("Pressione Enter para continuar...")
                continue

        if sair:
            media = sum(notas) / len(notas)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Registro de Notas - Média da Turma]")
            print(f"\nTotal de alunos: {len(notas)}")
            print(f"Notas: {notas}")
            print(f"Média da turma: {media:.2f}")
            input("\nPressione Enter para voltar ao menu....")
            break


def verificador_senha():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("[Verificador de Senha]")
        senha = input("Digite uma senha para verificar: ")

        erros = []

        # Critério a: pelo menos 8 caracteres
        if len(senha) < 8:
            erros.append("- A senha deve ter pelo menos 8 caracteres.")

        # Critério b: pelo menos um número
        tem_numero = False
        for char in senha:
            if char.isdigit():
                tem_numero = True
                break
        if not tem_numero:
            erros.append("- A senha deve conter pelo menos um número.")

        os.system('cls' if os.name == 'nt' else 'clear')
        print("[Verificador de Senha]")
        if erros:
            print("\nA senha NÃO atende aos critérios de segurança:")
            for erro in erros:
                print(erro)
        else:
            print("\nA senha atende aos critérios de segurança! ✓")

        input("\nPressione Enter para voltar ao menu....")
        break


def analisador_pares_impares():
    numeros = []
    pares = 0
    impares = 0
    sair = False
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        try:
            print("[Analisador de Números Pares e Ímpares]")
            numero = int(input("Digite um número inteiro: "))
            numeros.append(numero)

            if numero % 2 == 0:
                pares += 1
                tipo = "PAR"
            else:
                impares += 1
                tipo = "ÍMPAR"

            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Analisador de Números Pares e Ímpares]")
            print(f"\nO número {numero} é {tipo}!")

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Somente números inteiros são permitidos")
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        while True:
            continuar = input("\nDeseja analisar mais números? [s/n]: ")
            if continuar.strip().lower() == 's':
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            elif continuar.strip().lower() == 'n':
                sair = True
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("[Analisador de Números Pares e Ímpares]")
                print("Opção Inválida, selecione s ou n")
                continue

        if sair:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Analisador de Números Pares e Ímpares]")
            print(f"\n--- Resumo ---")
            print(f"Total de números analisados: {len(numeros)}")
            print(f"Números pares: {pares}")
            print(f"Números ímpares: {impares}")
            input("\nPressione Enter para voltar ao menu....")
            break


# mapa de opções do menu para funções
ferramentas = {
    1: calculadora_basica,
    2: registro_notas_alunos,
    3: verificador_senha,
    4: analisador_pares_impares
}

def menu():
    # loop principal do menu
    opcao_escolhida = None
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- Utilitários ---")
        print("Bem vindo ao Menu Principal")
        print("[1] Calculadora Básica (+, -, *, /)")
        print("[2] Registro de Notas (Média da Turma)")
        print("[3] Verificador de Senha")
        print("[4] Analisador de Pares e Ímpares")
        print("[0] Sair")
        try:
            opcao_escolhida = int(input("Escolha uma opção: "))
        except ValueError:
            print("\nOpção inválida, por favor selecione uma Opção do menu\n\n")
            continue

        if opcao_escolhida == 0:
            break

        func = ferramentas.get(opcao_escolhida)
        if func:
            func()
        else:
            print("Opção inválida, por favor selecione uma Opção do menu")
            continue

# inicialização
menu()