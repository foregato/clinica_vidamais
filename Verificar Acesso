def obter_booleano(pergunta):
    # ... (função auxiliar para entrada S/N) ...
    # É usada para obter os valores A, B, C e D do usuário.

def verificar_acesso():
    """
    Implementa o sistema de controle de acesso lógico.
    Verifica se o paciente pode ser atendido nas modalidades Consulta Normal e Emergência.
    """
    print("--- VERIFICAÇÃO DE ACESSO (LÓGICA PROPOSICIONAL) ---")
    
    print("\nPor favor, informe o status das seguintes condições:")
    
    # Coleta dos valores booleanos (A, B, C, D)
    A = obter_booleano("A: O paciente tem agendamento marcado?")
    B = obter_booleano("B: Os documentos estão em dia (RG/CPF válidos)?")
    C = obter_booleano("C: Há médico disponível no horário?")
    D = obter_booleano("D: Os pagamentos anteriores estão em dia?")
    
    print("\n--- RESULTADOS DA VERIFICAÇÃO ---")
    
    # Cálculo da Regra para CONSULTA NORMAL
    acesso_normal = (A and B and C) or (B and C and D)
    print(f"1. Acesso para Consulta Normal: {'LIBERADO (V)' if acesso_normal else 'NEGADO (F)'}")
    
    # Cálculo da Regra para EMERGÊNCIA
    acesso_emergencia = C and (B or D)
    print(f"2. Acesso para Emergência: {'LIBERADO (V)' if acesso_emergencia else 'NEGADO (F)'}")

    # Simulação da Situação Prática (Tarefa 5: A=F, B=V, C=V, D=F)
    if not A and B and C and not D:
        print("\n(Situação prática do exercício: Consulta Normal: F, Emergência: V)")
        
    input("\nPressione ENTER para voltar ao menu...")


# A função é chamada pela opção '6' no loop principal:
# ...
# elif opcao == '6':
#     verificar_acesso()
# ...
