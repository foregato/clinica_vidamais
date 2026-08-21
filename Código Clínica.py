import sqlite3
import unicodedata
from flask import Flask, render_template, request, redirect, url_for, flash

# Inicializa o Flask
app = Flask(__name__)
app.secret_key = "clinica-vidamais-chave-simples"

DB_PATH = "clinica.db"


# Abre conexão com o banco retornando linhas acessíveis por nome de coluna
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# Cria a tabela inicial caso não exista
def init_db():
    conn = get_conn()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            telefone TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


# Remove acentos e converte para minúsculas
def normalizar_texto(texto):
    texto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in texto if not unicodedata.combining(c)).lower()


# Página inicial
@app.route("/")
def index():
    return render_template("index.html")


# Cadastro com validações
@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        idade = request.form.get("idade", "").strip()
        telefone = request.form.get("telefone", "").strip()

        erro = None
        if not nome or not all(c.isalpha() or c.isspace() for c in nome):
            erro = "Informe um nome válido (apenas letras e espaços)."
        elif not idade.isdigit() or not (0 <= int(idade) <= 120):
            erro = "Informe uma idade válida entre 0 e 120 anos."
        else:
            numeros = "".join(c for c in telefone if c.isdigit())
            if len(numeros) not in (10, 11):
                erro = "Informe um telefone válido com 10 ou 11 dígitos."

        if erro:
            flash(erro, "erro")
            return render_template("cadastrar.html", nome=nome, idade=idade, telefone=telefone)

        conn = get_conn()
        conn.execute(
            "INSERT INTO pacientes (nome, idade, telefone) VALUES (?, ?, ?)",
            (nome, int(idade), telefone),
        )
        conn.commit()
        conn.close()

        flash("Paciente cadastrado com sucesso!", "sucesso")
        return redirect(url_for("listar"))

    return render_template("cadastrar.html", nome="", idade="", telefone="")


# Listagem de pacientes em ordem alfabética
@app.route("/listar")
def listar():
    conn = get_conn()
    pacientes = conn.execute("SELECT * FROM pacientes ORDER BY nome").fetchall()
    conn.close()
    return render_template("listar.html", pacientes=pacientes)


# Busca por nome ignorando acentos
@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    resultados = None
    termo = ""
    if request.method == "POST":
        termo = request.form.get("termo", "").strip()
        termo_normalizado = normalizar_texto(termo)

        conn = get_conn()
        todos = conn.execute("SELECT * FROM pacientes").fetchall()
        conn.close()

        resultados = [
            p for p in todos if termo_normalizado in normalizar_texto(p["nome"])
        ]

    return render_template("buscar.html", resultados=resultados, termo=termo)


# Exclusão de paciente por ID
@app.route("/excluir/<int:paciente_id>", methods=["POST"])
def excluir(paciente_id):
    conn = get_conn()
    conn.execute("DELETE FROM pacientes WHERE id = ?", (paciente_id,))
    conn.commit()
    conn.close()
    flash("Paciente removido.", "sucesso")
    return redirect(url_for("listar"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
