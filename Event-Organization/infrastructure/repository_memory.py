from exceptions.exceptii_infrastructure import RepositoryEroare


class RepositoryPersoane:

    def __init__(self):
        # initializeaza obiectul, cu o lista goala
        self._elemente = []

    def __len__(self):
        # realizeaza un override pentru functia len
        # returneaza numarul de elemente
        return len(self._elemente)

    def adauga(self, persoana):
        # daca elementul dat, de clasa Persoana, nu este in repository, il adauga
        # daca este deja inclus, arunca o exceptie cu aceasta informatie
        if persoana in self._elemente:
            raise RepositoryEroare("Exista deja o persoana cu ID-ul specificat!\n")
        self._elemente.append(persoana)

    def cauta_dupa_id(self, person_id):
        # daca exista o persoana in lista de repository cu id-ul dat, o returneaza
        # daca nu exista, arunca o exceptie cu aceasta informatie
        # person_id este int
        for persoana_de_cautat in self._elemente:
            if persoana_de_cautat.get_person_id() == person_id:
                return persoana_de_cautat
        raise RepositoryEroare("Nu exista o persoana cu ID-ul specificat!\n")

    def modifica(self, persoana_modificata):
        # daca exista o persoana in repository cu id-ul persoanei noi, o modifica cu datele noii persoane
        # daca nu exista, arunca o exceptie cu aceasta informatie
        # persoana_modificata este de clasa Persoana
        if persoana_modificata not in self._elemente:
            raise RepositoryEroare("Nu exista o persoana cu ID-ul specificat!\n")
        for i in range(len(self._elemente)):
            if self._elemente[i] == persoana_modificata:
                self._elemente[i] = persoana_modificata
                return

    def get_all(self):
        # lista returnata este de forma [persoana1, persoana2, ... ]
        # returneaza lista de obiecte
        return self._elemente[:]

    def sterge_dupa_id(self, person_id):
        # daca exista o persoana in repository cu id-ul dat, o sterge
        # daca nu exista, arunca o exceptie cu aceasta informatie
        # person_id este int
        for i in range(len(self._elemente)):
            if self._elemente[i].get_person_id() == person_id:
                del self._elemente[i]
                return
        raise RepositoryEroare("Nu exista o persoana cu ID-ul specificat!\n")


class RepositoryEvenimente:

    def __init__(self):
        # initializeaza obiectul, cu o lista goala
        self._elemente = []

    def __len__(self):
        # realizeaza un override pentru functia len
        # returneaza numarul de elemente
        return len(self._elemente)

    def adauga(self, eveniment):
        # daca elementul dat, de clasa Eveniment, nu este in repository, il adauga
        # daca este deja inclus, arunca o exceptie cu aceasta informatie
        if eveniment in self._elemente:
            raise RepositoryEroare("Exista deja un eveniment cu ID-ul specificat!\n")
        self._elemente.append(eveniment)

    def cauta_dupa_id(self, event_id):
        # daca exista un eveniment in lista de repository cu id-ul dat, il returneaza
        # daca nu exista, arunca o exceptie cu aceasta informatie
        # event_id este int
        for eveniment_de_cautat in self._elemente:
            if eveniment_de_cautat.get_event_id() == event_id:
                return eveniment_de_cautat
        raise RepositoryEroare("Nu exista un eveniment cu ID-ul specificat!\n")

    def modifica(self, eveniment_modificat):
        # daca exista un eveniment in repository cu id-ul evenimentului nou, il modifica cu datele noiului eveniment
        # daca nu exista, arunca o exceptie cu aceasta informatie
        # eveniment_modificat este de clasa Eveniment
        if eveniment_modificat not in self._elemente:
            raise RepositoryEroare("Nu exista un eveniment cu ID-ul specificat!\n")
        for i in range(len(self._elemente)):
            if self._elemente[i] == eveniment_modificat:
                self._elemente[i] = eveniment_modificat
                return

    def get_all(self):
        # returneaza lista de obiecte
        # lista returnata este de forma [eveniment1, eveniment2, ... ]
        return self._elemente[:]

    def sterge_dupa_id(self, event_id):
        # daca exista un eveniment in repository cu id-ul dat, il sterge
        # daca nu exista, arunca o exceptie cu aceasta informatie
        # event_id este int
        for i in range(len(self._elemente)):
            if self._elemente[i].get_event_id() == event_id:
                del self._elemente[i]
                return
        raise RepositoryEroare("Nu exista un eveniment cu ID-ul specificat!\n")


