class SessaoRepository:
    def __init__(self, conn):
        self.conn = conn

    def salvar(self, cinema_id, filme_id, horario, sala):
        cursor = self.conn.cursor()

        cursor.execute("""
            INSERT INTO sessoes
            (cinema_id, filme_id, horario, sala, publico)
            VALUES (?, ?, ?, ?, 0)
        """, (cinema_id, filme_id, horario, sala))

        self.conn.commit()

        return cursor.lastrowid

    def atualizar_publico(self, sessao_id, publico):
        cursor = self.conn.cursor()

        cursor.execute("""
            UPDATE sessoes
            SET publico = ?
            WHERE id = ?
        """, (publico, sessao_id))

        self.conn.commit()

    def listar_por_cinema(self, cinema_id):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT * FROM sessoes
            WHERE cinema_id = ?
        """, (cinema_id,))

        return cursor.fetchall()
