import sys
sys.path.insert(0, "src")
 
from db.database import get_connection, init_db
from repository.cinema_repository import CinemaRepository
from repository.filme_repository import FilmeRepository
from repository.sessao_repository import SessaoRepository
from service.sessao_service import SessaoService
 
 
def make_service():
    conn = get_connection(":memory:")
    init_db(conn)
    cinema_repo = CinemaRepository(conn)
    filme_repo  = FilmeRepository(conn)
    sessao_repo = SessaoRepository(conn)
    cinema_repo.salvar("Cinema Teste", "São Paulo", "SP", "Rua A, 1", 100)
    filme_repo.salvar("Filme Teste", 120, "Ação", "Diretor X", "Ator Y")
    return SessaoService(sessao_repo, cinema_repo, filme_repo)
 
 
def test_cadastrar_sessao():
    s = make_service()
    id = s.cadastrar(1, 1, "2025-06-10 14:00", "A1")
    assert id is not None
    print("OK : cadastrar sessao")
 
 
def test_conflito_horario():
    s = make_service()
    s.cadastrar(1, 1, "2025-06-10 14:00", "A1")
    try:
        s.cadastrar(1, 1, "2025-06-10 14:10", "A1")
        assert False
    except ValueError as e:
        assert "intervalo" in str(e).lower()
    print("OK : conflito de horario")
 
 
def test_registrar_publico():
    s = make_service()
    s.cadastrar(1, 1, "2025-06-10 14:00", "A1")
    s.registrar_publico(1, 80)
    print("OK : registrar publico")
 
 
def test_capacidade_excedida():
    s = make_service()
    s.cadastrar(1, 1, "2025-06-10 14:00", "A1")
    try:
        s.registrar_publico(1, 200)
        assert False
    except ValueError as e:
        assert "capacidade" in str(e).lower()
    print("OK : capacidade excedida")
 
 
if __name__ == "__main__":
    test_cadastrar_sessao()
    test_conflito_horario()
    test_registrar_publico()
    test_capacidade_excedida()
    print("\nTodos os testes foram bem sucedidos")
