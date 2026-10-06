from app import repositories as repo
from app.routes.crud import crud_blueprint


def _pacientes():
    return [(p["id"], p["nome"]) for p in repo.pacientes.listar()]


def _medicos():
    return [(m["id"], m["nome"]) for m in repo.medicos.listar()]


bp = crud_blueprint(
    "consultas", repo.consultas, "Consultas",
    colunas=[
        ("data_consulta", "Data/Hora"), ("paciente", "Paciente"),
        ("medico", "Médico"), ("motivo", "Motivo"),
    ],
    campos=[
        {"name": "paciente_id", "label": "Paciente", "type": "select",
         "required": True, "opcoes": _pacientes},
        {"name": "medico_id", "label": "Médico", "type": "select",
         "required": True, "opcoes": _medicos},
        {"name": "data_consulta", "label": "Data e hora", "type": "datetime-local",
         "required": True},
        {"name": "motivo", "label": "Motivo", "type": "text"},
    ],
)
