from app.database import get_db
from app.repositories.base import BaseRepository


class ConsultaRepository(BaseRepository):
    table = "consultas"
    fields = ("paciente_id", "medico_id", "data_consulta", "motivo")

    def listar(self):
        return get_db().execute(
            """
            SELECT c.id, c.data_consulta, c.motivo,
                   p.nome AS paciente, m.nome AS medico
            FROM consultas c
            JOIN pacientes p ON p.id = c.paciente_id
            JOIN medicos m ON m.id = c.medico_id
            ORDER BY c.data_consulta
            """
        ).fetchall()
