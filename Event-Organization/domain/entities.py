import datetime

class Persoana:

    def __init__(self, person_id, nume, adresa):
        # initializeaza obiectul cu un id - int si nume, adresa - string
        self.__person_id = person_id
        self.__nume = nume
        self.__adresa = adresa

    def get_person_id(self):
        # returneaza id-ul persoanei
        return self.__person_id

    def get_nume(self):
        # returneaza numele
        return self.__nume

    def get_adresa(self):
        # returneaza adresa
        return self.__adresa

    def set_nume(self, nume_new):
        # modifica numele
        self.__nume = nume_new

    def set_adresa(self, adresa_new):
        # modifica adresa
        self.__adresa = adresa_new

    def __str__(self):
        # realizeaza un override pentru functia str
        # muta intr-un string datele din obiect, separate prin " "
        return str(self.__person_id) + " " + self.__nume + " " + self.__adresa

    def __eq__(self, alta_persoana):
        # realizeaza un override pentru functia eq ( == )
        # verifica daca id-ul primei persoane este egal cu al celeilalte
        return self.__person_id == alta_persoana.__person_id


class Eveniment:

    def __init__(self, event_id, data, timp, descriere):
        # initializeaza obiectul cu un id - int, data, timp si descriere - string
        # data are formatul: zz.ll.aaaa
        # ora are formatul: hh:mm
        self.__event_id = event_id
        self.__data = data
        self.__timp = timp
        self.__descriere = descriere

    def get_event_id(self):
        # returneaza id-ul evenimentului
        return self.__event_id

    def get_data(self):
        # returneaza data
        return self.__data

    def get_data_datetime(self):
        z1 = int(self.__data[0])
        z2 = int(self.__data[1])
        l1 = int(self.__data[3])
        l2 = int(self.__data[4])
        a1 = int(self.__data[6])
        a2 = int(self.__data[7])
        a3 = int(self.__data[8])
        a4 = int(self.__data[9])
        zi = z1 * 10 + z2
        luna = l1 * 10 + l2
        an = a1 * 1000 + a2 * 100 + a3 * 10 + a4
        return datetime.datetime(an, luna, zi)

    def get_timp(self):
        # returneaza ora
        return self.__timp

    def get_descriere(self):
        # returneaza descrierea
        return self.__descriere

    def set_data(self, data_new):
        # modifica data
        self.__data = data_new

    def set_timp(self, timp_new):
        # modifica timpul
        self.__timp = timp_new

    def set_descriere(self, descriere_new):
        # modifica descrierea
        self.__descriere = descriere_new

    def __str__(self):
        # realizeaza un override pentru functia str
        # muta intr-un string datele din obiect, separate prin " "
        return str(self.__event_id) + " " + self.__data + " " + self.__timp + " " + self.__descriere

    def __eq__(self, alt_eveniment):
        # realizeaza un override pentru functia eq ( == )
        # verifica daca id-ul primului eveniment este egal cu al celeilalt
        return self.__event_id == alt_eveniment.__event_id


class Inscriere:

    def __init__(self, persoana, eveniment):
        # initializeaza obiectul cu un obiect de clasa persoana si un obiect de clasa eveniment
        self.__persoana = persoana
        self.__eveniment = eveniment

    def get_persoana(self):
        # returneaza obiectul persoana
        return self.__persoana

    def get_eveniment(self):
        # returneaza obiectul eveniment
        return self.__eveniment
