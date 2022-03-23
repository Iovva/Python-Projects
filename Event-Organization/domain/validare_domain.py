from exceptions.exceptii_domain import EvenimentEroare, PersoanaEroare


class ValidatorPersoana:

    def check(self, persoana):
        # valideaza daca obiectul primit, de clasa Persoana, are datele valide
        # verifica daca id-ul este mai mare ca 0, si daca numele si descrierea exista
        # in cazurile eronate, afiseazamesajul corespunzator
        error = ""

        if persoana.get_person_id() < 0:
            error += "ID persoana invalid!\n"

        if persoana.get_nume() == "":
            error += "Nume invalid!\n"

        if persoana.get_adresa() == "":
            error += "Adresa invalida!\n"

        if len(error) > 0:
            raise PersoanaEroare(error)


class ValidatorEveniment:

    def data_corecta(self, data):
        # functia verifica daca data are formatul corect si este reala
        # data primita este string
        try:
            z1 = int(data[0])
            z2 = int(data[1])
            l1 = int(data[3])
            l2 = int(data[4])
            a1 = int(data[6])
            a2 = int(data[7])
            a3 = int(data[8])
            a4 = int(data[9])
        except ValueError:
            return False
        except IndexError:
            return False

        if data[2] != "." or data[5] != ".":
            return False

        zi = z1 * 10 + z2
        if zi < 1:
            return False

        luna = l1 * 10 + l2
        if luna > 12 or luna < 1:
            return False

        an = a1 * 1000 + a2 * 100 + a3 * 10 + a4
        if an < 1:
            return False


        if (luna == 1 or luna == 3 or luna == 5 or luna == 7 or luna == 8 or luna == 10 or luna == 11) and zi > 31:
            return False
        elif luna == 2 and zi > 29:
            return False
        elif luna == 2 and zi == 29:
            if not (an % 4 == 0 and an % 100 != 0 or an % 400 == 0):
                return False
        elif zi > 30:
            return False

        return True

    def timp_corect(self, timp):
        # functia verifica daca timpul are formatul corect si este real
        # timpul primit este string
        try:
            h1 = int(timp[0])
            h2 = int(timp[1])
            m1 = int(timp[3])
            m2 = int(timp[4])
        except ValueError:
            return False
        except IndexError:
            return False

        if timp[2] != ":":
            return False

        ora = h1 * 10 + h2
        if ora > 23 or ora < 0:
            return False

        minut = m1 * 10 + m2
        if minut > 59 or minut < 0:
            return False

        return True

    def check(self, eveniment):
        # valideaza daca obiectul primit, de clasa Eveniment, are datele valide
        # verifica daca id-ul este mai mare ca 0, daca descrierea exista si daca data si timpul au formatul corect
        # si sunt reale
        # ( ora: hh:mm ; data: zz.ll.aaaa )
        # in cazurile eronate, afiseaza mesajul corespunzator
        error = ""

        if eveniment.get_event_id() < 0:
            error += "ID eveniment invalid!\n"

        data = eveniment.get_data()
        if not self.data_corecta(data):
            error += "Data invalida!\n"

        timp = eveniment.get_timp()
        if not self.timp_corect(timp):
            error += "Ora invalida!\n"

        if eveniment.get_descriere() == "":
            error += "Descriere invalida!\n"

        if len(error) > 0:
            raise EvenimentEroare(error)
