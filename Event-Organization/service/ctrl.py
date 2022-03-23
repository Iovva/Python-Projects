from domain.entities import Persoana, Eveniment, Inscriere
from sortari.sortari import Sort
from domain.dto import IdFrecventaDTO
import random


class ServicePersoane:

    def __init__(self, validator_persoana, repository_persoane):
        self.__validator_persoana = validator_persoana
        self.__repository_persoane = repository_persoane

    def adauga_persoana(self, person_id, nume, adresa):
        # creeaza un obiect de clasa Persoana cu datele primite
        # lanseaza validarea datelelor din obiect
        # daca trece de validare, lanseaza adaosul in obicetul de tip RepositoryPersoane
        # person_id - int, nume si adresa - string
        persoana = Persoana(person_id, nume, adresa)
        self.__validator_persoana.check(persoana)
        self.__repository_persoane.adauga(persoana)

    def sterge_persoana(self, person_id):
        # lanseaza stergerea unui obiect de clasa Persoana din repository, cu id-ul primit
        # realizeaza o copie a listei de inscrieri, fara inscrierile care contin persoana stearsa, avand id-ul primit
        # modifica lista veche cu cea care nu contine inscrieri ale persoanei sterse
        # person_id - int
        self.__repository_persoane.sterge_dupa_id(person_id)

    def modifica_persoana(self, person_id, nume, adresa):
        # creeaza un obiect de clasa Persoana cu datele primite
        # lanseaza validarea datelelor din obiect
        # daca trece de validare, lanseaza modificarea persoanei din repository cu datele persoanei noi
        # person_id - int, nume si adresa - string
        persoana = Persoana(person_id, nume, adresa)
        self.__validator_persoana.check(persoana)
        self.__repository_persoane.modifica(persoana)

    def cauta_persoana(self, person_id):
        # cauta un obiect de clasa Persoana cu id-ul primit
        # returneaza obiectul
        # person_id - int
        persoana = self.__repository_persoane.cauta_dupa_id(person_id)
        return persoana

    def get_persoane(self):
        # returneaza obiectul de clasa RepositoryPersoane
        return self.__repository_persoane.get_all()

    def adauga_persoane_random(self, nr_persoane):
        # adauga nr_persoane persoane generat aleatoriu
        # nr_persoane - int
        while nr_persoane:
            while True:
                person_id = random.randrange(1, 1000)
                try:
                    persoana = Persoana(person_id, "fd", "dasd")
                    self.__repository_persoane.adauga(persoana)
                    self.__repository_persoane.sterge_dupa_id(person_id)
                    break
                except:
                    pass

            nume = ""
            nume_range = random.randrange(3, 15)
            for i in range(nume_range):
                litera = chr(random.randrange(97, 122))
                nume = nume + litera

            adresa = ""
            adresa_range = random.randrange(3, 10)
            for i in range(adresa_range):
                litera = chr(random.randrange(97, 122))
                adresa = adresa + litera

            persoana = Persoana(person_id, nume, adresa)
            self.__repository_persoane.adauga(persoana)
            nr_persoane = nr_persoane - 1


