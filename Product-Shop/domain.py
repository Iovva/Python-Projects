class Produs:

    def __init__(self, id, denumire, pret):
        self.__id = id
        self.__denumire = denumire
        self.__pret = pret

    def set_denumire(self, denumire):
        # seteaza denumirea produsului
        self.__denumire = denumire

    def set_pret(self, pret):
        # seteaza pretul produsului
        self.__pret = pret

    def get_id(self):
        # returneaza id-ul produsului
        return self.__id

    def get_denumire(self):
        # returneaza denumirea produsului
        return self.__denumire

    def get_pret(self):
        # returneaza pretul produsului
        return self.__pret
