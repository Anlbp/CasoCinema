import sys
sys.path.insert(0, "src")
 
from db.database import get_connection, init_db
from repository.cinema_repository import CinemaRepository
from repository.filme_repository import FilmeRepository
from repository.sessao_repository import SessaoRepository
from service.sessao_service import SessaoService
 
 
def main():
    conn = get_connection()
    init_db(conn)
 
    cinemas  = CinemaRepository(conn)
    filmes   = FilmeRepository(conn)
    sessoes  = SessaoRepository(conn)
    service  = SessaoService(sessoes, cinemas, filmes)
 
    # seed
    cinemas.salvar("CineMax SP", "São Paulo", "SP", "Av. Paulista, 100", 300)
    filmes.salvar("Inception", 148, "Guerra", "Joe Biden", "Donald Trump")
 
    # casos de uso
    sessao_id = service.cadastrar(1, 1, "2025-06-10 14:00", "A1")
    print(f"Sessão criada: id={sessao_id}")
 
    service.registrar_publico(sessao_id, 250)
    print("Público registrado: 250")
 
    for s in service.listar_por_cinema(1):
        print(s)
 
 
if __name__ == "__main__":
    main()
