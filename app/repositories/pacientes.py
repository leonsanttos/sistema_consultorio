from app.repositories.base import BaseRepository


class PacienteRepository(BaseRepository):
    table = "pacientes"
    fields = ("nome", "data_nascimento", "telefone")
    order_by = "nome"
