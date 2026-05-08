class SessaoController:
    def __init__(self, service):
        self.service = service

    def criar_sessao(self, cinema_id, filme_id, horario, sala):
        return self.service.cadastrar(
            cinema_id,
            filme_id,
            horario,
            sala
        )

    def registrar_publico(self, sessao_id, publico):
        self.service.registrar_publico(
            sessao_id,
            publico
        )

    def listar_sessoes(self, cinema_id):
        return self.service.listar_por_cinema(
            cinema_id
        )
