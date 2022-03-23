from exceptions import RepoEroare

class UI:

    def __init__(self, service):
        self.__service = service
        self.__filtru = [None, None]
        self.__lista_filtrata = []
        self.__comenzi = {
            "1": self.__ui_adauga,
            "2": self.__ui_sterge,
            "3": self.__ui_filtru,
        }

    def __ui_adauga(self):
        # primeste de la utilizator detaliile produsului, si lanseaza operatia de adaos a produsului, din service
        # daca filtrul este activat, se afiseaza, dupa adaos, produsele care corespund filtrului,
        # iar daca nu, se semnaleaza ca nu a fost activat
        id = int(input("Introduceti id-ul:"))
        denumire = input("Introduceti denumirea:")
        pret = int(input("Introduceti pretul:"))
        self.__service.adauga(id, denumire, pret)
        self.__lista_filtrata = self.__service.filtru(self.__filtru)
        self.__printare_lista_filtrata()

    def __ui_sterge(self):
        # primeste de la utilizator o cifra, si lanseaza operatia de stergere a produselor, a caror id-uri contin cifra
        # data, din service
        # daca filtrul este activat, se afiseaza, dupa stergere, produsele care corespund filtrului,
        # iar daca nu, se semnaleaza ca nu a fost activat
        cifra = int(input("Introduceti o cifra, urmand sa fie sterse toate produsele care au acea cifra in id:"))
        sterse = self.__service.sterge(cifra)
        print("Au fost sterse ", sterse, " produse!")
        self.__lista_filtrata = self.__service.filtru(self.__filtru)
        self.__printare_lista_filtrata()

    def __ui_filtru(self):
        # primeste de la utilizator un text si un numar, si lanseaza operatia de setare a filtrului din service
        # se afiseaza, dupa setarea filtrului produsele care corespund filtrului,
        text = input("Introduceti textul:")
        numar = int(input("Introduceti numarul:"))
        self.__filtru = [text, numar]
        self.__lista_filtrata = self.__service.filtru(self.__filtru)
        self.__printare_lista_filtrata()

    def __printare_lista_filtrata(self):
        # printeaza lista filtrata, dupa orice comanda, daca a fost setat un filtru, sau trasmite ca nu a fost setat
        # un filtru, daca este cazul
        if self.__filtru == [None, None]:
            print("\nNu a fost pus nici un filtru inca!\n")
            return
        if self.__lista_filtrata == []:
            print("\nNu exista produse care se incadreaza la filtrele puse!\n")
            return
        print("\nLista filtrata:\n")
        for i in range(len(self.__lista_filtrata)):
            print(self.__lista_filtrata[i].get_id(), ";", self.__lista_filtrata[i].get_denumire(), ";",
                  self.__lista_filtrata[i].get_pret(), "\n")

    def run(self):
        #main-ul
        while True:
            cmd = input("Introduceti comanda:")
            if cmd == "exit":
                return
            try:
                self.__comenzi[cmd]()
            except KeyError:
                print("Comanda invalida")
            except RepoEroare as RE:
                print(RE)
                self.__lista_filtrata = self.__service.filtru(self.__filtru)
                self.__printare_lista_filtrata()
