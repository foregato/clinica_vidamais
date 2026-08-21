import sqlite3
from collections import deque

DB_PATH = "clinica.db"


# Conecta ao banco de dados
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# Carrega os pacientes do banco e simula a ordem de atendimento (fila)
def simular_fila():
    conn = get_conn()
    pacientes = conn.execute("SELECT * FROM pacientes").fetchall()
    conn.close()

    # Cria uma fila vazia (estrutura FIFO - primeiro que entra é o primeiro que sai)
    fila = deque()

    # Adiciona os pacientes na fila
    for p in pacientes:
        fila.append(dict(p))

    print(f"Total de pacientes na fila: {len(fila)}")

    # Simula o atendimento de cada um em ordem
    while fila:
        paciente_atual = fila.popleft()
        print(f"Atendendo agora: {paciente_atual['nome']} ({paciente_atual['idade']} anos)")

    print("Todos os pacientes foram atendidos.")


if __name__ == "__main__":
    simular_fila()
