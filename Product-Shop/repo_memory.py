from exceptions import RepoEroare

class RepoProduse:

    def __init__(self):
        self._elemente = []

    def adauga(self, produs):
        # primeste un obiect de clasa Produs, il adauga in repository
        for i in range(len(self._elemente)):
            if produs.get_id() == self._elemente[i].get_id():
                raise RepoEroare("Exista deja un produs cu id-ul dat!")
        self._elemente.append(produs)

    def sterge(self, cif):
        # sterge obiectele ale caror id-uri contin cifra data
        # returneaza numarul de elemente sterse
        sterse = 0
        ok_sterse = 0
        while ok_sterse == 0:
            ok_sterse = 1
            numere = len(self._elemente)
            for i in range(numere):
                nr = self._elemente[i].get_id()
                ok = 1
                while nr > 0:
                    if (nr % 10) == cif:
                        ok = 0
                        break
                    nr = nr//10
                if ok == 0:
                    sterse += 1
                    del self._elemente[i]
                    ok_sterse = 0
                    break
        return sterse

    def get_all(self):
        # returneaza lista completa de obiecte Produs din repo
        return self._elemente[:]