class ServiceEvenimente:

    def __init__(self, validator_eveniment, repository_evenimente):
        self.__validator_eveniment = validator_eveniment
        self.__repository_evenimente = repository_evenimente

    def adauga_eveniment(self, event_id, data, timp, descriere):
        # creeaza un obiect de clasa Eveniment cu datele primite
        # lanseaza validarea datelelor din obiect
        # daca trece de validare, lanseaza adaosul in obicetul de tip RepositoryEvenimente
        # event_id - int, data, timp, descriere - string
        eveniment = Eveniment(event_id, data, timp, descriere)
        self.__validator_eveniment.check(eveniment)
        self.__repository_evenimente.adauga(eveniment)

    def sterge_eveniment(self, event_id):
        # lanseaza stergerea unui obiect de clasa Eveniment din repository, cu id-ul primit
        # realizeaza o copie a listei de inscrieri, fara inscrierile care contin evenimentul stears, avand id-ul primit
        # modifica lista veche cu cea care nu contine inscrieri ale evenimentului sters
        # event_id - int
        self.__repository_evenimente.sterge_dupa_id(event_id)

    def modifica_eveniment(self, event_id, data, timp, descriere):
        # creeaza un obiect de clasa Eveniment cu datele primite
        # lanseaza validarea datelelor din obiect
        # daca trece de validare, lanseaza modificarea evenimentului din repository cu datele evenimentului noi
        # event_id - int, data, timp, descriere - string
        eveniment = Eveniment(event_id, data, timp, descriere)
        self.__validator_eveniment.check(eveniment)
        self.__repository_evenimente.modifica(eveniment)

    def cauta_eveniment(self, event_id):
        # cauta un obiect de clasa Eveniment cu id-ul primit
        # returneaza obiectul
        # event_id - int
        eveniment = self.__repository_evenimente.cauta_dupa_id(event_id)
        return eveniment

    def get_evenimente(self):
        # returneaza obiectul de clasa RepositoryEvenimente
        return self.__repository_evenimente.get_all()

    def adauga_evenimente_random(self, nr_evenimente):
        # adauga nr_evenimente evenimente generat aleatoriu
        # nr_evenimente - int
        while nr_evenimente:
            while True:
                event_id = random.randrange(1, 1000)
                try:
                    eveniment = Eveniment(event_id, "23.10.2020", "14:20", "ads")
                    self.__repository_evenimente.adauga(eveniment)
                    self.__repository_evenimente.sterge_dupa_id(event_id)
                    break
                except:
                    pass

            descriere = ""
            descriere_range = random.randrange(3, 15)
            for i in range(descriere_range):
                litera = chr(random.randrange(97, 122))
                descriere = descriere + litera

            while True:
                luna = random.randrange(1, 12)
                if luna < 10:
                    luna = "0" + str(luna)
                an = random.randrange(2021, 2100)
                if luna == 1 or luna == 3 or luna == 5 or luna == 7 or luna == 8 or luna == 10 or luna == 11:
                    zi = random.randrange(1, 32)
                elif luna == 2:
                    if an % 4 == 0 and an % 100 != 0:
                        zi = random.randrange(1, 30)
                    else:
                        zi = random.randrange(1, 29)
                else:
                    zi = random.randrange(1, 31)
                if zi < 10:
                    zi = "0" + str(zi)
                data = str(zi) + "." + str(luna) + "." + str(an)
                try:
                    eveniment = Eveniment(event_id, data, "10:00", "adsa")
                    self.__repository_evenimente.adauga(eveniment)
                    self.__repository_evenimente.sterge_dupa_id(event_id)
                    break
                except:
                    pass

            while True:
                ora = random.randrange(1, 24)
                if ora < 10:
                    ora = "0" + str(ora)
                minut = random.randrange(1, 60)
                if minut < 10:
                    minut = "0" + str(minut)
                timp = str(ora) + ":" + str(minut)
                try:
                    eveniment = Eveniment(event_id, data, timp, "asd")
                    self.__repository_evenimente.adauga(eveniment)
                    self.__repository_evenimente.sterge_dupa_id(event_id)
                    break
                except:
                    pass

            eveniment = Eveniment(event_id, data, timp, descriere)
            self.__repository_evenimente.adauga(eveniment)

            nr_evenimente = nr_evenimente - 1


