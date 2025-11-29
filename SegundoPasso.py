# Importa o módulo 'os' para comandos do sistema operacional (limpeza de tela)
import os

# Lista principal para armazenar os dados de cada paciente (dicionários)
# Cada dicionário armazena: {"nome": str, "idade": int, "telefone": str}
pacientes = []

def limpar_tela():
    """
    Limpa o console para manter o menu organizado.
    """
    # Limpa o console: 'cls' no Windows, 'clear' em Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_paciente():
    """
    Permite o cadastro de um novo paciente (nome, idade, telefone),
    incluindo tratamento de erro para a entrada da idade.
    """
    limpar_tela()
    print("--- NOVO CADASTRO COMPLETO ---")
    
    # 1. Solicita Nome
    nome = input("Nome do paciente: ")
    
    # 2. Tratamento de erro para Idade (deve ser número inteiro, entre 0 e 120)
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0:
                print("Erro: A idade não pode ser negativa.")
            elif idade > 120:
                print("Erro: A idade máxima permitida é 120 anos. Por favor, verifique.")
            else:
                break
        except ValueError:
            print("Erro: Digite um número inteiro válido para a idade.")
            
    # 3. Solicita Telefone
    telefone = input("Telefone: ")
    
    # Adiciona o dicionário do paciente à lista principal
    paciente = {"nome": nome, "idade": idade, "telefone": telefone}
    pacientes.append(paciente)
    print("\nPaciente cadastrado com sucesso!")
    input("Pressione ENTER para voltar ao menu...")

def ver_estatisticas():
    """
    Exibe estatísticas: total de pacientes, idade média, mais novo e mais velho.
    """
    limpar_tela()
    print("--- ESTATÍSTICAS DO SISTEMA ---")
    total = len(pacientes)
    
    if total == 0:
        print("Nenhum paciente cadastrado ainda.")
        input("\nPressione ENTER para voltar ao menu...")
        return

    # A lista 'pacientes_com_idade' já deve conter apenas inteiros válidos,
    # mas filtramos para garantir robustez.
    pacientes_com_idade = [p for p in pacientes if isinstance(p.get("idade"), int)]
    
    print(f"Total de pacientes cadastrados: {total}")
    
    if pacientes_com_idade:
        # 1. Idade Média
        soma_idades = sum(p["idade"] for p in pacientes_com_idade)
        media_idade = soma_idades / len(pacientes_com_idade)
        
        # 2. Paciente mais novo e mais velho
        mais_novo = min(pacientes_com_idade, key=lambda p: p["idade"])
        mais_velho = max(pacientes_com_idade, key=lambda p: p["idade"])
        
        print(f"Idade média: {media_idade:.1f} anos")
        print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
        print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")
    else:
        print("Não há dados de idade válidos para calcular estatísticas.")
        
    input("\nPressione ENTER para voltar ao menu...")

def buscar_paciente():
    """
    Busca um paciente pelo nome (busca parcial, não sensível a maiúsculas/minúsculas).
    """
    limpar_tela()
    print("--- BUSCAR PACIENTE ---")
    # Converte o termo de busca para minúsculas
    nome_busca = input("Digite o nome ou parte do nome para buscar: ").lower()
    encontrado = False
    
    print("\nRESULTADOS:")
    # Itera sobre a lista verificando se o termo de busca está no nome do paciente
    for p in pacientes:
        if nome_busca in p["nome"].lower():
            # Exibe os dados do paciente encontrado
            print(f"  > Nome: {p['nome']} | Idade: {p.get('idade', 'N/A')} | Tel: {p.get('telefone', 'N/A')}")
            encontrado = True
    
    if not encontrado:
        print("Paciente não encontrado.")
        
    input("\nPressione ENTER para voltar ao menu...")

def listar_todos():
    """
    Lista todos os pacientes cadastrados de forma organizada.
    """
    limpar_tela()
    print("--- LISTA DE PACIENTES CADASTRADOS ---")
    if not pacientes:
        print("A lista está vazia.")
    else:
        # Itera sobre a lista exibindo a numeração
        for i, p in enumerate(pacientes, 1):
            # Formatação de exibição
            idade_info = f"{p.get('idade', 'N/A')} anos" if isinstance(p.get('idade'), int) else p.get('idade', 'N/A')
            telefone_info = p.get('telefone', 'N/A')
            
            print(f"{i}. Nome: {p['nome']} | Idade: {idade_info} | Tel: {telefone_info}")

    input("\nPressione ENTER para voltar ao menu...")

# Loop Principal do Menu
while True:
    limpar_tela()
    print("\n=== SISTEMA CLÍNICA VIDA+ ===")
    print("1. Cadastrar paciente (Nome, Idade, Telefone)") 
    print("2. Exibir estatísticas")
    print("3. Buscar paciente pelo nome")
    print("4. Listar todos os cadastrados")
    print("5. Sair do sistema")                                   
    
    opcao = input("\nEscolha uma opção: ")
    
    # Direciona para a função correspondente
    if opcao == '1':
        cadastrar_paciente()
    elif opcao == '2':
        ver_estatisticas()
    elif opcao == '3':
        buscar_paciente()
    elif opcao == '4':
        listar_todos()
    elif opcao == '5':
        print("Encerrando sistema...")
        break
    else:
        # Tratamento de erro para opção inválida
        print("\n--- ERRO: Opção inválida! Escolha um número de 1 a 5. ---")
        input("Pressione ENTER para continuar...")