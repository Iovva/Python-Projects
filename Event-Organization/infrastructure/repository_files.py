from infrastructure.repository_memory import RepositoryPersoane, RepositoryEvenimente, RepositoryInscrieri
from domain.entities import Persoana, Eveniment, Inscriere


class RepositoryPersoaneFiles(RepositoryPersoane):

    def __init__(self, filename):
        # initializeaza obiectul cu filename-ul fisierului .txt de persoane, de tip string
        self.__filename = filename
        RepositoryPersoane.__init__(self)

    def __len__(self):
        # actualizeaza repository-ul cu valorile din fisier
        # returneaza numarul de persoane din repository
        self.__citeste_tot_din_fisier()
        return RepositoryPersoane.__len__(self)

    def __citeste_tot_din_fisier(self):
        # citeste toate randurile din fisier, separa valorile persoanelor si le baga in repository
        # randurile fisierului sunt de tip:
        # id;nume;adresa
        with open(self.__filename, "r") as f:
            self._elemente = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(";")
                    persoana = Persoana(int(parts[0]), parts[1], parts[2])
                    self._elemente.append(persoana)

    def __apend_persoana_fisier(self, persoana):
        # adauga un rand nou in fisierul .txt repository care contine valorile persoanei de clasa Persoana
        # randul adagat va fi de tipul:
        # id;nume;adresa
        with open(self.__filename, "a") as f:
            person_id = str(persoana.get_person_id())
            nume = persoana.get_nume()
            adresa = persoana.get_adresa()
            f.write(person_id + ";" + nume + ";" + adresa + "\n")

    def __scrie_tot_in_fisier(self):
        # rescrie tot continul fisierului cu valorile persoanelor din repository
        with open(self.__filename, "w") as f:
            for persoana in self._elemente:
                person_id = str(persoana.get_person_id())
                nume = persoana.get_nume()
                adresa = persoana.get_adresa()
                f.write(person_id + ";" + nume + ";" + adresa + "\n")

    def adauga(self, persoana):
        # actualizeaza repository-ul cu valorile din fisier
        # primeste un obiect de clasa Persoana, adauga persoana in repo, dar si in fisierul text
        self.__citeste_tot_din_fisier()
        RepositoryPersoane.adauga(self, persoana)
        self.__apend_persoana_fisier(persoana)

    def cauta_dupa_id(self, person_id):
        # actualizeaza repository-ul cu valorile din fisier
        # cauta si returneaza o persoana cu id-ul dat
        # person_id - int
        self.__citeste_tot_din_fisier()
        return RepositoryPersoane.cauta_dupa_id(self, person_id)

    def modifica(self, persoana_modificata):
        # actualizeaza repository-ul cu valorile din fisier
        # primeste un obiect de clasa Persoana, modifica persoana in repo, si rescrie fisierul text cu persoanele din
        # repo
        self.__citeste_tot_din_fisier()
        RepositoryPersoane.modifica(self, persoana_modificata)
        self.__scrie_tot_in_fisier()

    def get_all(self):
        # actualizeaza repository-ul cu valorile din fisier
        # returneaza toate persoanele din repository
        self.__citeste_tot_din_fisier()
        return RepositoryPersoane.get_all(self)

    def sterge_dupa_id(self, person_id):
        # actualizeaza repository-ul cu valorile din fisier
        # primeste id-ul unui obiect de clasa Persoana, sterge persoana din repo, si rescrie fisierul text cu persoanele
        # din repo
        self.__citeste_tot_din_fisier()
        RepositoryPersoane.sterge_dupa_id(self, person_id)
        self.__scrie_tot_in_fisier()


class RepositoryEvenimenteFiles(RepositoryEvenimente):

    def __init__(self, filename):
        # initializeaza obiectul cu filename-ul fisierului .txt de evenimente, de tip string
        self.__filename = filename
        RepositoryEvenimente.__init__(self)

    def __len__(self):
        # actualizeaza repository-ul cu valorile din fisier
        # returneaza numarul de evenimente din repository
        self.__citeste_tot_din_fisier()
        return RepositoryEvenimente.__len__(self)

    def __citeste_tot_din_fisier(self):
        # citeste toate randurile din fisier, separa valorile evenimentelor si le baga in repository
        # randurile fisierului sunt de tip:
        # id;data;timp;adresa
        with open(self.__filename, "r") as f:
            self._elemente = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(";")
                    eveniment = Eveniment(int(parts[0]), parts[1], parts[2], parts[3])
                    self._elemente.append(eveniment)

    def __apend_eveniment_fisier(self, eveniment):
        # adauga un rand nou in fisierul .txt repository care contine valorile persoanei de clasa Eveniment
        # randul adagat va fi de tipul:
        # id;data;timp;adresa
        with open(self.__filename, "a") as f:
            event_id = str(eveniment.get_event_id())
            data = eveniment.get_data()
            timp = eveniment.get_timp()
            descriere = eveniment.get_descriere()
            f.write(event_id + ";" + data + ";" + timp + ";" + descriere + "\n")

    def __scrie_tot_in_fisier(self):
        # rescrie tot continul fisierului cu valorile evenimentelor din repository
        with open(self.__filename, "w") as f:
            for eveniment in self._elemente:
                event_id = str(eveniment.get_event_id())
                data = eveniment.get_data()
                timp = eveniment.get_timp()
                descriere = eveniment.get_descriere()
                f.write(event_id + ";" + data + ";" + timp + ";" + descriere + "\n")

    def adauga(self, eveniment):
        # actualizeaza repository-ul cu valorile din fisier
        # primeste un obiect de clasa Eveniment, adauga evenimentul in repo, dar si in fisierul text
        self.__citeste_tot_din_fisier()
        RepositoryEvenimente.adauga(self, eveniment)
        self.__apend_eveniment_fisier(eveniment)

    def cauta_dupa_id(self, event_id):
        # actualizeaza repository-ul cu valorile din fisier
        # cauta si returneaza un eveniment cu id-ul dat
        # event_id - int
        self.__citeste_tot_din_fisier()
        return RepositoryEvenimente.cauta_dupa_id(self, event_id)

    def modifica(self, eveniment_modificat):
        # actualizeaza repository-ul cu valorile din fisier
        # primeste un obiect de clasa Eveniment, modifica evenimentul in repo, si rescrie fisierul text cu persoanele
        # din repo
        self.__citeste_tot_din_fisier()
        RepositoryEvenimente.modifica(self, eveniment_modificat)
        self.__scrie_tot_in_fisier()

    def get_all(self):
        # actualizeaza repository-ul cu valorile din fisier
        # returneaza toate evenimentele din repository
        self.__citeste_tot_din_fisier()
        return RepositoryEvenimente.get_all(self)

    def sterge_dupa_id(self, event_id):
        # actualizeaza repository-ul cu valorile din fisier
        # primeste un id-ul ubui obiect de clasa Eveniment, sterge evenimentul din  repo, si rescrie fisierul text cu
        # persoanele din repo
        # event_id - int
        self.__citeste_tot_din_fisier()
        RepositoryEvenimente.sterge_dupa_id(self, event_id)
        self.__scrie_tot_in_fisier()


