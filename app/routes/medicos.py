from app import repositories as repo
from app.routes.crud import crud_blueprint

bp = crud_blueprint(
    "medicos", repo.medicos, "Médicos",
    colunas=[("nome", "Nome"), ("especialidade", "Especialidade"), ("crm", "CRM")],
    campos=[
        {"name": "nome", "label": "Nome", "type": "text", "required": True},
        {"name": "especialidade", "label": "Especialidade", "type": "text"},
        {"name": "crm", "label": "CRM", "type": "text", "required": True},
    ],
)
