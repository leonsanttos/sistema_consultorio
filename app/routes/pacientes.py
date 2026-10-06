from app import repositories as repo
from app.routes.crud import crud_blueprint

bp = crud_blueprint(
    "pacientes", repo.pacientes, "Pacientes",
    colunas=[("nome", "Nome"), ("data_nascimento", "Nascimento"), ("telefone", "Telefone")],
    campos=[
        {"name": "nome", "label": "Nome", "type": "text", "required": True},
        {"name": "data_nascimento", "label": "Data de nascimento", "type": "date"},
        {"name": "telefone", "label": "Telefone", "type": "tel"},
    ],
)
