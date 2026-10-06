from app.database import get_db


class BaseRepository:
    table = ""
    fields = ()
    order_by = "id"

    def listar(self):
        return get_db().execute(
            f"SELECT * FROM {self.table} ORDER BY {self.order_by}"
        ).fetchall()

    def buscar(self, id_):
        return get_db().execute(
            f"SELECT * FROM {self.table} WHERE id = ?", (id_,)
        ).fetchone()

    def criar(self, dados):
        db = get_db()
        colunas = ", ".join(self.fields)
        marcas = ", ".join("?" for _ in self.fields)
        cur = db.execute(
            f"INSERT INTO {self.table} ({colunas}) VALUES ({marcas})",
            [dados.get(c) for c in self.fields],
        )
        db.commit()
        return cur.lastrowid

    def atualizar(self, id_, dados):
        db = get_db()
        sets = ", ".join(f"{c} = ?" for c in self.fields)
        db.execute(
            f"UPDATE {self.table} SET {sets} WHERE id = ?",
            [dados.get(c) for c in self.fields] + [id_],
        )
        db.commit()

    def excluir(self, id_):
        db = get_db()
        db.execute(f"DELETE FROM {self.table} WHERE id = ?", (id_,))
        db.commit()
