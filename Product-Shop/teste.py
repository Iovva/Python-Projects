from domain import Produs
from repo_files import RepositoryProduseFiles
from exceptions import RepoEroare
from service import Service

class Teste:

    def __teste_domain(self):
        # teste pentru domain ( obiecte de tip Produs )
        id = 1
        denumire = "masa"
        pret = 50
        produs = Produs(id, denumire, pret)
        assert (produs.get_id() == 1)
        assert (produs.get_denumire() == "masa")
        assert (produs.get_pret() == 50)
        produs.set_denumire("jucarie")
        produs.set_pret(25)
        assert (produs.get_denumire() == "jucarie")
        assert (produs.get_pret() == 25)


    def __teste_repository(self):
        # teste cu repository
        repo_produse = RepositoryProduseFiles("teste.txt")
        assert(len(repo_produse.get_all()) == 0)
        repo_produse.adauga(Produs(1, "masa", 50))
        assert (repo_produse.get_all()[0].get_id() == 1)
        assert (repo_produse.get_all()[0].get_denumire() == "masa")
        assert (repo_produse.get_all()[0].get_pret() == 50)
        repo_produse.adauga(Produs(2, "jucarie", 25))
        assert (len(repo_produse.get_all()) == 2)
        try:
            repo_produse.adauga(Produs(1, "masa", 50))
            assert False
        except RepoEroare as RE:
            assert (str(RE) == "Exista deja un produs cu id-ul dat!")

        assert (len(repo_produse.get_all()) == 2)
        sterse = repo_produse.sterge(3)
        assert (sterse == 0)
        assert (len(repo_produse.get_all()) == 2)
        sterse = repo_produse.sterge(2)
        assert (sterse == 1)
        assert (len(repo_produse.get_all()) == 1)
        sterse = repo_produse.sterge(1)
        assert (sterse == 1)
        assert (len(repo_produse.get_all()) == 0)


    def __teste_service(self):
        # teste cu service
        repo_produse = RepositoryProduseFiles("teste.txt")
        service = Service(repo_produse)
        service.adauga(1, "masa", 50)
        service.adauga(12, "jucarie", 25)
        assert (len(repo_produse.get_all()) == 2)
        sterse = service.sterge(1)
        assert (sterse == 2)
        assert (len(repo_produse.get_all()) == 0)


    def test_all(self):
        # lanseaza toate testele
        self.__teste_domain()
        self.__teste_repository()
        self.__teste_service()