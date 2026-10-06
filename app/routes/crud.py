import sqlite3

from flask import Blueprint, abort, flash, redirect, render_template, request, url_for


def crud_blueprint(nome, repo, titulo, colunas, campos):
    """Cria um blueprint CRUD (listar, novo, editar, excluir) para um repositório.

    colunas: lista de (chave, rótulo) exibidas na listagem.
    campos: lista de dicts com name, label, type, required e, opcionalmente,
            opcoes (função que devolve [(valor, rótulo)]) para campos <select>.
    """
    bp = Blueprint(nome, __name__, url_prefix=f"/{nome}")

    def contexto_form(registro):
        campos_ctx = []
        for campo in campos:
            c = dict(campo)
            if "opcoes" in c:
                c["choices"] = c["opcoes"]()
            campos_ctx.append(c)
        return dict(titulo=titulo, campos=campos_ctx, registro=registro, endpoint=nome)

    def ler_form():
        dados = {c["name"]: request.form.get(c["name"], "").strip() or None for c in campos}
        faltando = [c["label"] for c in campos if c.get("required") and not dados[c["name"]]]
        return dados, faltando

    def salvar(dados, id_=None):
        try:
            if id_ is None:
                repo.criar(dados)
                flash(f"{titulo}: cadastro realizado.", "success")
            else:
                repo.atualizar(id_, dados)
                flash(f"{titulo}: cadastro atualizado.", "success")
            return True
        except sqlite3.IntegrityError:
            flash("Dados inválidos ou duplicados (ex.: CRM já cadastrado).", "error")
            return False

    @bp.get("/")
    def listar():
        return render_template(
            "crud/lista.html", titulo=titulo, colunas=colunas,
            registros=repo.listar(), endpoint=nome,
        )

    @bp.route("/novo", methods=["GET", "POST"])
    def novo():
        if request.method == "POST":
            dados, faltando = ler_form()
            if faltando:
                flash("Preencha: " + ", ".join(faltando), "error")
            elif salvar(dados):
                return redirect(url_for(f"{nome}.listar"))
            return render_template("crud/form.html", **contexto_form(dados))
        return render_template("crud/form.html", **contexto_form(None))

    @bp.route("/<int:id_>/editar", methods=["GET", "POST"])
    def editar(id_):
        registro = repo.buscar(id_)
        if registro is None:
            abort(404)
        if request.method == "POST":
            dados, faltando = ler_form()
            if faltando:
                flash("Preencha: " + ", ".join(faltando), "error")
            elif salvar(dados, id_):
                return redirect(url_for(f"{nome}.listar"))
            return render_template("crud/form.html", **contexto_form(dados))
        return render_template("crud/form.html", **contexto_form(registro))

    @bp.post("/<int:id_>/excluir")
    def excluir(id_):
        try:
            repo.excluir(id_)
            flash("Registro excluído.", "success")
        except sqlite3.IntegrityError:
            flash("Não é possível excluir: existem consultas vinculadas.", "error")
        return redirect(url_for(f"{nome}.listar"))

    return bp
