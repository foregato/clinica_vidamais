# Sistema de Gerenciamento de Clínica Médica

Este projeto consiste em um sistema completo de gerenciamento para clínicas médicas, desenvolvido em Python. O sistema oferece funcionalidades para cadastro de pacientes, controle de acesso, estatísticas e gerenciamento de fila de atendimento.

## 📋 Funcionalidades Principais

### 1. Sistema Principal da Clínica (`clinica.py`)

**Módulo central com as seguintes operações:**

- **Cadastro Completo de Pacientes**
  - Registro de nome, idade e telefone
  - Validação robusta de idade (0-120 anos)
  - Tratamento de erros na entrada de dados

- **Estatísticas Detalhadas**
  - Total de pacientes cadastrados
  - Cálculo de idade média
  - Identificação do paciente mais novo e mais velho

- **Sistema de Busca Inteligente**
  - Busca parcial por nome
  - Não sensível a maiúsculas/minúsculas
  - Ignora acentos nas buscas

- **Listagem Completa**
  - Exibição organizada de todos os pacientes
  - Numeração sequencial para fácil referência

### 2. Sistema de Verificação de Acesso (`acesso_paciente.py`)

**Sistema baseado em lógica proposicional para controle de acesso:**

- **Avaliação de Condições:**
  - A: Paciente tem agendamento marcado
  - B: Documentos em dia (RG/CPF válidos)
  - C: Médico disponível no horário
  - D: Pagamentos anteriores em dia

- **Regras de Acesso:**
  - **Consulta Normal:** `(A ∧ B ∧ C) ∨ (B ∧ C ∧ D)`
  - **Emergência:** `C ∧ (B ∨ D)`

### 3. Sistema de Fila de Atendimento (`fila_atendimento.py`)

**Simulação de fila FIFO (First-In, First-Out):**

- **Triagem Rápida:**
  - Cadastro de nome e CPF
  - Adição sequencial ao final da fila

- **Atendimento FIFO:**
  - Remoção do primeiro paciente da fila
  - Visualização em tempo real da fila atual

## 🛠️ Tecnologias e Conceitos Utilizados

- **Linguagem:** Python 3
- **Estruturas de Dados:** Listas, Dicionários
- **Manipulação de Texto:** Unicodedata para normalização
- **Lógica Proposicional:** Operadores AND, OR para regras de negócio
- **Algoritmos:** FIFO (First-In, First-Out)
- **Tratamento de Erros:** Validação de entrada do usuário

## 📁 Estrutura do Projeto

```
sistema-clinica/
│
├── clinica.py                 # Sistema principal
├── acesso_paciente.py         # Módulo de verificação de acesso
├── fila_atendimento.py        # Sistema de fila FIFO
└── README.md                  # Este arquivo
```

## 🚀 Como Executar

### Sistema Principal
```bash
python clinica.py
```

### Verificação de Acesso
```bash
python acesso_paciente.py
```

### Simulação de Fila
```bash
python fila_atendimento.py
```

## 💡 Destaques Técnicos

### Busca Avançada
```python
def normalizar_texto(texto):
    # Implementa busca case-insensitive e accent-insensitive
    nfkd_form = unicodedata.normalize('NFD', texto)
    only_ascii = "".join([c for c in nfkd_form if not unicodedata.combining(c)])
    return only_ascii.lower()
```

### Lógica de Negócio
```python
# Consulta Normal: (A and B and C) or (B and C and D)
acesso_normal = (A and B and C) or (B and C and D)

# Emergência: C and (B or D)
acesso_emergencia = C and (B or D)
```

### FIFO Implementation
```python
# Adiciona ao final da fila
fila_atendimento.append({"nome": nome_fila, "cpf": cpf_fila})

# Remove do início (FIFO)
atendido = fila_atendimento.pop(0)
```

## 📊 Exemplo de Uso

1. **Cadastro:** Adicione pacientes com dados completos
2. **Busca:** Encontre pacientes por partes do nome
3. **Estatísticas:** Analise a distribuição etária
4. **Acesso:** Verifique elegibilidade para diferentes tipos de consulta
5. **Fila:** Simule o fluxo de atendimento real

## 🎯 Objetivos de Aprendizado

Este projeto demonstra:
- Programação orientada a procedimentos em Python
- Manipulação de estruturas de dados complexas
- Implementação de algoritmos de busca e filtragem
- Aplicação de lógica booleana em sistemas reais
- Desenvolvimento de interfaces de usuário em console
- Tratamento robusto de entrada do usuário

---

*Desenvolvido como parte de um projeto acadêmico/prático em Python*