class RepositoryInscrieriFiles(RepositoryInscrieri):

    def __init__(self, filename):
        # initializeaza obiectul cu filename-ul fisierului .txt de inscrieri, de tip string
        self.__filename = filename
        RepositoryInscrieri.__init__(self)

    def __len__(self):
        # actualizeaza repository-ul cu valorile din fisier
        # returneaza numarul de inscrieri din repository
        self.__citeste_tot_din_fisier()
        return RepositoryInscrieri.__len__(self)

    def __citeste_tot_din_fisier(self):
        # citeste toate randurile din fisier, separa valorile persoanelor si ale evenimentelor si le baga in
        # repository-ul de persoane, respectiv repository-ul de evenimente
        # randurile fisierului sunt de tip:
        # id_persoana;nume;adresa;id_event;data;timp;adresa
        with open(self.__filename, "r") as f:
            self._lista = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(";")
                    persoana = Persoana(int(parts[0]), parts[1], parts[2])
                    eveniment = Eveniment(int(parts[3]), parts[4], parts[5], parts[6])
                    inscriere = Inscriere(persoana, eveniment)
                    self._lista.append(inscriere)

    def __apend_inscriere_fisier(self, inscriere):
        # adauga un rand nou in fisierul .txt repository care contine valorile inscrierii de clasa Inscriere
        # randul adagat va fi de tipul:
        # id_persoana;nume;adresa;id_event;data;timp;adresa
        with open(self.__filename, "a") as f:
            persoana = inscriere.get_persoana()
            person_id = str(persoana.get_person_id())
            nume = persoana.get_nume()
            adresa = persoana.get_adresa()
            eveniment = inscriere.get_eveniment()
            event_id = str(eveniment.get_event_id())
            data = eveniment.get_data()
            timp = eveniment.get_timp()
            descriere = eveniment.get_descriere()
            f.write(person_id + ";" + nume + ";" + adresa + ";" + event_id + ";" + data + ";" + timp + ";" + descriere + "\n")

    def __scrie_tot_in_fisier(self):
        # rescrie tot continul fisierului cu valorile inscrierilor din repository
        with open(self.__filename, "w") as f:
            for inscriere in self._lista:
                persoana = inscriere.get_persoana()
                person_id = str(persoana.get_person_id())
                nume = persoana.get_nume()
                adresa = persoana.get_adresa()
                eveniment = inscriere.get_eveniment()
                event_id = str(eveniment.get_event_id())
                data = eveniment.get_data()
                timp = eveniment.get_timp()
                descriere = eveniment.get_descriere()
                f.write(person_id + ";" + nume + ";" + adresa + ";" + event_id + ";" + data + ";" + timp + ";" + descriere + "\n")

    def adauga(self, inscriere, repo_persoane, repo_evenimente):
        # actualizeaza repository-ul cu valorile din fisier
        # primeste un obiect de clasa Inscriere, unul de clasa RepositoryPersoane si unul de Repository Evenimente,
        # si adauga inscrierea in repo, dar si in fisierul text
        self.__citeste_tot_din_fisier()
        RepositoryInscrieri.adauga(self, inscriere, repo_persoane, repo_evenimente)
        self.__apend_inscriere_fisier(inscriere)

    def sterge(self, inscriere):
        # actualizeaza repository-ul cu valorile din fisier
        # primeste un obiect de clasa Inscriere, sterge inscrierea din repo, si rescrie fisierul text cu inscrierile din
        # repo
        self.__citeste_tot_din_fisier()
        RepositoryInscrieri.sterge(self, inscriere)
        self.__scrie_tot_in_fisier()

    def get_all(self):
        # actualizeaza repository-ul cu valorile din fisier
        # returneaza toate inscrierile din repository
        self.__citeste_tot_din_fisier()
        return RepositoryInscrieri.get_all(self)

    def set_all(self, lista_modificata):
        # modifica lista de inscrieri din repo, egaland-o cu lista data, urmand sa rescrie tot continul fisierului cu
        # valorile inscrierilor din repository
        RepositoryInscrieri.set_all(self, lista_modificata)
        self.__scrie_tot_in_fisier()
