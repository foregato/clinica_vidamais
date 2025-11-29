# 📊 Módulo de Cadastro e Estatísticas da Clínica Vida+ (Passo 2)

Este módulo Python simula o sistema básico de **cadastro e gestão de informações** de pacientes da Clínica Vida+. Ele demonstra a aplicação de estruturas de dados (listas e dicionários) e lógica de programação para cálculos estatísticos e busca de dados.

---

## 📋 Funcionalidades Implementadas

As seguintes funcionalidades foram desenvolvidas para atender aos requisitos do Passo 2:

### 1. Cadastro de Pacientes
* Permite o registro de **Nome**, **Idade** e **Telefone**.
* Utiliza **dicionários** para armazenar os dados de cada paciente e uma **lista** principal (`pacientes`) para gerenciar todos os registros.
* Inclui **tratamento de erros (`try-except`)** para garantir que a idade seja inserida como um número inteiro válido (entre 0 e 120 anos).

### 2. Estatísticas de Pacientes
A função de estatísticas calcula e exibe as métricas essenciais:
* **Total de pacientes** cadastrados.
* **Idade Média** dos pacientes.
* Identificação e exibição do **paciente mais novo** e do **paciente mais velho**.

### 3. Busca e Listagem
* **Buscar Paciente:** Permite a busca parcial pelo nome (não sensível a maiúsculas/minúsculas).
* **Listar Todos:** Exibe todos os pacientes cadastrados em formato organizado.

---

## 🛠️ Como Executar o Módulo

### Pré-requisitos
* **Python 3.x** instalado.

### Execução
1.  **Clone o Repositório** (ou copie o código Python para um arquivo, ex: `gestao_pacientes.py`).
2.  **Execute o Arquivo** via terminal:
    ```bash
    python gestao_pacientes.py
    ```
3.  **Utilize o Menu:** O programa iniciará com um menu de opções (1 a 4) para realizar o cadastro, ver estatísticas, buscar ou listar pacientes.

---

## 💻 Estrutura de Dados Principal

O programa usa a seguinte estrutura para armazenar os dados:

```python
# Lista principal
pacientes = [
    {
        "nome": "João da Silva", 
        "idade": 45, 
        "telefone": "99991111"
    },
    # ... outros pacientes
]
