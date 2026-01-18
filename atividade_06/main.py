import os  # só pra limpar o terminal
import random
import string
import requests

def ler_int(prompt):
    # le um inteiro com validação e repete até entrada válida
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\nSomente números inteiros são permitidos")
            input("\nPressione Enter para continuar....")
            os.system('cls' if os.name == 'nt' else 'clear')


def gerador_senha():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[Gerador de Senhas Seguras]")
    
    tamanho = ler_int("\nDigite o tamanho da senha desejada: ")
    
    if tamanho < 4:
        print("\nA senha deve ter pelo menos 4 caracteres para ser segura.")
        input("\nPressione Enter para voltar ao menu....")
        return
    
    if tamanho > 100:
        print("\nO tamanho máximo permitido é 100 caracteres.")
        input("\nPressione Enter para voltar ao menu....")
        return
    
    # caracteres disponíveis
    letras_minusculas = string.ascii_lowercase  # a-z
    letras_maiusculas = string.ascii_uppercase  # A-Z
    numeros = string.digits  # 0-9
    simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Combina todos os caracteres
    todos_caracteres = letras_minusculas + letras_maiusculas + numeros + simbolos
    
    # Garante pelo menos um de cada tipo
    senha = [
        random.choice(letras_minusculas),
        random.choice(letras_maiusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]
    
    # Preenche o restante da senha
    for _ in range(tamanho - 4):
        senha.append(random.choice(todos_caracteres))
    
    # Embaralhar a senha
    random.shuffle(senha)
    
    # Converte lista para string
    senha_final = ''.join(senha)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[Gerador de Senhas Seguras]")
    print(f"\n--- Senha Gerada ---")
    print(f"Tamanho: {tamanho} caracteres")
    print(f"\nSua senha: {senha_final}")
    input("\nPressione Enter para voltar ao menu....")


def buscar_usuario_aleatorio():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[Gerador de Usuário Aleatório]")
    print("\nBuscando usuário fictício...")
    
    try:
        # Acessa a API Random User Generator
        response = requests.get("https://randomuser.me/api/", timeout=10)
        
        if response.status_code == 200:
            dados = response.json()
            usuario = dados['results'][0]
            
            # Extrai informações do usuário
            nome = f"{usuario['name']['first']} {usuario['name']['last']}"
            email = usuario['email']
            pais = usuario['location']['country']
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Gerador de Usuário Aleatório]")
            print(f"\n--- Usuário Encontrado ---")
            print(f"Nome: {nome}")
            print(f"E-mail: {email}")
            print(f"País: {pais}")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Gerador de Usuário Aleatório]")
            print(f"\nFalha ao buscar usuário. Código de erro: {response.status_code}")
    
    except requests.exceptions.ConnectionError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[Gerador de Usuário Aleatório]")
        print("\nFalha na conexão. Verifique sua internet e tente novamente.")
    except requests.exceptions.Timeout:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[Gerador de Usuário Aleatório]")
        print("\nTempo limite excedido. Tente novamente mais tarde.")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[Gerador de Usuário Aleatório]")
        print(f"\nErro inesperado: {e}")
    
    input("\nPressione Enter para voltar ao menu....")


def consultar_cep():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[Consulta de CEP]")
    
    cep = input("\nDigite o CEP (somente números): ").strip()
    
    # Remove caracteres não numéricos
    cep = ''.join(filter(str.isdigit, cep))
    
    if len(cep) != 8:
        print("\nCEP inválido. O CEP deve conter 8 dígitos.")
        input("\nPressione Enter para voltar ao menu....")
        return
    
    print("\nConsultando CEP...")
    
    try:
        # Acessa a API ViaCEP
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=10)
        
        if response.status_code == 200:
            dados = response.json()
            
            # Verifica se o CEP existe
            if "erro" in dados:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("[Consulta de CEP]")
                print(f"\nCEP {cep} não encontrado.")
            else:
                logradouro = dados.get('logradouro', 'Não informado')
                bairro = dados.get('bairro', 'Não informado')
                cidade = dados.get('localidade', 'Não informado')
                estado = dados.get('uf', 'Não informado')
                
                os.system('cls' if os.name == 'nt' else 'clear')
                print("[Consulta de CEP]")
                print(f"\n--- Informações do CEP {cep[:5]}-{cep[5:]} ---")
                print(f"Logradouro: {logradouro}")
                print(f"Bairro: {bairro}")
                print(f"Cidade: {cidade}")
                print(f"Estado: {estado}")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Consulta de CEP]")
            print(f"\nFalha na requisição. Código de erro: {response.status_code}")
    
    except requests.exceptions.ConnectionError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[Consulta de CEP]")
        print("\nFalha na conexão. Verifique sua internet e tente novamente.")
    except requests.exceptions.Timeout:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[Consulta de CEP]")
        print("\nTempo limite excedido. Tente novamente mais tarde.")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[Consulta de CEP]")
        print(f"\nErro inesperado: {e}")
    
    input("\nPressione Enter para voltar ao menu....")


