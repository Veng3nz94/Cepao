import requests

#primeira parte do código
#busca um endereço a partir de um CEP
def buscar_cep(cep):
    """Busca o endereço a partir de um CEP."""
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if response.status_code == 200:
        endereco = response.json()
        if "erro" in endereco:
            print("CEP não encontrado.")
        else:
            print("\n--- Endereço Encontrado ---")
            print(f"Logradouro: {endereco['logradouro']}")
            print(f"Bairro: {endereco['bairro']}")
            print(f"Cidade: {endereco['localidade']}")
            print(f"Estado: {endereco['uf']}")
            print(f"CEP: {endereco['cep']}")
    else:
        print("Erro ao buscar CEP.")

#segunda parte do código
#busca um CEP a partir de um endereço aproximado
def buscar_cep_por_endereco(logradouro, cidade, uf):
    """Busca CEPs a partir de um endereço aproximado."""
    url = f"https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        ceps = response.json()
        if ceps:
            print("\n--- CEPs Encontrados ---")
            for cep in ceps:
                print(f"CEP: {cep['cep']}")
                print(f"Logradouro: {cep['logradouro']}")
                print(f"Bairro: {cep['bairro']}")
                print("---")
        else:
            print("Nenhum CEP encontrado para este endereço.")
    else:
        print("Erro ao buscar endereço.")

#Parte principal do MENU
def menu():
    """Exibe o menu e gerencia a escolha do usuário."""
    print("\n--- CEP Finder ---")
    print("1) Buscar endereço por CEP")
    print("2) Buscar CEP por endereço")
    print("0) Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def main():
    while True:
        escolha = menu()
        if escolha == "1":
            cep = input("\nDigite o CEP (apenas números): ")
            buscar_cep(cep)
        elif escolha == "2":
            print("\nDigite o endereço aproximado:")
            logradouro = input("Logradouro (ex: Rua das Flores): ")
            cidade = input("Cidade (ex: São Paulo): ")
            uf = input("Estado (ex: SP): ")
            buscar_cep_por_endereco(logradouro, cidade, uf)
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
