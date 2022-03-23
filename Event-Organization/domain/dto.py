class IdFrecventaDTO(object):
    def __init__(self, id, nr_inscrieri):
        # initializeaza obiectul cu persoana_id si nr_inscrieri_persoana - int
        self.__id = id
        self.__nr_inscrieri = nr_inscrieri

    def get_id(self):
        # returneaza id-ul persoanei
        return self.__id

    def get_nr_inscrieri(self):
        # returneaza numarul de inscrieri ale persoanei
        return self.__nr_inscrieri


