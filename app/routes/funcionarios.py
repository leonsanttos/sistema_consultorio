from app import repositories as repo
from app.routes.crud import crud_blueprint

bp = crud_blueprint(
    "funcionarios", repo.funcionarios, "Funcionários",
    colunas=[("nome", "Nome"), ("cargo", "Cargo"), ("data_contratacao", "Contratação")],
    campos=[
        {"name": "nome", "label": "Nome", "type": "text", "required": True},
        {"name": "cargo", "label": "Cargo", "type": "text", "required": True},
        {"name": "data_contratacao", "label": "Data de contratação", "type": "date"},
    ],
)