def consultar_cotacao():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[Cotação de Moedas]")
    print("\nEscolha uma moeda:")
    print("[1] USD - Dólar Americano")
    print("[2] EUR - Euro")
    print("[3] GBP - Libra Esterlina")
    print("[4] ARS - Peso Argentino")
    print("[5] CAD - Dólar Canadense")
    print("[6] JPY - Iene Japonês")
    print("[7] BTC - Bitcoin")
    print("[0] Voltar ao Menu")
    
    # Mapa de opções para códigos de moeda
    moedas = {
        1: "USD",
        2: "EUR",
        3: "GBP",
        4: "ARS",
        5: "CAD",
        6: "JPY",
        7: "BTC"
    }
    
    try:
        opcao = int(input("\nDigite o número da moeda: "))
    except ValueError:
        print("\nOpção inválida.")
        input("\nPressione Enter para voltar ao menu....")
        return
    
    if opcao == 0:
        return
    
    if opcao not in moedas:
        print("\nOpção inválida, selecione uma moeda da lista.")
        input("\nPressione Enter para voltar ao menu....")
        return
    
    moeda = moedas[opcao]
    
    print("\nConsultando cotação...")
    
    try:
        # Acessa a API AwesomeAPI
        response = requests.get(f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL", timeout=10)
        
        if response.status_code == 200:
            dados = response.json()
            
            # A chave é a combinação da moeda com BRL
            chave = f"{moeda}BRL"
            
            if chave in dados:
                cotacao = dados[chave]
                
                nome = cotacao.get('name', 'Não informado')
                valor_atual = float(cotacao.get('bid', 0))
                maxima = float(cotacao.get('high', 0))
                minima = float(cotacao.get('low', 0))
                data_hora = cotacao.get('create_date', 'Não informado')
                
                os.system('cls' if os.name == 'nt' else 'clear')
                print("[Cotação de Moedas]")
                print(f"\n--- {nome} ---")
                print(f"Valor atual: R$ {valor_atual:.4f}")
                print(f"Máxima do dia: R$ {maxima:.4f}")
                print(f"Mínima do dia: R$ {minima:.4f}")
                print(f"Última atualização: {data_hora}")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("[Cotação de Moedas]")
                print(f"\nMoeda '{moeda}' não encontrada ou não disponível.")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Cotação de Moedas]")
            print(f"\nMoeda '{moeda}' não encontrada ou erro na requisição.")
    
    except requests.exceptions.ConnectionError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[Cotação de Moedas]")
        print("\nFalha na conexão. Verifique sua internet e tente novamente.")
    except requests.exceptions.Timeout:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[Cotação de Moedas]")
        print("\nTempo limite excedido. Tente novamente mais tarde.")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[Cotação de Moedas]")
        print(f"\nErro inesperado: {e}")
    
    input("\nPressione Enter para voltar ao menu....")


# mapa de opções do menu para funções
ferramentas = {
    1: gerador_senha,
    2: buscar_usuario_aleatorio,
    3: consultar_cep,
    4: consultar_cotacao
}

def menu():
    # loop principal do menu
    opcao_escolhida = None
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- Utilitários com APIs ---")
        print("Bem vindo ao Menu Principal")
        print("[1] Gerador de Senhas Seguras")
        print("[2] Gerador de Usuário Aleatório")
        print("[3] Consulta de CEP")
        print("[4] Cotação de Moedas")
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