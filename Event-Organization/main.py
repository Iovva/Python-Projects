from infrastructure.memorie_sau_fisier import LucruMemeorieFisier, CreeareFisiere
from testare.teste import *
from ui.consola import UI

'''
created: 11.04.2020
@author: IOWA
'''

if __name__ == '__main__':
    # main
    # functia creeaza obictele de teste, validare, repository, service si ui il lanseaza pe cel de ui
    # obiectul service contine validatori si repository

    fisiere = CreeareFisiere()
    mod = LucruMemeorieFisier()

    if mod.check():
        path = fisiere.path()
        repo_persoane = RepositoryPersoaneFiles(path + "\persoane.txt")
        repo_evenimente = RepositoryEvenimenteFiles(path + "\evenimente.txt")
        repo_inscrieri = RepositoryInscrieriFiles(path + "\inscrieri.txt")
    else:
        repo_persoane = RepositoryPersoane()
        repo_evenimente = RepositoryEvenimente()
        repo_inscrieri = RepositoryInscrieri()

    validator_persoana = ValidatorPersoana()
    service_persoane = ServicePersoane(validator_persoana, repo_persoane)
    validator_eveniment = ValidatorEveniment()
    service_evenimente = ServiceEvenimente(validator_eveniment, repo_evenimente)
    service_inscrieri = ServiceInscrieri(repo_persoane, repo_evenimente, repo_inscrieri)

    ui = UI(service_persoane, service_evenimente, service_inscrieri)
    ui.run()
