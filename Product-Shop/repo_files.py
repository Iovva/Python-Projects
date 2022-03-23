from repo_memory import RepoProduse
from domain import Produs

class RepositoryProduseFiles(RepoProduse):

    def __init__(self, filename):
        # initializeaza obiectul cu filename-ul fisierului .txt de produse, de tip string
        self.__filename = filename
        RepoProduse.__init__(self)

    def __citeste_din_fisier(self):
        # citeste toate randurile din fisier, separa valorile produselor si le baga in repository
        with open(self.__filename, "r") as f:
            self._elemente = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(";")
                    produs = Produs(int(parts[0]), parts[1], int(parts[2]))
                    self._elemente.append(produs)

    def __append_fisier(self, produs):
        # adauga un rand noi un fisierul .txt repository care contine valorile produsului
        with open(self.__filename, "a") as f:
            id = str(produs.get_id())
            denumire = produs.get_denumire()
            pret = str(produs.get_pret())       # nu stiu sigur
            f.write(id + ";" + denumire + ";" + pret + "\n")

    def __scrie_fisier(self):
        # rescrie tot continutul fisierului cu valorile persoanelor din repository
        with open(self.__filename, "w") as f:
            for produs in self._elemente:
                id = str(produs.get_id())
                denumire = produs.get_denumire()
                pret = str(produs.get_pret())       # nu stiu sigur
                f.write(id + ";" + denumire + ";" + pret + "\n")

    def adauga(self, produs):
        # actualizeaza repository-ul cu valorile din fisier
        # primeste un obiect de clasa Produs, il adauga in repository, dar si in fisierul text
        self.__citeste_din_fisier()
        RepoProduse.adauga(self, produs)
        self.__append_fisier(produs)

    def sterge(self, cif):
        # actualizeaza repository-ul cu valorile din fisier
        # sterge obiectele ale caror id-uri contin cifra data, atat din repository, cat si din fisierul text
        # returneaza numarul de elemente sterse
        self.__citeste_din_fisier()
        sterse = RepoProduse.sterge(self, cif)
        self.__scrie_fisier()
        return sterse

    def get_all(self):
        # actualizeaza repository-ul cu valorile din fisier
        # returneaza lista completa de obiecte Produs din repo
        self.__citeste_din_fisier()
        return RepoProduse.get_all(self)
