class CinemaRepository:
    def __init__(self, conn):
        self.conn = conn

    def salvar(self, nome, cidade, estado, endereco, capacidade):
        cursor = self.conn.cursor()

        cursor.execute("""
            INSERT INTO cinemas
            (nome, cidade, estado, endereco, capacidade)
            VALUES (?, ?, ?, ?, ?)
        """, (nome, cidade, estado, endereco, capacidade))

        self.conn.commit()

    def buscar_por_id(self, cinema_id):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT * FROM cinemas WHERE id = ?
        """, (cinema_id,))

        return cursor.fetchone()
