def obter_booleano(pergunta):
    """
    Função auxiliar para obter um valor booleano (True/False) a partir de
    uma entrada de usuário 'S' (Sim) ou 'N' (Não).
    """
    while True:
        resposta = input(f"{pergunta} (S/N): ").strip().upper()
        if resposta == 'S':
            return True
        elif resposta == 'N':
            return False
        else:
            print("Resposta inválida. Por favor, digite 'S' para Sim ou 'N' para Não.")


def verificar_acesso():
    """
    Implementa o sistema de controle de acesso lógico.
    Verifica se o paciente pode ser atendido nas modalidades Consulta Normal e Emergência.
    """
    print("--- VERIFICAÇÃO DE ACESSO (LÓGICA PROPOSICIONAL) ---")

    print("\nPor favor, informe o status das seguintes condições:")

    # Variáveis Lógicas (Convertidas para True/False)
    A = obter_booleano("A: O paciente tem agendamento marcado?")
    B = obter_booleano("B: Os documentos estão em dia (RG/CPF válidos)?")
    C = obter_booleano("C: Há médico disponível no horário?")
    D = obter_booleano("D: Os pagamentos anteriores estão em dia?")

    print("\n--- RESULTADOS DA VERIFICAÇÃO ---")

    # 1. Regra para CONSULTA NORMAL: O paciente será atendido SE:
    # (Tem agendamento E documentos OK E médico disponível) OU
    # (Documentos OK E médico disponível E pagamentos em dia)
    # Expressão Lógica: R1 = (A ^ B ^ C) v (B ^ C ^ D)
    acesso_normal = (A and B and C) or (B and C and D)

    print(f"1. Acesso para Consulta Normal: {'LIBERADO (V)' if acesso_normal else 'NEGADO (F)'}")

    # 2. Regra para EMERGÊNCIA: O paciente será atendido SE:
    # (Há médico disponível) E (Tem documentos OU pagamentos em dia)
    # Expressão Lógica: R2 = C ^ (B v D)

    acesso_emergencia = C and (B or D)

    print(f"2. Acesso para Emergência: {'LIBERADO (V)' if acesso_emergencia else 'NEGADO (F)'}")

    # Exemplo do Passo 3, Tarefa 5: A=F, B=V, C=V, D=F
    if not A and B and C and not D:
        # Consulta Normal: (F ^ V ^ V) v (V ^ V ^ F) = F v F = F
        # Emergência: V ^ (V v F) = V ^ V = V
        print("\n(Situação prática do exercício: Consulta Normal: F, Emergência: V)")

    input("\nPressione ENTER para voltar ao menu...")


# Executa a verificação de acesso ao iniciar o programa
verificar_acesso()
