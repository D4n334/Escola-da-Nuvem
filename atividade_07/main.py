import csv
import json
import os


def limpa_tela():
    comando = "cls" if os.name == "nt" else "clear"
    try:
        os.system(comando)
    except Exception:
        print("\n" * 100)


def _normalizar_nome_arquivo(nome: str, extensao: str) -> str:
    nome = (nome or "").strip().strip('"').strip("'")
    if not nome:
        return f"dados{extensao}"
    if not nome.lower().endswith(extensao):
        nome += extensao
    return nome


def _pausar():
    try:
        input("\nPressione ENTER para voltar ao menu...")
    except KeyboardInterrupt:
        pass


def cadastro_clientes():
    limpa_tela()
    print("[Cadastro de Clientes - Gravar CSV]\n")
    pessoas = [
        ["Ana", 23, "São Paulo"],
        ["Bruno", 31, "Rio de Janeiro"],
        ["Carla", 27, "Belo Horizonte"],
    ]

    nome_arquivo = _normalizar_nome_arquivo(
        input("Digite o nome do arquivo CSV para salvar (ex: clientes.csv): "),
        ".csv",
    )

    try:
        with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["nome", "idade", "cidade"])
            for pessoa in pessoas:
                escritor.writerow(pessoa)

        print(f"\nDados gravados com sucesso em: {nome_arquivo}")
    except PermissionError:
        print("\nErro: permissão negada para escrever o arquivo.")
    except OSError as exc:
        print(f"\nErro ao escrever o arquivo: {exc}")

    _pausar()


def ler_clientes():
    limpa_tela()
    print("[Listar Clientes - Ler CSV]\n")
    nome_arquivo = _normalizar_nome_arquivo(
        input("Digite o nome do arquivo CSV para ler (ex: clientes.csv): "),
        ".csv",
    )

    try:
        with open(nome_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                print(linha)

        print(f"\nLeitura concluída: {nome_arquivo}")
    except FileNotFoundError:
        print("\nErro: arquivo não encontrado.")
    except PermissionError:
        print("\nErro: permissão negada para ler o arquivo.")
    except (OSError, csv.Error) as exc:
        print(f"\nErro ao ler o arquivo: {exc}")

    _pausar()


def dicionario_json():
    limpa_tela()
    print("[Criar Payload - JSON]\n")
    pessoa = [{
        "nome": "Diego",
        "idade": 29,
        "cidade": "Curitiba",
    },
    {
        "nome": "Talvanes",
        "idade": 29,
        "cidade": "Maceió",
    },
    {   "nome": "Jussara",
        "idade": 29,
        "cidade": "Rio de Janeiro",
    }
    ]

    nome_arquivo = _normalizar_nome_arquivo(
        input("Digite o nome do arquivo JSON (ex: pessoa.json): "),
        ".json",
    )

    try:
        with open(nome_arquivo, mode="w", encoding="utf-8") as arquivo:
            json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)
        print(f"\nJSON salvo com sucesso em: {nome_arquivo}")

        with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        print("\nConteúdo lido do JSON:")
        print(dados)
    except FileNotFoundError:
        print("\nErro: arquivo não encontrado.")
    except PermissionError:
        print("\nErro: permissão negada para acessar o arquivo.")
    except json.JSONDecodeError:
        print("\nErro: o arquivo JSON está inválido/corrompido.")
    except OSError as exc:
        print(f"\nErro de arquivo: {exc}")

    _pausar()

opcoes = {
    1:cadastro_clientes,
    2:ler_clientes,
    3: dicionario_json
}



def menu():
    opcao_escolhida = 0
    while True:
        limpa_tela()
        print("[Menu Principal]")
        print("[1] - Cadastro de Clientes ")
        print("[2] - Listar Clientes")
        print("[3] - Criar Payload de Clientes")
        print("[0] - Sair")
        print("-------------------------------")

        try:
            opcao_escolhida = int(input("Escolha uma opção: ").strip())
        except KeyboardInterrupt:
            print("\n\nSaindo...")
            break
        except ValueError:
            print("\nOpção inválida (digite um número).")
            _pausar()
            continue

        if opcao_escolhida == 0:
            print("\nSaindo...")
            break

        funcao = opcoes.get(opcao_escolhida)
        if not funcao:
            print("\nOpção inexistente.")
            _pausar()
            continue

        funcao()


if __name__ == "__main__":
    menu()


