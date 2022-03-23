from exceptions.exceptii_domain import PersoanaEroare, EvenimentEroare
from exceptions.exceptii_infrastructure import RepositoryEroare

class UI:

    def __init__(self, service_persoane, service_evenimente, service_inscrieri):
        self.__service_persoane = service_persoane
        self.__service_evenimente = service_evenimente
        self.__service_inscrieri = service_inscrieri
        self.__comenzi = {
            "debug": self.__debug,
            "adauga_persoana": self.__ui_adauga_persoana,
            "sterge_persoana": self.__ui_sterge_persoana,
            "modifica_persoana": self.__ui_modifica_persoana,
            "cauta_persoana": self.__ui_cauta_persoana,
            "print_persoane": self.__ui_print_persoane,
            "adauga_eveniment": self.__ui_adauga_eveniment,
            "sterge_eveniment": self.__ui_sterge_eveniment,
            "modifica_eveniment": self.__ui_modifica_eveniment,
            "cauta_eveniment": self.__ui_cauta_eveniment,
            "print_evenimente": self.__ui_print_evenimente,
            "adauga_inscriere": self.__ui_adauga_inscriere,
            "sterge_inscriere": self.__ui_sterge_inscriere,
            "rapoarte_inscrieri": self.__ui_rapoarte_inscrieri,
            "print_inscrieri": self.__ui_print_inscrieri,
            "help": self.__ui_help,
            "0": self.__debug,
            "1": self.__ui_adauga_persoana,
            "2": self.__ui_sterge_persoana,
            "3": self.__ui_modifica_persoana,
            "4": self.__ui_cauta_persoana,
            "5": self.__ui_print_persoane,
            "6": self.__ui_adauga_eveniment,
            "7": self.__ui_sterge_eveniment,
            "8": self.__ui_modifica_eveniment,
            "9": self.__ui_cauta_eveniment,
            "10": self.__ui_print_evenimente,
            "11": self.__ui_adauga_inscriere,
            "12": self.__ui_sterge_inscriere,
            "13": self.__ui_rapoarte_inscrieri,
            "14": self.__ui_print_inscrieri,
            "15": self.__ui_help
        }
        self.__comenzi_rapoarte = {
            "lista_evenimente_persoana": self.__ui_lista_evenimente_persoana,
            "persoane_multe_inscrieri": self.__ui_persoane_multe_inscrieri,
            "evenimente_multe_inscrieri": self.__ui_evenimente_multe_inscrieri,
            "evenimente_inscrieri_interval": self.__ui_evenimente_inscrieri_interval,
            "help": self.__ui_rapoarte_inscrieri_help,
            "1": self.__ui_lista_evenimente_persoana,
            "2": self.__ui_persoane_multe_inscrieri,
            "3": self.__ui_evenimente_multe_inscrieri,
            "4": self.__ui_evenimente_inscrieri_interval,
        }

    def __debug(self):
        self.__service_persoane.adauga_persoana(1, "das", "da")
        self.__service_persoane.adauga_persoana(2, "das", "da")
        self.__service_evenimente.adauga_eveniment(1, "01.01.2023", "00:00", "a")
        self.__service_evenimente.adauga_eveniment(2, "10.01.2022", "00:00", "a")
        self.__service_evenimente.adauga_eveniment(3, "09.10.2022", "00:00", "aa")
        self.__service_evenimente.adauga_eveniment(4, "09.11.2021", "00:00", "aa")
        self.__service_evenimente.adauga_eveniment(5, "13.10.2021", "00:00", "aaa")
        self.__service_evenimente.adauga_eveniment(6, "09.10.2021", "00:00", "aaa")
        self.__service_evenimente.adauga_eveniment(7, "10.10.2021", "00:00", "aaaaz")
        self.__service_evenimente.adauga_eveniment(8, "10.11.2021", "00:00", "aaaa")
        self.__service_inscrieri.adauga_inscriere(1, 1)
        self.__service_inscrieri.adauga_inscriere(1, 2)
        self.__service_inscrieri.adauga_inscriere(1, 3)
        self.__service_inscrieri.adauga_inscriere(1, 4)
        self.__service_inscrieri.adauga_inscriere(1, 5)
        self.__service_inscrieri.adauga_inscriere(1, 6)
        self.__service_inscrieri.adauga_inscriere(1, 7)
        self.__service_inscrieri.adauga_inscriere(1, 8)
        self.__service_inscrieri.adauga_inscriere(2, 1)
        self.__service_inscrieri.adauga_inscriere(2, 2)
        print("Elemente adaugate!")

    def __ui_initializare(self):
        # functia are loc doar la inceputul programului, daca nu exista nici o persoana si nici un eveniment
        # primeste de la utilizator un string
        # daca string-ul este 'da', porneste adaosul unor persoane si evenimente aleatorii
        # in caz contrar, este rugat sa reintroduca comanda
        print("Doriti sa initializati programul cu niste persoane si evenimente generate aleatoriu?")
        while True:
            try:
                cmd = input()
                if cmd.lower() == "da":
                    self.__ui_adauga_persoane_random()
                    self.__ui_adauga_evenimente_random()
                    break
                if cmd.lower() == "nu":
                    break
                assert False
            except AssertionError:
                print("Introduceti 'DA' sau 'NU'!")

    def __ui_adauga_persoane_random(self):
        while True:
            try:
                nr_persoane = int(input("Cate persoane doriti sa adaugati?\n"))
                if nr_persoane > 999:
                    print("Maximul este 999!\n")
                else:
                    break
            except ValueError:
                print("Valoarea introdusa trebuie sa fie un numar natural!\n")
        self.__service_persoane.adauga_persoane_random(nr_persoane)

    def __ui_adauga_evenimente_random(self):
        while True:
            try:
                nr_evenimente = int(input("Cate evenimente doriti sa adaugati?\n"))
                if nr_evenimente > 999:
                    print("Maximul este 999!\n")
                else:
                    break
            except ValueError:
                print("Valoarea introdusa trebuie sa fie un numar natural!\n")
        self.__service_evenimente.adauga_evenimente_random(nr_evenimente)

    def __ui_adauga_persoana(self):
        # preia de la utilizaotr id-ul, numele si adresa persoanei ce trebuie adaugate
        # lanseaza adaugarea persoanei in repository, daca nu exista deja
        # afiseaza un mesaj daca operatia s-a executat cu succes
        person_id = int(input("Introduceti ID-ul persoanei:"))
        nume = input("Introduceti numele persoanei:")
        adresa = input("Introduceti adresa persoanei:")
        self.__service_persoane.adauga_persoana(person_id, nume, adresa)
        print("Comanda efectuata cu succes!\n")

    def __ui_sterge_persoana(self):
        # preia de la utilizaotr id-ul persoanei ce trebuie stearsa
        # lanseaza stergerea persoanei din repository, daca exista
        # afiseaza un mesaj daca operatia s-a executat cu succes
        person_id = int(input("Introduceti ID-ul persoanei:"))
        self.__service_persoane.sterge_persoana(person_id)
        self.__service_inscrieri.sterge_persoana_inscrieri(person_id)
        print("Comanda efectuata cu succes!\n")

    def __ui_modifica_persoana(self):
        # preia de la utilizator id-ul persoanei ce trebuie modifcata si numele si adresa noua
        # lanseaza modificarea persoanei din repository, daca exista
        # afiseaza un mesaj daca operatia s-a executat cu succes
        person_id = int(input("Introduceti ID-ul persoanei ce trebuie modificata:"))
        nume = input("Introduceti numele nou:")
        adresa = input("Introduceti adresai noua:")
        self.__service_persoane.modifica_persoana(person_id, nume, adresa)
        self.__service_inscrieri.modifica_persoana_inscrieri(person_id, nume, adresa)
        print("Comanda efectuata cu succes!\n")

    def __ui_cauta_persoana(self):
        # preia de la utilizaotr id-ul unei persoane si afiseaza o afiseaza, daca exista
        person_id = int(input("Introduceti ID-ul persoanei cautate:"))
        persoana = self.__service_persoane.cauta_persoana(person_id)
        print("\nPersoana cautata este:\n")
        print("ID:", persoana.get_person_id(), "\n"
                                               "Nume:", persoana.get_nume(), "\n"
                                                                             "Adresa:", persoana.get_adresa(), "\n")

    def __ui_print_persoane(self):
        # afiseaza lista persoanelor
        persoane = self.__service_persoane.get_persoane()
        if len(persoane) == 0:
            print("Nu exista persoane in lista!\n")
            return
        print("Persoanele din lista sunt:")
        for i in range(len(persoane)):
            print(i + 1, ")  ID:", persoane[i].get_person_id(), "\n"
                                                                "     Nume:", persoane[i].get_nume(), "\n"
                                                                                                      "     Adresa:",
                  persoane[i].get_adresa(), "\n"
                  )

    def __ui_adauga_eveniment(self):
        # preia de la utilizaotr id-ul data, timpul si descrierea eveimentului ce trebuie adaugat
        # lanseaza adaugarea evenimentului in repository, daca nu exista deja
        # afiseaza un mesaj daca operatia s-a executat cu succes
        event_id = int(input("Introduceti ID-ul evenimentului:"))
        data = input("Introduceti data evenimentului:")
        timp = input("Introduceti timpul evenimentului:")
        descriere = input("Introduceti descrierea evenimentului:")
        self.__service_evenimente.adauga_eveniment(event_id, data, timp, descriere)
        print("Comanda efectuata cu succes!\n")

    def __ui_sterge_eveniment(self):
        # preia de la utilizaotr id-ul elementului ce trebuie sters
        # lanseaza stergerea evenimentului din repository, daca exista
        # afiseaza un mesaj daca operatia s-a executat cu succes
        event_id = int(input("Introduceti ID-ul evenimentului:"))
        self.__service_evenimente.sterge_eveniment(event_id)
        self.__service_inscrieri.sterge_eveniment_inscrieri(event_id)
        print("Comanda efectuata cu succes!\n")

    def __ui_modifica_eveniment(self):
        # preia de la utilizator id-ul evenimentului ce trebuie modifcat si data, timpul si descrierea noua
        # lanseaza modificarea evenimentului din repository, daca exista
        # afiseaza un mesaj daca operatia s-a executat cu succes
        event_id = int(input("Introduceti ID-ul evenimentului ce trebuie modificat:"))
        data = input("Introduceti data noua:")
        timp = input("Introduceti timpul nou:")
        descriere = input("Introduceti descrierea noua:")
        self.__service_evenimente.modifica_eveniment(event_id, data, timp, descriere)
        self.__service_inscrieri.modifica_eveniment_inscrieri(event_id, data, timp, descriere)
        print("Comanda efectuata cu succes!\n")

    def __ui_cauta_eveniment(self):
        # preia de la utilizaotr id-ul unui eveniment si afiseaza evenimentul, daca exista
        event_id = int(input("Introduceti ID-ul evenimentului cautat:"))
        eveniment = self.__service_evenimente.cauta_eveniment(event_id)
        print("\nEvenimentul cautat este:\n")
        print("ID:", eveniment.get_event_id(), "\n"
                                               "Data:", eveniment.get_data(), "\n"
                                                                              "Ora:", eveniment.get_timp(), "\n"
                                                                                                            "Descriere:",
              eveniment.get_descriere(), "\n"
              )

    def __ui_print_evenimente(self):
        # afiseaza lista evenimentelor
        evenimente = self.__service_evenimente.get_evenimente()
        if len(evenimente) == 0:
            print("Nu exista evenimente in lista!\n")
            return
        print("Evenimentele din lista sunt:\n")
        for i in range(len(evenimente)):
            print(i + 1, ") ID:", evenimente[i].get_event_id(), "\n"
                                                                "    Data:", evenimente[i].get_data(), "\n"
                                                                                                       "    Ora:",
                  evenimente[i].get_timp(), "\n"
                                            "    Descriere:", evenimente[i].get_descriere(), "\n"
                  )

    def __ui_adauga_inscriere(self):
        # preia de la utilizator id-ul persoanei si id-ul evenimentului ce trebuie adaugat in lista inscrierilor
        # lanseaza metoda de inscriere
        # afiseaza un mesaj daca operatia s-a executat cu succes
        person_id = int(input("Introduceti ID-ul persoanei:"))
        event_id = int(input("Introduceti ID-ul evenimentului:"))
        self.__service_inscrieri.adauga_inscriere(person_id, event_id)
        print("Comanda efectuata cu succes!\n")

    def __ui_sterge_inscriere(self):
        # preia de la utilizator id-ul persoanei si id-ul evenimentului din inscrierea ce trebuie stearsa
        # lanseaza metoda de stergere
        # afiseaza un mesaj daca operatia s-a executat cu succes
        person_id = int(input("Introduceti ID-ul persoanei:"))
        event_id = int(input("Introduceti ID-ul evenimentului:"))
        self.__service_inscrieri.sterge_inscriere(person_id, event_id)
        print("Comanda efectuata cu succes!\n")

    def __ui_rapoarte_inscrieri_help(self):
        # afiseaza lista comenzilor pentru rapoartele cu inscrierii
        print("\nRapoarte disponibile:")
        print("1) lista_evenimente_persoana - lista de evenimente la care participa o persoana,\n"
              "                               ordonata alfabetic după descriere, după data")
        print("2) persoane_multe_inscrieri - persoane participante la cele mai multe evenimente")
        print("3) evenimente_multe_inscrieri - primele 20% evenimente cu cei mai mulți participanți\n"
              "                                ( afiseaza: descriere, număr participanți )")
        print(
            "4) evenimente_inscrieri_interval - afiseaza evenimentele la care participa minim A si maxim B persoane,\n"
            "                                   cu A si B date de utilizator.")
        print("5) back - intoarcere la meniul principal")

    def __ui_rapoarte_inscrieri(self):
        # preia de la utilizator comenzi pentru rapoartele cu inscrieri si le executa
        while True:
            cmd = input("Introduceti raportul pe care doriti sa il aflati:\n")
            cmd = cmd.lower()
            if cmd == "back" or cmd == "5":
                return
            if cmd in self.__comenzi_rapoarte:
                try:
                    self.__comenzi_rapoarte[cmd]()
                except RepositoryEroare as RE:
                    print(RE)
                except ValueError:
                    print("Valoarea introdusa trebuie sa fie un numar natural!\n")
            else:
                print("Comanda invalida!")
                print("Puteti tasta 'help' pentru a accesa lista de comenzi.\n")

    def __ui_lista_evenimente_persoana(self):
        person_id = int(input("Introduceti id-ul persoanei:\n"))
        persoana = self.__service_persoane.cauta_persoana(person_id)
        lista_evenimente = self.__service_inscrieri.lista_evenimente_persoana(persoana)
        print("\nPersoana:\n"
              "ID:", persoana.get_person_id(), "\n"
                                               "Nume:", persoana.get_nume(), "\n"
                                                                             "Adresa:", persoana.get_adresa(), "\n")
        if lista_evenimente == []:
            print("Nu este inscrisa la nici un eveniment!\n")
            return
        print("este inscrisa la evenimentele:\n")
        for i in range(len(lista_evenimente)):
            eveniment = lista_evenimente[i]
            print(i + 1, ") ID:", eveniment.get_event_id(), "\n"
                                                            "    Data:", eveniment.get_data(), "\n"
                                                                                               "    Ora:",
                  eveniment.get_timp(), "\n"
                                        "    Descriere:", eveniment.get_descriere(), "\n")

    def __ui_persoane_multe_inscrieri(self):
        freq = self.__service_inscrieri.persoane_multe_inscrieri()
        if len(freq) == 0:
            print("\nNu exista nici o persoana in lista, adaugati cel putin una pentru a folosi comanda!\n")
            return
        if freq:
            print("\nPersoanele participante la cele mai multe evenimente sunt:\n")
            max_inscrieri = freq[0].get_nr_inscrieri()
            for i in range(0, len(freq)):
                if max_inscrieri != freq[i].get_nr_inscrieri():
                    break
                person_id = freq[i].get_id()
                persoana = self.__service_persoane.cauta_persoana(person_id)
                print(i + 1, ") ID:", persoana.get_person_id(), "\n"
                                                                "    Nume:", persoana.get_nume(), "\n"
                                                                                                  "    Adresa:",
                      persoana.get_adresa(), "\n"
                      )
            if max_inscrieri == 0:
                print("Insa, nici o persoana nu este inscrisa inca la un eveniment.\n")
            else:
                print("avand '", max_inscrieri, "' eveniment(e) la care participa.\n")

    def __ui_evenimente_multe_inscrieri(self):
        # lanseaza preluarea liste de inscrieri, realizarea unei lista de frecventa pentru elemente, sortarea
        # descrescatoare a listei, adaugarea in lista de frecventa a elementelor care nu apar deloc si
        # afisarea primelor 20% evenimente cu cei mai multi participanti
        freq = self.__service_inscrieri.evenimente_multe_inscrieri()
        if len(freq) == 0:
            print("\nNu exista nici un eveniment in lista, adaugati cel putin 5 pentru a folosi comanda!\n")
            return
        if len(freq) >= 5:
            print("\nPrimele 20% evenimente cu cei mai mulți participanti sunt:\n")
            for i in range(0, len(freq) // 5):
                event_id = freq[i].get_id()
                eveniment = self.__service_evenimente.cauta_eveniment(event_id)
                print(i + 1, ") ID:", eveniment.get_event_id(), "\n"
                                                                "    Data:", eveniment.get_data(), "\n"
                                                                                                   "    Ora:",
                      eveniment.get_timp(), "\n"
                                            "    Descriere:", eveniment.get_descriere(), "\n"
                                                                                         "    cu '", freq[i].get_nr_inscrieri(),
                      "' participant(i).\n")
        else:
            print("Pentru a folosi aceasta comanda, mai adaugati cel putin '", 5 - len(freq), "' evenimente!\n")

    def __ui_evenimente_inscrieri_interval(self):
        a = int(input("Introduceti numarul minim de persoane participante la eveniment:\n"))
        b = int(input("Introduceti numarul minim de persoane participante la eveniment:\n"))
        if b < a:
            print("Primul numar introdus trebuie sa fie mai mic decat al doilea!\n")
            return
        freq = self.__service_inscrieri.evenimente_multe_inscrieri()
        if len(freq) == 0:
            print("Nu exista nici un eveniment in lista!")
            return
        ok = 0
        j = 1
        print("Evenimentele care au cel putin' ", a, " 'si cel mult' ", b, " 'persoane sunt:\n")
        for i in range(0, len(freq)):
            if a <= freq[i].get_nr_inscrieri() <= b:
                ok = 1
                event_id = freq[i].get_id()
                eveniment = self.__service_evenimente.cauta_eveniment(event_id)
                print(j, ") ID:", eveniment.get_event_id(), "\n"
                                                            "    Data:", eveniment.get_data(), "\n"
                                                                                               "    Ora:",
                      eveniment.get_timp(), "\n"
                                            "    Descriere:", eveniment.get_descriere(), "\n"
                                                                                         "    cu '", freq[i].get_nr_inscrieri(),
                      "' participant(i).\n")
        if ok == 0:
            print("Nu exista astfel de elemente!\n")

    def __ui_print_inscrieri(self):
        # afiseaza lista persoanelor inscrise la evenimente
        inscrieri = self.__service_inscrieri.get_inscrieri()
        if len(inscrieri) == 0:
            print("Nu exista persoana inscrise la evenimente!\n")
            return
        for i in range(len(inscrieri)):
            persoana = inscrieri[i].get_persoana()
            eveniment = inscrieri[i].get_eveniment()
            print(i + 1, ") Persoana:")
            print("    ID:", persoana.get_person_id(), "\n"
                                                       "    Nume:", persoana.get_nume(), "\n"
                                                                                         "    Adresa:",
                  persoana.get_adresa()
                  )
            print("este inscrisa la evenimentul:")
            print("    ID:", eveniment.get_event_id(), "\n"
                                                       "    Data:", eveniment.get_data(), "\n"
                                                                                          "    Ora:",
                  eveniment.get_timp(), "\n"
                                        "    Descriere:", eveniment.get_descriere(), "\n"
                  )

    def __ui_help(self):
        # afiseaza lista comenzilor
        print("Comenzi disponibile:")
        print("1) adauga_persoana - adauga o persoana in lista")
        print("2) sterge_persoana - sterge o persoana din lista")
        print("3) modifica_persoana - modifica o persoana din lista")
        print("4) cauta_persoana - afiseaza o persoana din lista")
        print("5) print_persoane - afiseaza toate persoanele din lista")
        print("6) adauga_eveniment - adauga un eveniment in lista")
        print("7) sterge_eveniment - sterge un eveniment din lista")
        print("8) modifica_eveniment - modifica un eveniment din lista")
        print("9) cauta eveniment - afiseaza un eveniment din lista")
        print("10) print_evenimente - afiseaza toate evenimentele din lista")
        print("11) adauga_inscriere - inscrie o persoana la un eveniment")
        print("12) sterge_inscriere - sterge inscrierea unei persoane la un eveniment")
        print("13) rapoarte_inscrieri - comenzi de afisare a rapoartelor pentru persoanele inscrise la evenimente")
        print("14) print_inscrieri - afiseaza lista persoanelor inscrise")
        print("15) exit - inchide programul\n")

    def run(self):
        # preia de la utilizator comenzi si le executa
        # afiseaza erori ce pot aparea pe baza datelor introduse de utilizator

        if self.__service_persoane.get_persoane() == [] and self.__service_evenimente.get_evenimente() == []:
            self.__ui_initializare()

        while True:
            cmd = input("Introduceti o comanda:\n")
            cmd = cmd.lower()
            print()
            if cmd == "exit" or cmd == "15":
                print("La revedere!")
                return
            if cmd in self.__comenzi:
                try:
                    self.__comenzi[cmd]()
                except PersoanaEroare as PE:
                    print(PE)
                except EvenimentEroare as EE:
                    print(EE)
                except RepositoryEroare as RE:
                    print(RE)
                except ValueError:
                    print("Valoarea introdusa trebuie sa fie un numar natural!\n")
            else:
                print("Comanda invalida!")
                print("Puteti tasta 'help' pentru a accesa lista de comenzi.\n")
