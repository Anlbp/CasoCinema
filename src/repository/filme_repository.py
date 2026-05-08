class FilmeRepository:
    def __init__(self, conn):
        self.conn = conn

    def salvar(self, titulo, duracao, genero, diretor, elenco):
        cursor = self.conn.cursor()

        cursor.execute("""
            INSERT INTO filmes
            (titulo, duracao, genero, diretor, elenco)
            VALUES (?, ?, ?, ?, ?)
        """, (titulo, duracao, genero, diretor, elenco))

        self.conn.commit()

    def buscar_por_id(self, filme_id):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT * FROM filmes WHERE id = ?
        """, (filme_id,))

        return cursor.fetchone()
