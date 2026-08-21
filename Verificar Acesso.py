import sqlite3

DB_PATH = "clinica.db"


# Conecta ao banco de dados
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# Regra simples para checar se o paciente tem prioridade (por exemplo, 60 anos ou mais)
def verificar_prioridade(idade):
    return idade >= 60


# Consulta pacientes e exibe estatísticas e permissão de acesso prioritário
def relatorio_acessos():
    conn = get_conn()
    pacientes = conn.execute("SELECT * FROM pacientes").fetchall()
    conn.close()

    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    # Cálculos estatísticos simples
    idades = [p["idade"] for p in pacientes]
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])
    media = sum(idades) / len(idades)

    print("--- Estatísticas Gerais ---")
    print(f"Total: {len(pacientes)}")
    print(f"Média de idade: {media:.1f}")
    print(f"Mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")

    print("\n--- Verificação de Prioridade ---")
    for p in pacientes:
        prioridade = "Sim (Prioritário)" if verificar_prioridade(p["idade"]) else "Não (Comum)"
        print(f"Paciente: {p['nome']} | Idade: {p['idade']} | Acesso prioritário: {prioridade}")


if __name__ == "__main__":
    relatorio_acessos()
