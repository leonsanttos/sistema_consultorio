from app.repositories.base import BaseRepository


class FuncionarioRepository(BaseRepository):
    table = "funcionarios"
    fields = ("nome", "cargo", "data_contratacao")
    order_by = "nome"
