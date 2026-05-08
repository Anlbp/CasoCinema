class SessaoService:
    def __init__(self, sessao_repo, cinema_repo, filme_repo):
        self.sessao_repo = sessao_repo
        self.cinema_repo = cinema_repo
        self.filme_repo = filme_repo

    def cadastrar(self, cinema_id, filme_id, horario, sala):
        cinema = self.cinema_repo.buscar_por_id(cinema_id)
        filme = self.filme_repo.buscar_por_id(filme_id)

        if not cinema:
            raise Exception("Cinema não encontrado")

        if not filme:
            raise Exception("Filme não encontrado")

        return self.sessao_repo.salvar(
            cinema_id,
            filme_id,
            horario,
            sala
        )

    def registrar_publico(self, sessao_id, publico):
        self.sessao_repo.atualizar_publico(
            sessao_id,
            publico
        )

    def listar_por_cinema(self, cinema_id):
        return self.sessao_repo.listar_por_cinema(
            cinema_id
        )
