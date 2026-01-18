import os  # só pra limpar o terminal
from datetime import date

def ler_float(prompt):
    # le um float com validação e repete até entrada válida
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\nSomente números são permitidos")
            input("\nPressione Enter para continuar....")
            os.system('cls' if os.name == 'nt' else 'clear')

def ler_int(prompt):
    # le um inteiro com validação e repete até entrada válida
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\nSomente números inteiros são permitidos")
            input("\nPressione Enter para continuar....")
            os.system('cls' if os.name == 'nt' else 'clear')

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

def calculadora_gorjeta():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[Calculadora de Gorjeta]")
    valor_conta = ler_float("\nDigite o valor total da conta: R$ ")
    
    if valor_conta <= 0:
        print("\nO valor da conta deve ser maior que zero.")
        input("\nPressione Enter para voltar ao menu....")
        return
    
    porcentagem = ler_float("Digite a porcentagem de gorjeta desejada (ex: 10 para 10%): ")
    
    if porcentagem < 0:
        print("\nA porcentagem não pode ser negativa.")
        input("\nPressione Enter para voltar ao menu....")
        return
    
    gorjeta = calcular_gorjeta(valor_conta, porcentagem)
    total = valor_conta + gorjeta
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[Calculadora de Gorjeta]")
    print(f"\n--- Resumo ---")
    print(f"Valor da conta: R$ {valor_conta:.2f}")
    print(f"Porcentagem de gorjeta: {porcentagem:.1f}%")
    print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
    print(f"Total a pagar: R$ {total:.2f}")
    input("\nPressione Enter para voltar ao menu....")


def eh_palindromo(texto):
    # Remove espaços e pontuação, converte para minúsculas
    texto_limpo = ""
    for char in texto.lower():
        if char.isalnum():  # mantém apenas letras e números
            texto_limpo += char
    
    # Compara o texto com sua versão invertida
    return texto_limpo == texto_limpo[::-1]

def verificador_palindromo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[Verificador de Palíndromo]")
    texto = input("\nDigite uma palavra ou frase: ")
    
    if not texto.strip():
        print("\nVocê precisa digitar algo.")
        input("\nPressione Enter para voltar ao menu....")
        return
    
    resultado = eh_palindromo(texto)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[Verificador de Palíndromo]")
    print(f"\nTexto digitado: \"{texto}\"")
    
    if resultado:
        print("\nÉ um palíndromo? Sim")
    else:
        print("\nÉ um palíndromo? Não")
    
    input("\nPressione Enter para voltar ao menu....")


def calcular_desconto(preco_original, porcentagem_desconto):
    return preco_original * (porcentagem_desconto / 100)

def calculadora_desconto():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[Calculadora de Desconto]")
    preco_original = ler_float("\nDigite o preço original do produto: R$ ")
    
    if preco_original <= 0:
        print("\nO preço deve ser maior que zero.")
        input("\nPressione Enter para voltar ao menu....")
        return
    
    porcentagem = ler_float("Digite a porcentagem de desconto (ex: 15 para 15%): ")
    
    if porcentagem < 0 or porcentagem > 100:
        print("\nA porcentagem deve estar entre 0 e 100.")
        input("\nPressione Enter para voltar ao menu....")
        return
    
    # Cálculo de desconto
    valor_desconto = calcular_desconto(preco_original, porcentagem)
    
    # Preço final
    preco_final = preco_original - valor_desconto
    
    # Formatação: Arredonda para 2 casas decimais
    valor_desconto = round(valor_desconto, 2)
    preco_final = round(preco_final, 2)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[Calculadora de Desconto]")
    print(f"\n--- Resultado ---")
    print(f"Preço original: R$ {preco_original:.2f}")
    print(f"Desconto: {porcentagem:.1f}% (R$ {valor_desconto:.2f})")
    print(f"Preço final: R$ {preco_final:.2f}")
    input("\nPressione Enter para voltar ao menu....")


def calculadora_dias_vivo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[Calculadora de Dias Vivos]")
    print("\nDigite sua data de nascimento:")
    
    dia = ler_int("Dia: ")
    mes = ler_int("Mês: ")
    ano = ler_int("Ano: ")
    
    try:
        data_nascimento = date(ano, mes, dia)
        data_atual = date.today()
        
        if data_nascimento > data_atual:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Calculadora de Dias Vivos]")
            print("\nA data de nascimento não pode ser no futuro!")
            input("\nPressione Enter para voltar ao menu....")
            return
        
        diferenca = data_atual - data_nascimento
        dias_vivos = diferenca.days
        
        # Cálculo adicional para contexto
        anos = dias_vivos // 365
        meses_aprox = (dias_vivos % 365) // 30
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[Calculadora de Dias Vivos]")
        print(f"\n--- Resultado ---")
        print(f"Data de nascimento: {data_nascimento.strftime('%d/%m/%Y')}")
        print(f"Data atual: {data_atual.strftime('%d/%m/%Y')}")
        print(f"\nVocê está vivo há {dias_vivos} dias!")
        print(f"(Aproximadamente {anos} anos e {meses_aprox} meses)")
        
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[Calculadora de Dias Vivos]")
        print("\nData inválida! Verifique os valores digitados.")
    
    input("\nPressione Enter para voltar ao menu....")


# mapa de opções do menu para funções
ferramentas = {
    1: calculadora_gorjeta,
    2: verificador_palindromo,
    3: calculadora_desconto,
    4: calculadora_dias_vivo
}

def menu():
    # loop principal do menu
    opcao_escolhida = None
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- Utilitários ---")
        print("Bem vindo ao Menu Principal")
        print("[1] Calculadora de Gorjeta")
        print("[2] Verificador de Palíndromo")
        print("[3] Calculadora de Desconto")
        print("[4] Calculadora de Dias Vivos")
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