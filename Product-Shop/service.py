from domain import Produs


class Service:

    def __init__(self, repo_produse):
        self.__repo_produse = repo_produse

    def adauga(self, id, denumire, pret):
        # creeaza un obiect de tip produs si il adauga in repo
        produs = Produs(id, denumire, pret)
        self.__repo_produse.adauga(produs)

    def sterge(self, cif):
        # primeste o cifra si sterge toate obiectele ale caror id-uri contin cifra respectiva
        sterse = self.__repo_produse.sterge(cif)
        return sterse

    def filtru(self, filtru):
        # daca filtrul nu a fost inca setat, returneaza o lista_filtrata goala
        # daca s-a setat un filtru, se modifica lista filtrata
        if filtru[0] == None:
            return []

        text = filtru[0]
        numar = filtru[1]

        lista = self.__repo_produse.get_all()

        if text == "" and numar == -1:
            return lista
        lista_filtrata = []

        if text == "":
            for i in range(len(lista)):
                if lista[i].get_pret() < numar:
                    lista_filtrata.append(lista[i])
            return lista_filtrata

        if numar == -1:
            for i in range(len(lista)):
                if lista[i].get_denumire() == text:
                    lista_filtrata.append(lista[i])
            return lista_filtrata

        for i in range(len(lista)):
            if lista[i].get_denumire() == text and  lista[i].get_pret() < numar:
                lista_filtrata.append(lista[i])
        return lista_filtrata