class ServiceInscrieri:

    def __init__(self, repo_persoane, repo_evenimente, repo_inscrieri):
        self.__repo_persoane = repo_persoane
        self.__repo_evenimente = repo_evenimente
        self.__repo_inscrieri = repo_inscrieri

    def adauga_inscriere(self, person_id, event_id):
        # adauga in lista de inscrieri o lista de tip [persoana,eveniment] cu person_id si event_id date daca
        # inscrierea nu este deja in lista si daca exista obiectul Persoana si obiectul Eveniment in repository-ul
        # de persoane, respectiv de evenimente
        # person_id, event_id - int
        persoana = self.__repo_persoane.cauta_dupa_id(person_id)
        eveniment = self.__repo_evenimente.cauta_dupa_id(event_id)
        repo_persoane = self.__repo_persoane.get_all()
        repo_evenimente = self.__repo_evenimente.get_all()
        inscriere = Inscriere(persoana, eveniment)
        self.__repo_inscrieri.adauga(inscriere, repo_persoane, repo_evenimente)

    def sterge_inscriere(self, person_id, event_id):
        # sterge din lista de inscrieri o lista de tip [persoana,eveniment], person_id si event_id date daca
        # inscrierea este in lista
        persoana = self.__repo_persoane.cauta_dupa_id(person_id)
        eveniment = self.__repo_evenimente.cauta_dupa_id(event_id)
        inscriere = Inscriere(persoana, eveniment)
        self.__repo_inscrieri.sterge(inscriere)

    def sterge_persoana_inscrieri(self, person_id):
        # returneaza o copie a listei de inscrieri, fara inscrierile care contin id-ul persoanei date
        # person_id - int
        lista_inscrieri = self.__repo_inscrieri.get_all()
        i = 0
        n = len(lista_inscrieri)
        while i < n:
            if lista_inscrieri[i].get_persoana().get_person_id() == person_id:
                lista_inscrieri[i:i + 1] = []
                n = n - 1
            else:
                i = i + 1
        self.__repo_inscrieri.set_all(lista_inscrieri)

    def modifica_persoana_inscrieri(self, person_id, nume, adresa):
        persoana = Persoana(person_id, nume, adresa)
        lista_inscrieri = self.__repo_inscrieri.get_all()
        i = 0
        n = len(lista_inscrieri)
        while i < n:
            if lista_inscrieri[i].get_persoana().get_person_id() == person_id:
                eveniment = lista_inscrieri[i].get_eveniment()
                inscriere = Inscriere(persoana, eveniment)
                lista_inscrieri[i] = inscriere
            i = i + 1
        self.__repo_inscrieri.set_all(lista_inscrieri)

    def sterge_eveniment_inscrieri(self, event_id):
        # returneaza o copie a listei de inscrieri, fara inscrierile care contin id-ul evenimentului dat
        # event_id - int
        lista_inscrieri = self.__repo_inscrieri.get_all()
        i = 0
        n = len(lista_inscrieri)
        while i < n:
            if lista_inscrieri[i].get_eveniment().get_event_id() == event_id:
                lista_inscrieri[i:i + 1] = []
                n = n - 1
            else:
                i = i + 1
        self.__repo_inscrieri.set_all(lista_inscrieri)

    def modifica_eveniment_inscrieri(self, event_id, data, timp, descriere):
        # returneaza o copie a listei de inscrieri, modificand inscrieriile care contin evenimentul dat, cu noul
        # eveniment
        # eveniment este un obiect de clasa Eveniment
        eveniment = Eveniment(event_id, data, timp, descriere)
        lista_inscrieri = self.__repo_inscrieri.get_all()
        i = 0
        n = len(lista_inscrieri)
        while i < n:
            if lista_inscrieri[i].get_eveniment().get_event_id() == event_id:
                persoana = lista_inscrieri[i].get_persoana()
                inscriere = Inscriere(persoana, eveniment)
                lista_inscrieri[i] = inscriere
            i = i + 1
        self.__repo_inscrieri.set_all(lista_inscrieri)

    def lista_evenimente_persoana(self, persoana):
        # returneaza o lista de evenimente ( de tip [[eveniment1], [eveniment2], ... ] ) la care persoana este inscrisa
        # in obiectul de clasa ListaInscrieri
        lista_inscrieri = self.__repo_inscrieri.get_all()
        lista_evenimente = self.__lista_evenimente_persoana_creeare_recursiv(persoana, lista_inscrieri, [])
        if not lista_evenimente:
            return lista_evenimente
        Sort().bubble_sort(lista_evenimente, key=Eveniment.get_descriere, key2=Eveniment.get_data_datetime)
        return lista_evenimente

    def __lista_evenimente_persoana_creeare_recursiv(self, persoana, lista_inscrieri, lista_evenimente):
        # ----------------------------------------------recursiv----------------------------------------------------
        # returneaza o lista de evenimente la care este inscrisa persoana in lista de inscrieri
        # persoana este un obiect de clasa Persoana
        if lista_inscrieri == []:
            return lista_evenimente
        if lista_inscrieri[0].get_persoana() == persoana:
            lista_evenimente.append(lista_inscrieri[0].get_eveniment())
        return self.__lista_evenimente_persoana_creeare_recursiv(persoana, lista_inscrieri[1:], lista_evenimente)

    def persoane_multe_inscrieri(self):
        # returneaza o lista de dto-s de frecventa de tipul: [dto1, dto2,...]
        # unde: dto.get_id - persoana_id ; dto.get_nr_inscrieri - nr_inscrieri_persoana,
        # pentru persoanele inscrise in obiectul de clasa RepositoryPersoane,
        # unde lista este sortata descrescator dupa numarul de inscrieri ale unei persoane
        lista_inscrieri = self.__repo_inscrieri.get_all()
        lista_frecventa = self.__persoane_multe_inscrieri_frecventa_recursiv(lista_inscrieri, [])
        repo_persoane = self.__repo_persoane.get_all()
        lista_frecventa = self.__persoane_multe_inscrieri_adauga_persoane_fara_evenimente_recursiv(repo_persoane, lista_frecventa)
        lista_frecventa = self.__freq_list_to_id_frecventa_dto(lista_frecventa)
        Sort().bubble_sort(lista_frecventa, key=IdFrecventaDTO.get_nr_inscrieri, reverse=True)
        return lista_frecventa

    def __persoane_multe_inscrieri_frecventa_recursiv(self, lista_inscrieri, lista_frecventa):
        # ----------------------------------------------recursiv----------------------------------------------------
        # realizeaza o lista de frecventa cu persoanele care participa la cel putin un eveniment
        # ( [[persoana][nr_inscrieri_persoana], ... ] )
        # daca un element exista deja in lista, ii este incrementata frecventa
        # daca nu exista, este adaugat si frecventa este setata la 1
        # lista_inscrieri = obiect de tip ListaInscrieri
        if not lista_inscrieri:
            return lista_frecventa
        person_id = lista_inscrieri[0].get_persoana().get_person_id()
        el = self.__element_in_frecventa(person_id, lista_frecventa)
        if el != -1:
            lista_frecventa[el][1] += 1
        else:
            lista_frecventa.append([person_id, 1])
        return self.__persoane_multe_inscrieri_frecventa_recursiv(lista_inscrieri[1:], lista_frecventa)

    def __persoane_multe_inscrieri_adauga_persoane_fara_evenimente_recursiv(self, repo_persoane, lista_frecventa):
        # ----------------------------------------------recursiv----------------------------------------------------
        # adauga in lista de frecventa persoanele care nu participa la nici un eveniment
        # freq - lista de frecventa de tipul: [[persoana][nr_inscrieri_persoana], ... ]
        if not repo_persoane:
            return lista_frecventa
        if self.__element_in_frecventa(repo_persoane[0].get_person_id(), lista_frecventa) == -1:
            lista_frecventa.append([repo_persoane[0].get_person_id(), 0])
        return self.__persoane_multe_inscrieri_adauga_persoane_fara_evenimente_recursiv(repo_persoane[1:],
                                                                                        lista_frecventa)


    def evenimente_multe_inscrieri(self):
        # returneaza o lista de frecventa de tipul: [[eveniment][nr_inscrieri_eveniment], ... ] pentru persoanele
        # inscrise in obiectul de clasa RepositoryEvenimente
        lista_inscrieri = self.__repo_inscrieri.get_all()
        lista_frecventa = self.__evenimente_multe_inscrieri_frecventa_recursiv(lista_inscrieri, [])
        repo_evenimente = self.__repo_evenimente.get_all()
        lista_frecventa = self.__evenimente_multe_inscrieri_adauga_evenimente_fara_persoane_recursiv(repo_evenimente, lista_frecventa)
        lista_frecventa = self.__freq_list_to_id_frecventa_dto(lista_frecventa)
        Sort().comb_sort(lista_frecventa, key=IdFrecventaDTO.get_nr_inscrieri, reverse=True)
        return lista_frecventa

    def __evenimente_multe_inscrieri_frecventa_recursiv(self, lista_inscrieri, lista_frecventa):
        # ----------------------------------------------recursiv----------------------------------------------------
        # realizeaza o lista de frecventa cu evenimentele care au cel putin un participant
        # ( [[id_eveniment, nr_inscrieri_eveniment], ... ] )
        # daca un element exista deja in lista, ii este incrementata frecventa
        # daca nu exista, este adaugat si frecventa este setata la 1
        # lista_inscrieri = obiect de tip ListaInscrieri

        if not lista_inscrieri:
            return lista_frecventa
        event_id = lista_inscrieri[0].get_eveniment().get_event_id()
        el = self.__element_in_frecventa(event_id, lista_frecventa)
        if el != -1:
            lista_frecventa[el][1] += 1
        else:
            lista_frecventa.append([event_id, 1])
        return self.__evenimente_multe_inscrieri_frecventa_recursiv(lista_inscrieri[1:], lista_frecventa)

    def __evenimente_multe_inscrieri_adauga_evenimente_fara_persoane_recursiv(self, repo_evenimente, lista_frecventa):
        # ----------------------------------------------recursiv----------------------------------------------------
        # adauga in lista de frecventa persoanele care nu participa la nici un eveniment
        # freq - lista de frecventa de tipul: [[eveniment][nr_inscrieri_eveniment], ... ]

        if not repo_evenimente:
            return lista_frecventa
        if self.__element_in_frecventa(repo_evenimente[0].get_event_id(), lista_frecventa) == -1:
            lista_frecventa.append([repo_evenimente[0].get_event_id(), 0])
        return self.__evenimente_multe_inscrieri_adauga_evenimente_fara_persoane_recursiv(repo_evenimente[1:], lista_frecventa)

    def get_inscrieri(self):
        # returneaza lista de liste de tip [[persoana,eveniment], ... ], unde persoana si eveniment sunt obiecte de
        # clasa Persoana, respectiv Eveniment
        return self.__repo_inscrieri.get_all()

    def __element_in_frecventa(self, id, freq):
        # verifica daca elementul (persoana / evenimentul) de id-ul dat exista deja in lista de frecventa
        # returneaza -1 daca nu exista sau pozitia unde se gaseste daca exista
        # id - int, freq - lista de frecventa de tipul:
        # [[persoana / eveniment][nr_inscrieri_persoana / nr_inscrieri_persoana ], ... ]
        for i in range(len(freq)):
            if id == freq[i][0]:
                return i
        return -1

    def __freq_list_to_id_frecventa_dto(self, lista_frecventa):
        # transforma o lista de frecventa de tipul: [[persoana_id, nr_inscrieri_persoana], ... ] intr-o lista de dto:
        # [dto1, dto2,...] unde: dto.get_person_id - persoana_id ; dto.get_nr_inscrieri - nr_inscrieri_persoana
        lista = []
        for i in range(len(lista_frecventa)):
            lista.append(IdFrecventaDTO(lista_frecventa[i][0], lista_frecventa[i][1]))
        return lista