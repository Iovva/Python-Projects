class LucruMemeorieFisier:
    def __init__(self):
        # la intializare obiectului, solicita de la utiliator daca doreste sa lucreze cu fisiere sau exclusiv in
        # memorie
        self.__fisier = True
        print("Doriti sa lucrati cu fisiere sau strict in memorie?")
        while True:
            try:
                cmd = input()
                if cmd.lower() == "memorie":
                    self.__fisier = False
                    break
                if cmd.lower() == "fisiere":
                    break
                assert False
            except AssertionError:
                print("Introduceti 'memorie' sau 'fisiere'!")

    def check(self):
        # returneaza True, daca se lucreaza cu fisiere, respectiv False, in caz contrar
        return self.__fisier


class CreeareFisiere:
    def __init__(self):
        # la initializarea obiectului, creeaza un fisier care contine text-file-uri de persoane, inscrieri si
        # evenimente, daca nu exista deja
        # adauga un textfile de copyright
        import os
        path = os.path.dirname(os.path.realpath(__file__))
        path = path[:-14]
        path += "!Fisiere!"
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
        try:
            f = open(path + "\persoane.txt", "r")
            f.close()
        except:
            f = open(path + "\persoane.txt", "w")
            f.close()
        try:
            f = open(path + "\evenimente.txt", "r")
            f.close()
        except FileNotFoundError:
            f = open(path + "\evenimente.txt", "w")
            f.close()
        try:
            f = open(path + "\inscrieri.txt", "r")
            f.close()
        except FileNotFoundError:
            f = open(path + "\inscrieri.txt", "w")
            f.close()

        self.__path = path

        path = path[:-10]
        try:
            f = open(path + "\copyright.txt", "r")
            f.close()
        except FileNotFoundError:
            f = open(path + "\copyright.txt", "w")
            f.write("IOWA 2020®")

    def path(self):
        return self.__path
