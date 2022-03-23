from repo_files import RepositoryProduseFiles
from service import Service
from consola import UI
from teste import Teste

if __name__ == '__main__':
    teste = Teste()
    teste.test_all()
    repo_produse = RepositoryProduseFiles("produse.txt")
    service = Service(repo_produse)
    ui = UI(service)
    ui.run()
