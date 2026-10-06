from app.repositories.base import BaseRepository


class MedicoRepository(BaseRepository):
    table = "medicos"
    fields = ("nome", "especialidade", "crm")
    order_by = "nome"