class RepositoryInscrieri:

    def __init__(self):
        # initializeaza obiectul, cu o lista goala
        self._lista = []

    def __len__(self):
        # realizeaza un override pentru functia len
        # returneaza dimensiunea listei
        return len(self._lista)

    def __persoana_in_repo(self, person_id, repo_persoane):
        # verifica daca exista o persoana in repository cu id-ul dat
        # person_id este de tip int si repo_persoane este un obiect de clasa RepositoryPersoane
        for i in range(len(repo_persoane)):
            if repo_persoane[i].get_person_id() == person_id:
                return True
        return False

    def __eveniment_in_repo(self, event_id, repo_evenimente):
        # verifica daca exista un eveniment in repository cu id-ul dat
        # person_id este de tip int si repo_evenimente este un obiect de clasa RepositoryEvenimente
        for i in range(len(repo_evenimente)):
            if repo_evenimente[i].get_event_id() == event_id:
                return True
        return False

    def adauga(self, inscriere, repo_persoane, repo_evenimente):
        # lanseaza verificare id-urilor in repository
        # adauga elementul de tip [person_id, event_id] in lista daca au fost verificate id-urile
        # daca exista deja inscrierea in lista de inscrieri, se va arunca o exceptie
        # daca, intr-un repository, nu exista un obiect cu id-ul dat se va arunca o exceptie
        # inscriere este un obiect de clasa Inscriere, repo_evenimente este un obiect de clasa RepositoryEvenimente,
        # iar repo_persoane este un obiect de clasa RepositoryPersoane
        person_id = inscriere.get_persoana().get_person_id()
        event_id = inscriere.get_eveniment().get_event_id()
        error = ""
        if self.__persoana_in_repo(person_id, repo_persoane) is False:
            error += "Nu exista o persoana cu ID-ul specificat!\n"
        if self.__eveniment_in_repo(event_id, repo_evenimente) is False:
            error += "Nu exista un eveniment cu ID-ul specificat!\n"
        if len(error) > 0:
            raise RepositoryEroare(error)

        for i in range(len(self._lista)):
            if self._lista[i].get_persoana() == inscriere.get_persoana() and self._lista[i].get_eveniment() == inscriere.get_eveniment():
                raise RepositoryEroare("Persoana specificata este deja inscrisa la eveniment!\n")
        self._lista.append(inscriere)

    def sterge(self, inscriere):
        # sterge in element, de clasa Inscriere, din lista, daca exista
        # daca nu exista, se va arunca o exceptie cu aceasta informatie
        person_id = inscriere.get_persoana().get_person_id()
        event_id = inscriere.get_eveniment().get_event_id()
        for i in range(len(self._lista)):
            if self._lista[i].get_persoana() == inscriere.get_persoana() and self._lista[i].get_eveniment() == inscriere.get_eveniment():
                self._lista[i:i+1] = []
                return
        raise RepositoryEroare("Persoana data nu este inscrisa la acest eveniment!\n")

    def get_all(self):
        # returneaza toate elementele din lista
        # lista returnata este de forma [[persoana,eveniment], ... ]
        return self._lista[:]

    def set_all(self, lista_modificata):
        # modifica lista de inscrieri, egaland-o cu lista data
        # din motive evidente, functia poate compromite usor starea programului, asadar trebuie folosita cu grija
        self._lista = lista_modificata
