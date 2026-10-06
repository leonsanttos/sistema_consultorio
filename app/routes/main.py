from flask import Blueprint, render_template

from app import repositories as repo

bp = Blueprint("main", __name__)


@bp.get("/")
def inicio():
    totais = {
        "Médicos": len(repo.medicos.listar()),
        "Pacientes": len(repo.pacientes.listar()),
        "Funcionários": len(repo.funcionarios.listar()),
        "Consultas": len(repo.consultas.listar()),
    }
    return render_template("inicio.html", totais=totais)
