# Importa o módulo 'os' para comandos do sistema operacional (limpeza de tela)
import os

# Lista dedicada para a Fila de Atendimento (FIFO - Primeiro a Entrar, Primeiro a Sair)
# Armazena dicionários: {"nome": str, "cpf": str}
fila_atendimento = []

def limpar_tela():
    """
    Limpa o console para manter o menu organizado.
    """
    # Limpa o console: 'cls' no Windows, 'clear' em Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def simular_fila_atendimento():
    """
    Simula a chegada de pacientes na fila e o atendimento (saída FIFO).
    A chegada permite inserir múltiplos pacientes até que o usuário digite '0'.
    O atendimento remove apenas o primeiro da fila.
    """
    global fila_atendimento
    
    limpar_tela()
    print("--- SIMULAÇÃO: CHEGADA E ATENDIMENTO NA FILA (FIFO) ---")
    
    # 1. Chegada: Inserir pacientes na fila (Chegada)
    print("\n1. CHEGADA (ENTRADA DE PACIENTES NA FILA - Triagem Rápida):")
    print("   (Digite '0' no Nome para parar a chegada)")
    i = 1
    
    while True:
        print(f"\nPaciente {i}:")
        
        # Pede Nome
        nome_fila = input("Nome (0 para parar): ")
        if nome_fila == '0':
            print("\nChegada de pacientes na fila finalizada.")
            break
        
        # Pede CPF
        cpf_fila = input("CPF: ")
        
        # Adiciona o paciente ao FINAL da fila (Chegada)
        fila_atendimento.append({"nome": nome_fila, "cpf": cpf_fila})
        
        print(f"-> {nome_fila} (CPF: {cpf_fila}) adicionado ao final da FILA.")
        i += 1
        
    print("\n2. FILA ATUAL (Antes do Atendimento):")
    if fila_atendimento:
        for p in fila_atendimento:
            print(f"- {p['nome']} (CPF: {p['cpf']})")
    else:
        print("A fila está vazia.")

    # 3. Atendimento: Remover o primeiro paciente para serviço (Saída FIFO)
    print("\n3. ATENDIMENTO (Removendo o primeiro paciente da fila):")
    if fila_atendimento:
        # O método .pop(0) remove e retorna o PRIMEIRO elemento (FIFO)
        atendido = fila_atendimento.pop(0)
        print(f"*** PACIENTE ATENDIDO: {atendido['nome']} (CPF: {atendido['cpf']}) ***")
    else:
        print("A fila está vazia, ninguém para atender.")

    # 4. Mostrar quem ainda está na fila
    print("\n4. PACIENTES RESTANTES NA FILA:")
    if fila_atendimento:
        for i, p in enumerate(fila_atendimento, 1):
            print(f"{i}. {p['nome']} (CPF: {p['cpf']})")
    else:
        print("A fila está vazia.")

    input("\nFim da simulação. Pressione ENTER para sair...")


# Executa a simulação ao iniciar o programa
simular_fila_atendimento()
