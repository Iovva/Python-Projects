from domain.entities import Persoana, Eveniment, Inscriere
from domain.validare_domain import ValidatorPersoana, ValidatorEveniment
from exceptions.exceptii_domain import PersoanaEroare, EvenimentEroare
from exceptions.exceptii_infrastructure import RepositoryEroare
from infrastructure.repository_files import RepositoryPersoaneFiles, RepositoryEvenimenteFiles, RepositoryInscrieriFiles
from infrastructure.repository_memory import RepositoryPersoane, RepositoryEvenimente, RepositoryInscrieri
from service.ctrl import ServicePersoane, ServiceEvenimente, ServiceInscrieri
from sortari.sortari import Sort
import random
import unittest


class TesteEntityPersoana(unittest.TestCase):
    def setUp(self):
        # executa functia inaintea fiecarei functii de test.
        self.person_id = 3
        self.nume = "Marcel"
        self.adresa = "Navodari, nr. 3"
        self.persoana = Persoana(self.person_id, self.nume, self.adresa)

    def testA(self):
        # testeaza metodele de get
        self.assertEqual(self.persoana.get_person_id(), self.person_id)
        self.assertEqual(self.persoana.get_nume(), self.nume)
        self.assertEqual(self.persoana.get_adresa(), self.adresa)

    def testB(self):
        # testeaza metoda de transformare a obiectului in string
        self.assertEqual(str(self.persoana), "3 Marcel Navodari, nr. 3")

    def testC(self):
        # testeaza metodele de set
        self.persoana.set_nume("Napoleon")
        self.assertEqual(self.persoana.get_nume(), "Napoleon")
        self.persoana.set_adresa("Mitropolit Varlam, nr. 56")
        self.assertEqual(self.persoana.get_adresa(), "Mitropolit Varlam, nr. 56")

    def testD(self):
        # testeaza metoda de eq
        alta_persoana = Persoana(self.person_id, "", "asd")
        self.assertEqual(self.persoana, alta_persoana)


class TesteEntityEveniment(unittest.TestCase):
    def setUp(self):
        # executa functia inaintea fiecarei functii de test.
        self.event_id = 57
        self.data = "19.08.2021"
        self.timp = "13:37"
        self.descriere = "Botez regal."
        self.eveniment = Eveniment(self.event_id, self.data, self.timp, self.descriere)

    def testA(self):
        # testeaza metodele de get
        self.assertEqual(self.eveniment.get_event_id(), self.event_id)
        self.assertEqual(self.eveniment.get_data(), self.data)
        self.assertEqual(self.eveniment.get_timp(), self.timp)
        self.assertEqual(self.eveniment.get_descriere(), self.descriere)

    def testB(self):
        # testeaza metoda de transformare a obiectului in string
        self.assertEqual(str(self.eveniment), "57 19.08.2021 13:37 Botez regal.")

    def testC(self):
        # testeaza metodele de set
        self.eveniment.set_data("17.10.2100")
        self.assertEqual(self.eveniment.get_data(), "17.10.2100")
        self.eveniment.set_timp("00:00")
        self.assertEqual(self.eveniment.get_timp(), "00:00")
        self.eveniment.set_descriere("Bufet suedez.")
        self.assertEqual(self.eveniment.get_descriere(), "Bufet suedez.")

    def testD(self):
        # testeaza metodele de eq
        alt_eveniment = Eveniment(self.event_id, "", "", "dada")
        self.assertEqual(self.eveniment, alt_eveniment)


class TesteEntityInscrieri(unittest.TestCase):
    def test(self):
        # testeaza creearea si metodele de get
        person_id = 3
        nume = "Marcel"
        adresa = "Navodari, nr. 3"
        persoana = Persoana(person_id, nume, adresa)
        event_id = 57
        data = "19.08.2021"
        timp = "13:37"
        descriere = "Botez regal."
        eveniment = Eveniment(event_id, data, timp, descriere)
        inscriere = Inscriere(persoana, eveniment)
        self.assertEqual(inscriere.get_persoana(), persoana)
        self.assertEqual(inscriere.get_eveniment(), eveniment)


class TesteValidarePersoana(unittest.TestCase):
    def setUp(self):
        # executa functia inaintea fiecarei functii de test.
        self.validator_persoana = ValidatorPersoana()

    def testA(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru un id invalid
        persoana_gresita = Persoana(-1, "Marcel", "Strada 1")
        self.assertRaisesRegex(PersoanaEroare, "ID persoana invalid!\n",
                               self.validator_persoana.check, persoana_gresita)

    def testB(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru un nume invalid
        persoana_gresita = Persoana(3, "", "Strada 1")
        self.assertRaisesRegex(PersoanaEroare, "Nume invalid!\n",
                               self.validator_persoana.check, persoana_gresita)

    def testC(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o adresa invalid
        persoana_gresita = Persoana(3, "Marcel", "")
        self.assertRaisesRegex(PersoanaEroare, "Adresa invalida!\n",
                               self.validator_persoana.check, persoana_gresita)

    def testD(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o persoana cu toate campurile invalide
        persoana_gresita_total = Persoana(-3, "", "")
        self.assertRaisesRegex(PersoanaEroare, "ID persoana invalid!\nNume invalid!\nAdresa invalida!\n",
                               self.validator_persoana.check, persoana_gresita_total)

    def testE(self):
        # verifica daca validatorul nu ridica o eroare pentru o persoana cu valori valide
        persoana_corecta = Persoana(3, "Marcel", "Strada 1")
        self.assertIsNone(self.validator_persoana.check(persoana_corecta))


class TesteValidareEveniment(unittest.TestCase):
    def setUp(self):
        # executa functia inaintea fiecarei functii de test.
        self.validator_eveniment = ValidatorEveniment()

    def testA(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru un id invalid
        eveniment_gresit = Eveniment(-5, "15.10.2021", "16:23", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "ID eveniment invalid!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testB(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o data invalida
        eveniment_gresit = Eveniment(1, "35.10.2021", "16:30", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "Data invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testC(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o data invalida
        eveniment_gresit = Eveniment(1, "31.09.2021", "16:30", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "Data invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testD(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o data invalida
        eveniment_gresit = Eveniment(1, "00.10.2021", "16:30", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "Data invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testE(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o data invalida
        eveniment_gresit = Eveniment(1, "29.02.2021", "16:30", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "Data invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testF(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o data invalida
        eveniment_gresit = Eveniment(1, "29.02.2100", "16:30", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "Data invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testG(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o data invalida
        eveniment_gresit = Eveniment(1, "30.00.2021", "16:30", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "Data invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testH(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o data invalida
        eveniment_gresit = Eveniment(1, "30.17.2021", "16:30", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "Data invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testI(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o data invalida
        eveniment_gresit = Eveniment(1, "30.10.0000", "16:30", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "Data invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testJ(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o ora invalida
        eveniment_gresit = Eveniment(1, "15.10.2021", "16:3", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "Ora invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testJ1(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o ora invalida
        eveniment_gresit = Eveniment(1, "15.10.202", "16:30", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "Data invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testJ3(self):
        eveniment_gresit = Eveniment(1, "15:10:2020", "16:30", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "Data invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testJ2(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o ora invalida
        eveniment_gresit = Eveniment(1, "30.02.2021", "16:3", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "Ora invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testK(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o ora invalida
        eveniment_gresit = Eveniment(1, "15.10.2021", "sfs", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "Ora invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testL(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o ora invalida
        eveniment_gresit = Eveniment(1, "15.10.2021", "24:00", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "Ora invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testM(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o ora invalida
        eveniment_gresit = Eveniment(1, "15.10.2021", "10:60", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "Ora invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testM1(self):
        eveniment_gresit = Eveniment(1, "15.10.2021", "10.60", "Banchet")
        self.assertRaisesRegex(EvenimentEroare, "Ora invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testN(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru o descriere invalida
        eveniment_gresit = Eveniment(1, "15.10.2021", "10:13", "")
        self.assertRaisesRegex(EvenimentEroare, "Descriere invalida!\n",
                               self.validator_eveniment.check, eveniment_gresit)

    def testO(self):
        # verifica daca validatorul ridica eroarea corespunzatoare pentru un eveniment cu toate campurile invalide
        eveniment_gresita_total = Eveniment(-3, "adsda", "26:13", "")
        self.assertRaisesRegex(EvenimentEroare,
                               "ID eveniment invalid!\nData invalida!\nOra invalida!\nDescriere invalida!\n",
                               self.validator_eveniment.check, eveniment_gresita_total)

    def testP(self):
        # verifica daca validatorul nu ridica o eroare pentru o persoana cu valori valide
        eveniment_corect = Eveniment(1, "12.12.2012", "10:13", "adsads")
        self.assertIsNone(self.validator_eveniment.check(eveniment_corect))


class TesteRepoPersoaneMemory(unittest.TestCase):
    def setUp(self):
        # executa functia inaintea fiecarei functii de test.
        self.repository_persoane = RepositoryPersoane()
        self.person_id = 3
        self.nume = "Mirel Marcel"
        self.adresa = "Str Eris, Nr. 3"
        self.persoana = Persoana(self.person_id, self.nume, self.adresa)

    def testA(self):
        # verifica daca, fara sa adauge o persoana, repository-ul de persoane este gol
        self.assertEqual(len(self.repository_persoane), 0)

    def testB(self):
        # verifica adaugarea corecta a unei persoane
        self.repository_persoane.adauga(self.persoana)
        self.assertEqual(len(self.repository_persoane), 1)

    def testC(self):
        self.repository_persoane.adauga(self.persoana)
        # verifica daca, in urma adaugarii unei persoane cu un id deja rezervat, ridica eroarea corespunzatoare
        persoana = Persoana(self.person_id, "dadsa", "31132")
        self.assertRaisesRegex(RepositoryEroare, "Exista deja o persoana cu ID-ul specificat!\n",
                               self.repository_persoane.adauga, persoana)

    def testD(self):
        # testeaza daca functia de cautare a unei persoane returneaza persoana corecta
        self.repository_persoane.adauga(self.persoana)
        persoana_gasita = self.repository_persoane.cauta_dupa_id(self.person_id)
        self.assertEqual(persoana_gasita.get_person_id(), 3)
        self.assertEqual(persoana_gasita.get_nume(), "Mirel Marcel")
        self.assertEqual(persoana_gasita.get_adresa(), "Str Eris, Nr. 3")

    def testE(self):
        # testeaza daca functia de cautare ridica exceptia corecta, in cazul in care nu exista persoana data in repo
        self.repository_persoane.adauga(self.persoana)
        self.assertRaisesRegex(RepositoryEroare, "Nu exista o persoana cu ID-ul specificat!\n",
                               self.repository_persoane.cauta_dupa_id, 7)

    def testF(self):
        # testeaza daca functia de modificare ridica exceptia corecta, in cazul in care nu exista persoana data in repo
        self.repository_persoane.adauga(self.persoana)
        persoana_modifcata = Persoana(14, "Mocanu Emilian", "asddas")
        self.assertRaisesRegex(RepositoryEroare, "Nu exista o persoana cu ID-ul specificat!\n",
                               self.repository_persoane.modifica, persoana_modifcata
                               )

    def testG(self):
        # verifica daca functia de get_all returneaza corect, sub forma unei liste de obicete, toate persoanele din repo
        self.repository_persoane.adauga(self.persoana)
        persoana_modificata = Persoana(3, "Mocanu Emilian", "asddas")
        self.repository_persoane.modifica(persoana_modificata)
        repository_persoane_all = self.repository_persoane.get_all()
        self.assertEqual(repository_persoane_all[0].get_person_id(), 3)
        self.assertEqual(repository_persoane_all[0].get_nume(), "Mocanu Emilian")
        self.assertEqual(repository_persoane_all[0].get_adresa(), "asddas")

    def testH(self):
        # verifica daca metoda de stergere a unui obiect din repository functioneaza corespunzator
        self.repository_persoane.adauga(self.persoana)
        self.repository_persoane.sterge_dupa_id(self.person_id)
        self.assertEqual(len(self.repository_persoane), 0)

    def testI(self):
        # testeaza daca functia de stergere ridica exceptia corecta, in cazul in care nu exista persoana data in repo
        self.repository_persoane.adauga(self.persoana)
        self.assertRaisesRegex(RepositoryEroare, "Nu exista o persoana cu ID-ul specificat!\n",
                               self.repository_persoane.sterge_dupa_id, 5
                               )


class TesteRepoEvenimenteMemory(unittest.TestCase):
    def setUp(self):
        # executa functia inaintea fiecarei functii de test.
        self.repository_evenimente = RepositoryEvenimente()
        self.event_id = 3
        self.data = "31.10.2020"
        self.timp = "23:00"
        self.descriere = "Revelion la munte."
        self.eveniment = Eveniment(self.event_id, self.data, self.timp, self.descriere)

    def testA(self):
        # verifica daca, fara sa adauge un eveniment, repository-ul de persoane este gol
        self.assertEqual(len(self.repository_evenimente), 0)

    def testB(self):
        # verifica adaugarea corecta a unui eveniment
        self.repository_evenimente.adauga(self.eveniment)
        self.assertEqual(len(self.repository_evenimente), 1)

    def testC(self):
        # verifica daca, in urma adaugarii unui eveniment cu un id deja rezervat, ridica eroarea corespunzatoare
        self.repository_evenimente.adauga(self.eveniment)
        eveniment = Eveniment(self.event_id, "17.10.2020", "14:23", "saddas")
        self.assertRaisesRegex(RepositoryEroare, "Exista deja un eveniment cu ID-ul specificat!\n",
                               self.repository_evenimente.adauga, eveniment)

    def testD(self):
        # testeaza daca functia de cautare a unei persoane returneaza evenimentul corect
        self.repository_evenimente.adauga(self.eveniment)
        eveniment_gasit = self.repository_evenimente.cauta_dupa_id(self.event_id)
        self.assertEqual(eveniment_gasit.get_event_id(), 3)
        self.assertEqual(eveniment_gasit.get_data(), "31.10.2020")
        self.assertEqual(eveniment_gasit.get_timp(), "23:00")
        self.assertEqual(eveniment_gasit.get_descriere(), "Revelion la munte.")

    def testE(self):
        # testeaza daca functia de cautare ridica exceptia corecta, in cazul in care nu exista evenimentul dat in repo
        self.repository_evenimente.adauga(self.eveniment)
        self.assertRaisesRegex(RepositoryEroare, "Nu exista un eveniment cu ID-ul specificat!\n",
                               self.repository_evenimente.cauta_dupa_id, 7)

    def testF(self):
        # testeaza daca functia de modificare ridica exceptia corecta, in cazul in care nu exista evenimentul dat in repo
        self.repository_evenimente.adauga(self.eveniment)
        eveniment_modificat = Eveniment(14, "05.02.2030", "17:34", "Ski.")
        self.assertRaisesRegex(RepositoryEroare, "Nu exista un eveniment cu ID-ul specificat!\n",
                               self.repository_evenimente.modifica, eveniment_modificat
                               )

    def testG(self):
        # verifica daca functia de get_all returneaza corect, sub forma unei liste de obicete, toate evenimentele din repo
        self.repository_evenimente.adauga(self.eveniment)
        eveniment_modificat = Eveniment(3, "05.02.2030", "17:34", "Ski.")
        self.repository_evenimente.modifica(eveniment_modificat)
        repository_evenimente_all = self.repository_evenimente.get_all()
        self.assertEqual(repository_evenimente_all[0].get_event_id(), 3)
        self.assertEqual(repository_evenimente_all[0].get_data(), "05.02.2030")
        self.assertEqual(repository_evenimente_all[0].get_timp(), "17:34")
        self.assertEqual(repository_evenimente_all[0].get_descriere(), "Ski.")

    def testH(self):
        # verifica daca metoda de stergere a unui obiect din repository functioneaza corespunzator
        self.repository_evenimente.adauga(self.eveniment)
        self.repository_evenimente.sterge_dupa_id(self.event_id)
        self.assertEqual(len(self.repository_evenimente), 0)

    def testI(self):
        # testeaza daca functia de stergere ridica exceptia corecta, in cazul in care nu exista evenimentul dat in repo
        self.repository_evenimente.adauga(self.eveniment)
        self.assertRaisesRegex(RepositoryEroare, "Nu exista un eveniment cu ID-ul specificat!\n",
                               self.repository_evenimente.sterge_dupa_id, 5
                               )


class TesteRepoInscrieriMemory(unittest.TestCase):
    def setUp(self):
        # executa functia inaintea fiecarei functii de test.
        self.repository_persoane = RepositoryPersoane()
        self.repository_evenimente = RepositoryEvenimente()
        self.repository_inscrieri = RepositoryInscrieri()
        self.persoana = Persoana(1, "Andrei", "Str. Tipatesti, Nr.3")
        self.repository_persoane.adauga(self.persoana)
        self.eveniment = Eveniment(1, "23:12:2023", "20:30", "Nunta")
        self.repository_evenimente.adauga(self.eveniment)
        self.inscriere = Inscriere(self.persoana, self.eveniment)

    def testA(self):
        # verifica daca, fara sa adauge o inscriere, repository-ul de inscrieri este gol
        self.assertEqual(len(self.repository_inscrieri), 0)

    def testB(self):
        # verifica adaugarea corecta a unei inscrieri
        self.repository_inscrieri.adauga(self.inscriere, self.repository_persoane.get_all(),
                                         self.repository_evenimente.get_all())
        self.assertEqual(len(self.repository_inscrieri), 1)

    def testC(self):
        # verifica daca functia de get_all returneaza corect, sub forma unei liste de obicete, toate inscrierile din repo
        self.repository_inscrieri.adauga(self.inscriere, self.repository_persoane.get_all(),
                                         self.repository_evenimente.get_all())
        lista = self.repository_inscrieri.get_all()
        assert (lista[0].get_persoana() == self.persoana)
        assert (lista[0].get_eveniment() == self.eveniment)

    def testD(self):
        # testeaza daca functia de cautare ridica exceptia corecta, in cazul in care incearca sa adauge o inscriere,
        # avand o persoana care nu se afla in repository de persoane
        persoana = Persoana(2, "Simion", "Str. Tipatesti, Nr. 34")
        inscriere = Inscriere(persoana, self.eveniment)
        self.assertRaisesRegex(RepositoryEroare, "Nu exista o persoana cu ID-ul specificat!\n",
                               self.repository_inscrieri.adauga, inscriere,
                               self.repository_persoane.get_all(), self.repository_evenimente.get_all()
                               )

    def testE(self):
        # testeaza daca functia de cautare ridica exceptia corecta, in cazul in care incearca sa adauge o inscriere,
        # avand un eveniment care nu se afla in repository de evenimente
        eveniment = Eveniment(2, "10.10.2021", "10:10", "Nunta")
        inscriere = Inscriere(self.persoana, eveniment)
        self.assertRaisesRegex(RepositoryEroare, "Nu exista un eveniment cu ID-ul specificat!\n",
                               self.repository_inscrieri.adauga, inscriere,
                               self.repository_persoane.get_all(), self.repository_evenimente.get_all()
                               )

    def testF(self):
        # testeaza daca functia de cautare ridica exceptia corecta, in cazul in care incearca sa adauge o inscriere,
        # avand o persoana, respctiv in eveniment care nu se afla in repository de persoane, respectiv evenimente
        persoana = Persoana(2, "Simion", "Str. Tipatesti, Nr. 34")
        eveniment = Eveniment(2, "10.10.2021", "10:10", "Nunta")
        inscriere = Inscriere(persoana, eveniment)
        self.assertRaisesRegex(RepositoryEroare,
                               "Nu exista o persoana cu ID-ul specificat!\nNu exista un eveniment cu ID-ul specificat!\n",
                               self.repository_inscrieri.adauga, inscriere,
                               self.repository_persoane.get_all(), self.repository_evenimente.get_all()
                               )

    def testG(self):
        # testeaza daca functia de cautare ridica exceptia corecta, in cazul in care incearca sa adauge o inscriere
        # care se afla deja in repository
        self.repository_inscrieri.adauga(self.inscriere, self.repository_persoane.get_all(),
                                         self.repository_evenimente.get_all())
        self.assertRaisesRegex(RepositoryEroare, "Persoana specificata este deja inscrisa la eveniment!\n",
                               self.repository_inscrieri.adauga, self.inscriere,
                               self.repository_persoane.get_all(), self.repository_evenimente.get_all()
                               )

    def testH(self):
        # verifica daca metoda de stergere a unui obiect din repository functioneaza corespunzator
        self.repository_inscrieri.adauga(self.inscriere, self.repository_persoane.get_all(),
                                         self.repository_evenimente.get_all())
        self.repository_inscrieri.sterge(self.inscriere)
        self.assertEqual(len(self.repository_inscrieri), 0)

    def testI(self):
        # testeaza daca functia de cautare ridica exceptia corecta, in cazul in care incearca sa stearga o inscriere
        # care nu se afla deja in repository
        self.repository_inscrieri.adauga(self.inscriere, self.repository_persoane.get_all(),
                                         self.repository_evenimente.get_all())
        self.repository_inscrieri.sterge(self.inscriere)
        self.assertRaisesRegex(RepositoryEroare, "Persoana data nu este inscrisa la acest eveniment!\n",
                               self.repository_inscrieri.sterge, self.inscriere)




class TesteRepoPersoaneFisier(unittest.TestCase):
    def setUp(self):
        # executa functia inaintea fiecarei functii de test.
        self.file_persoane = open("teste_persoane_fisier.txt", "w")
        self.repository_persoane = RepositoryPersoaneFiles("teste_persoane_fisier.txt")
        self.person_id = 3
        self.nume = "Mirel Marcel"
        self.adresa = "Str Eris, Nr. 3"
        self.persoana = Persoana(self.person_id, self.nume, self.adresa)

    def tearDown(self):
        # executa functia dupa fiecare metoda
        self.file_persoane.close()

    def testA(self):
        # verifica daca, fara sa adauge o persoana, repository-ul de persoane este gol
        self.assertEqual(len(self.repository_persoane), 0)

    def testB(self):
        # verifica adaugarea corecta a unei persoane
        self.repository_persoane.adauga(self.persoana)
        self.assertEqual(len(self.repository_persoane), 1)

    def testC(self):
        self.repository_persoane.adauga(self.persoana)
        # verifica daca, in urma adaugarii unei persoane cu un id deja rezervat, ridica eroarea corespunzatoare
        persoana = Persoana(self.person_id, "dadsa", "31132")
        self.assertRaisesRegex(RepositoryEroare, "Exista deja o persoana cu ID-ul specificat!\n",
                               self.repository_persoane.adauga, persoana)

    def testD(self):
        # testeaza daca functia de cautare a unei persoane returneaza persoana corecta
        self.repository_persoane.adauga(self.persoana)
        persoana_gasita = self.repository_persoane.cauta_dupa_id(self.person_id)
        self.assertEqual(persoana_gasita.get_person_id(), 3)
        self.assertEqual(persoana_gasita.get_nume(), "Mirel Marcel")
        self.assertEqual(persoana_gasita.get_adresa(), "Str Eris, Nr. 3")

    def testE(self):
        # testeaza daca functia de cautare ridica exceptia corecta, in cazul in care nu exista persoana data in repo
        self.repository_persoane.adauga(self.persoana)
        self.assertRaisesRegex(RepositoryEroare, "Nu exista o persoana cu ID-ul specificat!\n",
                               self.repository_persoane.cauta_dupa_id, 7)

    def testF(self):
        # testeaza daca functia de modificare ridica exceptia corecta, in cazul in care nu exista persoana data in repo
        self.repository_persoane.adauga(self.persoana)
        persoana_modifcata = Persoana(14, "Mocanu Emilian", "asddas")
        self.assertRaisesRegex(RepositoryEroare, "Nu exista o persoana cu ID-ul specificat!\n",
                               self.repository_persoane.modifica, persoana_modifcata
                               )

    def testG(self):
        # verifica daca functia de get_all returneaza corect, sub forma unei liste de obicete, toate persoanele din repo
        self.repository_persoane.adauga(self.persoana)
        persoana_modificata = Persoana(3, "Mocanu Emilian", "asddas")
        self.repository_persoane.modifica(persoana_modificata)
        repository_persoane_all = self.repository_persoane.get_all()
        self.assertEqual(repository_persoane_all[0].get_person_id(), 3)
        self.assertEqual(repository_persoane_all[0].get_nume(), "Mocanu Emilian")
        self.assertEqual(repository_persoane_all[0].get_adresa(), "asddas")

    def testH(self):
        # verifica daca metoda de stergere a unui obiect din repository functioneaza corespunzator
        self.repository_persoane.adauga(self.persoana)
        self.repository_persoane.sterge_dupa_id(self.person_id)
        self.assertEqual(len(self.repository_persoane), 0)

    def testI(self):
        # testeaza daca functia de stergere ridica exceptia corecta, in cazul in care nu exista persoana data in repo
        self.repository_persoane.adauga(self.persoana)
        self.assertRaisesRegex(RepositoryEroare, "Nu exista o persoana cu ID-ul specificat!\n",
                               self.repository_persoane.sterge_dupa_id, 5
                               )


class TesteRepoEvenimenteFisier(unittest.TestCase):
    def setUp(self):
        # executa functia inaintea fiecarei functii de test.
        self.file_evenimente = open("teste_evenimente_fisier.txt", "w")
        self.repository_evenimente = RepositoryEvenimenteFiles("teste_evenimente_fisier.txt")
        self.event_id = 3
        self.data = "31.10.2020"
        self.timp = "23:00"
        self.descriere = "Revelion la munte."
        self.eveniment = Eveniment(self.event_id, self.data, self.timp, self.descriere)

    def tearDown(self):
        # executa functia dupa fiecare metoda
        self.file_evenimente.close()

    def testA(self):
        # verifica daca, fara sa adauge un eveniment, repository-ul de persoane este gol
        self.assertEqual(len(self.repository_evenimente), 0)

    def testB(self):
        # verifica adaugarea corecta a unui eveniment
        self.repository_evenimente.adauga(self.eveniment)
        self.assertEqual(len(self.repository_evenimente), 1)

    def testC(self):
        # verifica daca, in urma adaugarii unui eveniment cu un id deja rezervat, ridica eroarea corespunzatoare
        self.repository_evenimente.adauga(self.eveniment)
        eveniment = Eveniment(self.event_id, "17.10.2020", "14:23", "saddas")
        self.assertRaisesRegex(RepositoryEroare, "Exista deja un eveniment cu ID-ul specificat!\n",
                               self.repository_evenimente.adauga, eveniment)

    def testD(self):
        # testeaza daca functia de cautare a unei persoane returneaza evenimentul corect
        self.repository_evenimente.adauga(self.eveniment)
        eveniment_gasit = self.repository_evenimente.cauta_dupa_id(self.event_id)
        self.assertEqual(eveniment_gasit.get_event_id(), 3)
        self.assertEqual(eveniment_gasit.get_data(), "31.10.2020")
        self.assertEqual(eveniment_gasit.get_timp(), "23:00")
        self.assertEqual(eveniment_gasit.get_descriere(), "Revelion la munte.")

    def testE(self):
        # testeaza daca functia de cautare ridica exceptia corecta, in cazul in care nu exista evenimentul dat in repo
        self.repository_evenimente.adauga(self.eveniment)
        self.assertRaisesRegex(RepositoryEroare, "Nu exista un eveniment cu ID-ul specificat!\n",
                               self.repository_evenimente.cauta_dupa_id, 7)

    def testF(self):
        # testeaza daca functia de modificare ridica exceptia corecta, in cazul in care nu exista evenimentul dat in repo
        self.repository_evenimente.adauga(self.eveniment)
        eveniment_modificat = Eveniment(14, "05.02.2030", "17:34", "Ski.")
        self.assertRaisesRegex(RepositoryEroare, "Nu exista un eveniment cu ID-ul specificat!\n",
                               self.repository_evenimente.modifica, eveniment_modificat
                               )

    def testG(self):
        # verifica daca functia de get_all returneaza corect, sub forma unei liste de obicete, toate evenimentele din repo
        self.repository_evenimente.adauga(self.eveniment)
        eveniment_modificat = Eveniment(3, "05.02.2030", "17:34", "Ski.")
        self.repository_evenimente.modifica(eveniment_modificat)
        repository_evenimente_all = self.repository_evenimente.get_all()
        self.assertEqual(repository_evenimente_all[0].get_event_id(), 3)
        self.assertEqual(repository_evenimente_all[0].get_data(), "05.02.2030")
        self.assertEqual(repository_evenimente_all[0].get_timp(), "17:34")
        self.assertEqual(repository_evenimente_all[0].get_descriere(), "Ski.")

    def testH(self):
        # verifica daca metoda de stergere a unui obiect din repository functioneaza corespunzator
        self.repository_evenimente.adauga(self.eveniment)
        self.repository_evenimente.sterge_dupa_id(self.event_id)
        self.assertEqual(len(self.repository_evenimente), 0)

    def testI(self):
        # testeaza daca functia de stergere ridica exceptia corecta, in cazul in care nu exista evenimentul dat in repo
        self.repository_evenimente.adauga(self.eveniment)
        self.assertRaisesRegex(RepositoryEroare, "Nu exista un eveniment cu ID-ul specificat!\n",
                               self.repository_evenimente.sterge_dupa_id, 5
                               )


class TesteRepoInscrieriFisier(unittest.TestCase):
    def setUp(self):
        # executa functia inaintea fiecarei functii de test.
        self.file_persoane = open("teste_persoane_fisier.txt", "w")
        self.repository_persoane = RepositoryPersoaneFiles("teste_persoane_fisier.txt")
        self.file_evenimente = open("teste_evenimente_fisier.txt", "w")
        self.repository_evenimente = RepositoryEvenimenteFiles("teste_evenimente_fisier.txt")
        self.file_inscrieri = open("teste_inscrieri_fisier.txt", "w")
        self.repository_inscrieri = RepositoryInscrieriFiles("teste_inscrieri_fisier.txt")
        self.persoana = Persoana(1, "Andrei", "Str. Tipatesti, Nr.3")
        self.repository_persoane.adauga(self.persoana)
        self.eveniment = Eveniment(1, "23:12:2023", "20:30", "Nunta")
        self.repository_evenimente.adauga(self.eveniment)
        self.inscriere = Inscriere(self.persoana, self.eveniment)

    def tearDown(self):
        # executa functia dupa fiecare metoda
        self.file_persoane.close()
        self.file_evenimente.close()
        self.file_inscrieri.close()

    def testA(self):
        # verifica daca, fara sa adauge o inscriere, repository-ul de inscrieri este gol
        self.assertEqual(len(self.repository_inscrieri), 0)

    def testB(self):
        # verifica adaugarea corecta a unei inscrieri
        self.repository_inscrieri.adauga(self.inscriere, self.repository_persoane.get_all(),
                                         self.repository_evenimente.get_all())
        self.assertEqual(len(self.repository_inscrieri), 1)

    def testC(self):
        # verifica daca functia de get_all returneaza corect, sub forma unei liste de obicete, toate inscrierile din repo
        self.repository_inscrieri.adauga(self.inscriere, self.repository_persoane.get_all(),
                                         self.repository_evenimente.get_all())
        lista = self.repository_inscrieri.get_all()
        assert (lista[0].get_persoana() == self.persoana)
        assert (lista[0].get_eveniment() == self.eveniment)

    def testD(self):
        # testeaza daca functia de cautare ridica exceptia corecta, in cazul in care incearca sa adauge o inscriere,
        # avand o persoana care nu se afla in repository de persoane
        persoana = Persoana(2, "Simion", "Str. Tipatesti, Nr. 34")
        inscriere = Inscriere(persoana, self.eveniment)
        self.assertRaisesRegex(RepositoryEroare, "Nu exista o persoana cu ID-ul specificat!\n",
                               self.repository_inscrieri.adauga, inscriere,
                               self.repository_persoane.get_all(), self.repository_evenimente.get_all()
                               )

    def testE(self):
        # testeaza daca functia de cautare ridica exceptia corecta, in cazul in care incearca sa adauge o inscriere,
        # avand un eveniment care nu se afla in repository de evenimente
        eveniment = Eveniment(2, "10.10.2021", "10:10", "Nunta")
        inscriere = Inscriere(self.persoana, eveniment)
        self.assertRaisesRegex(RepositoryEroare, "Nu exista un eveniment cu ID-ul specificat!\n",
                               self.repository_inscrieri.adauga, inscriere,
                               self.repository_persoane.get_all(), self.repository_evenimente.get_all()
                               )

    def testF(self):
        # testeaza daca functia de cautare ridica exceptia corecta, in cazul in care incearca sa adauge o inscriere,
        # avand o persoana, respctiv in eveniment care nu se afla in repository de persoane, respectiv evenimente
        persoana = Persoana(2, "Simion", "Str. Tipatesti, Nr. 34")
        eveniment = Eveniment(2, "10.10.2021", "10:10", "Nunta")
        inscriere = Inscriere(persoana, eveniment)
        self.assertRaisesRegex(RepositoryEroare,
                               "Nu exista o persoana cu ID-ul specificat!\nNu exista un eveniment cu ID-ul specificat!\n",
                               self.repository_inscrieri.adauga, inscriere,
                               self.repository_persoane.get_all(), self.repository_evenimente.get_all()
                               )

    def testG(self):
        # testeaza daca functia de cautare ridica exceptia corecta, in cazul in care incearca sa adauge o inscriere
        # care se afla deja in repository
        self.repository_inscrieri.adauga(self.inscriere, self.repository_persoane.get_all(),
                                         self.repository_evenimente.get_all())
        self.assertRaisesRegex(RepositoryEroare, "Persoana specificata este deja inscrisa la eveniment!\n",
                               self.repository_inscrieri.adauga, self.inscriere,
                               self.repository_persoane.get_all(), self.repository_evenimente.get_all()
                               )

    def testH(self):
        # verifica daca metoda de stergere a unui obiect din repository functioneaza corespunzator
        self.repository_inscrieri.adauga(self.inscriere, self.repository_persoane.get_all(),
                                         self.repository_evenimente.get_all())
        self.repository_inscrieri.sterge(self.inscriere)
        self.assertEqual(len(self.repository_inscrieri), 0)

    def testI(self):
        self.repository_inscrieri.adauga(self.inscriere, self.repository_persoane.get_all(),
                                         self.repository_evenimente.get_all())
        self.repository_evenimente.adauga(Eveniment(2, "23:12:2023", "20:30", "Nunta"))
        inscriere = Inscriere(Persoana(1, "Andrei", "Str. Tipatesti, Nr.3"),
                              Eveniment(2, "23:12:2023", "20:30", "Nunta"))
        self.repository_inscrieri.adauga(inscriere, self.repository_persoane.get_all(),self.repository_evenimente.get_all())
        self.repository_inscrieri.sterge(self.inscriere)


class TesteServicePersoaneMemory(unittest.TestCase):
    def setUp(self):
        self.__validator_persoana = ValidatorPersoana()
        self.__repository_persoane = RepositoryPersoane()
        self.__service_persoane = ServicePersoane(self.__validator_persoana, self.__repository_persoane)

    def testA(self):
        self.assertEqual(len(self.__repository_persoane), 0)
        self.__service_persoane.adauga_persoana(3, "Andrei", "Str Tipografiei, nr. 3")
        self.assertEqual(len(self.__repository_persoane), 1)

    def testB(self):
        self.__service_persoane.adauga_persoana(3, "Andrei", "Str Tipografiei, nr. 3")
        self.__service_persoane.sterge_persoana(3)
        self.assertEqual(len(self.__repository_persoane), 0)

    def testC(self):
        self.__service_persoane.adauga_persoana(3, "Andrei", "Str Tipografiei, nr. 3")
        self.__service_persoane.adauga_persoana(4, "Simion", "Str Marului")
        self.assertEqual(self.__service_persoane.get_persoane()[0].get_person_id(), 3)
        self.assertEqual(self.__service_persoane.get_persoane()[0].get_nume(), "Andrei")
        self.assertEqual(self.__service_persoane.get_persoane()[0].get_adresa(), "Str Tipografiei, nr. 3")
        self.assertEqual(self.__service_persoane.get_persoane()[1].get_person_id(), 4)
        self.assertEqual(self.__service_persoane.get_persoane()[1].get_nume(), "Simion")
        self.assertEqual(self.__service_persoane.get_persoane()[1].get_adresa(), "Str Marului")

    def testD(self):
        self.__service_persoane.adauga_persoana(3, "Andrei", "Str Tipografiei, nr. 3")
        self.__service_persoane.modifica_persoana(3, "Simion", "Str Marului")
        self.assertEqual(self.__service_persoane.get_persoane()[0].get_person_id(), 3)
        self.assertEqual(self.__service_persoane.get_persoane()[0].get_nume(), "Simion")
        self.assertEqual(self.__service_persoane.get_persoane()[0].get_adresa(), "Str Marului")

    def testE(self):
        self.__service_persoane.adauga_persoana(3, "Andrei", "Str Tipografiei, nr. 3")
        persoana_gasita = self.__service_persoane.cauta_persoana(3)
        self.assertEqual(persoana_gasita.get_person_id(), 3)
        self.assertEqual(persoana_gasita.get_nume(), "Andrei")
        self.assertEqual(persoana_gasita.get_adresa(), "Str Tipografiei, nr. 3")

    def testF(self):
        nr_persoane = random.randrange(20, 50)
        self.__service_persoane.adauga_persoane_random(nr_persoane)
        self.assertEqual(len(self.__repository_persoane), nr_persoane)


class TesteServiceEvenimenteMemory(unittest.TestCase):
    def setUp(self):
        self.__validator_eveniment = ValidatorEveniment()
        self.__repository_evenimente = RepositoryEvenimente()
        self.__service_evenimente = ServiceEvenimente(self.__validator_eveniment, self.__repository_evenimente)

    def testA(self):
        self.assertEqual(len(self.__repository_evenimente), 0)
        self.__service_evenimente.adauga_eveniment(3, "17.10.2021", "22:30", "Zi de nastere")
        self.assertEqual(len(self.__repository_evenimente), 1)

    def testB(self):
        self.__service_evenimente.adauga_eveniment(3, "17.10.2021", "22:30", "Zi de nastere")
        self.__service_evenimente.sterge_eveniment(3)
        self.assertEqual(len(self.__repository_evenimente), 0)

    def testC(self):
        self.__service_evenimente.adauga_eveniment(3, "17.10.2021", "22:30", "Zi de nastere")
        self.__service_evenimente.adauga_eveniment(4, "13.12.2021", "15:00", "Aniversare")
        self.assertEqual(self.__service_evenimente.get_evenimente()[0].get_event_id(), 3)
        self.assertEqual(self.__service_evenimente.get_evenimente()[0].get_data(), "17.10.2021")
        self.assertEqual(self.__service_evenimente.get_evenimente()[0].get_timp(), "22:30")
        self.assertEqual(self.__service_evenimente.get_evenimente()[0].get_descriere(), "Zi de nastere")
        self.assertEqual(self.__service_evenimente.get_evenimente()[1].get_event_id(), 4)
        self.assertEqual(self.__service_evenimente.get_evenimente()[1].get_data(), "13.12.2021")
        self.assertEqual(self.__service_evenimente.get_evenimente()[1].get_timp(), "15:00")
        self.assertEqual(self.__service_evenimente.get_evenimente()[1].get_descriere(), "Aniversare")

    def testD(self):
        self.__service_evenimente.adauga_eveniment(3, "17.10.2021", "22:30", "Zi de nastere")
        self.__service_evenimente.modifica_eveniment(3, "13.12.2021", "15:00", "Aniversare")
        self.assertEqual(self.__service_evenimente.get_evenimente()[0].get_event_id(), 3)
        self.assertEqual(self.__service_evenimente.get_evenimente()[0].get_data(), "13.12.2021")
        self.assertEqual(self.__service_evenimente.get_evenimente()[0].get_timp(), "15:00")
        self.assertEqual(self.__service_evenimente.get_evenimente()[0].get_descriere(), "Aniversare")

    def testE(self):
        self.__service_evenimente.adauga_eveniment(3, "17.10.2021", "22:30", "Zi de nastere")
        eveniment_gasit = self.__service_evenimente.cauta_eveniment(3)
        self.assertEqual(eveniment_gasit.get_event_id(), 3)
        self.assertEqual(eveniment_gasit.get_data(), "17.10.2021")
        self.assertEqual(eveniment_gasit.get_timp(), "22:30")
        self.assertEqual(eveniment_gasit.get_descriere(), "Zi de nastere")

    def testF(self):
        nr_evenimente = random.randrange(20, 50)
        self.__service_evenimente.adauga_evenimente_random(nr_evenimente)
        self.assertEqual(len(self.__repository_evenimente), nr_evenimente)


class TesteBubbleSort(unittest.TestCase):
    def setUp(self):
        self.__lista = [5, 3, 2, 5, 1, 23, 4, 2, 14]

    def testA(self):
        Sort().bubble_sort(self.__lista)
        self.assertEqual(self.__lista, [1, 2, 2, 3, 4, 5, 5, 14, 23])

    def testB(self):
        Sort().bubble_sort(self.__lista, l=2)
        self.assertEqual(self.__lista, [5, 3, 1, 2, 2, 4, 5, 14, 23])

    def testC(self):
        Sort().bubble_sort(self.__lista, r=8)
        self.assertEqual(self.__lista, [1, 2, 2, 3, 4, 5, 5, 23, 14])

    def testD(self):
        Sort().bubble_sort(self.__lista, l=3, r=8)
        self.assertEqual(self.__lista, [5, 3, 2, 1, 2, 4, 5, 23, 14])


class TesteCombSort(unittest.TestCase):
    def setUp(self):
        self.__lista = [5, 3, 2, 5, 1, 23, 4, 2, 14]

    def testA(self):
        Sort().comb_sort(self.__lista)
        self.assertEqual(self.__lista, [1, 2, 2, 3, 4, 5, 5, 14, 23])

    def testB(self):
        Sort().comb_sort(self.__lista, l=2)
        self.assertEqual(self.__lista, [5, 3, 1, 2, 2, 4, 5, 14, 23])

    def testC(self):
        Sort().comb_sort(self.__lista, r=8)
        self.assertEqual(self.__lista, [1, 2, 2, 3, 4, 5, 5, 23, 14])

    def testD(self):
        Sort().comb_sort(self.__lista, l=3, r=8)
        self.assertEqual(self.__lista, [5, 3, 2, 1, 2, 4, 5, 23, 14])


class TesteServiceInscrieriMemory(unittest.TestCase):
    def setUp(self):
        self.__repository_persoane = RepositoryPersoane()
        self.__repository_evenimente = RepositoryEvenimente()
        self.__repository_inscrieri = RepositoryInscrieri()
        self.__repository_persoane = RepositoryPersoane()
        self.__repository_evenimente = RepositoryEvenimente()
        self.__service_inscrieri = ServiceInscrieri(self.__repository_persoane, self.__repository_evenimente, self.__repository_inscrieri)

    def testA(self):
        self.__repository_persoane.adauga(Persoana(3, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(3, "17.10.2021", "22:30", "Zi de nastere"))
        self.__service_inscrieri.adauga_inscriere(3, 3)
        self.assertEqual(len(self.__repository_inscrieri), 1)

    def testB(self):
        self.__repository_persoane.adauga(Persoana(3, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(3, "17.10.2021", "22:30", "Zi de nastere"))
        self.__service_inscrieri.adauga_inscriere(3, 3)
        self.__service_inscrieri.sterge_inscriere(3, 3)
        self.assertEqual(len(self.__repository_inscrieri), 0)

    def testC(self):
        self.__repository_persoane.adauga(Persoana(3, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(3, "17.10.2021", "22:30", "Zi de nastere"))
        self.__repository_persoane.adauga(Persoana(4, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(4, "17.10.2021", "22:30", "Zi de nastere"))
        self.__service_inscrieri.adauga_inscriere(3, 3)
        self.__service_inscrieri.adauga_inscriere(4, 4)
        self.__service_inscrieri.sterge_persoana_inscrieri(3)
        self.assertEqual(len(self.__repository_inscrieri), 1)

    def testD(self):
        self.__repository_persoane.adauga(Persoana(3, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(3, "17.10.2021", "22:30", "Zi de nastere"))
        self.__repository_persoane.adauga(Persoana(4, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(4, "17.10.2021", "22:30", "Zi de nastere"))
        self.__service_inscrieri.adauga_inscriere(3, 3)
        self.__service_inscrieri.adauga_inscriere(4, 4)
        self.__service_inscrieri.sterge_eveniment_inscrieri(3)
        self.assertEqual(len(self.__repository_inscrieri), 1)

    def testE(self):
        self.__repository_persoane.adauga(Persoana(3, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(3, "17.10.2021", "22:30", "Zi de nastere"))
        self.__service_inscrieri.adauga_inscriere(3, 3)
        lista_inscrieri = self.__service_inscrieri.get_inscrieri()
        self.assertEqual(lista_inscrieri[0].get_persoana().get_person_id(), 3)
        self.assertEqual(lista_inscrieri[0].get_persoana().get_nume(), "Andrei")
        self.assertEqual(lista_inscrieri[0].get_persoana().get_adresa(), "Str Tipografiei, nr. 3")
        self.assertEqual(lista_inscrieri[0].get_eveniment().get_event_id(), 3)
        self.assertEqual(lista_inscrieri[0].get_eveniment().get_data(), "17.10.2021")
        self.assertEqual(lista_inscrieri[0].get_eveniment().get_timp(), "22:30")
        self.assertEqual(lista_inscrieri[0].get_eveniment().get_descriere(), "Zi de nastere")

    def testG(self):
        self.__repository_persoane.adauga(Persoana(3, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(3, "17.10.2021", "22:30", "Zi de nastere"))
        self.__service_inscrieri.adauga_inscriere(3, 3)
        self.__service_inscrieri.modifica_persoana_inscrieri(3, "Simion", "Str, Marului")
        lista_inscrieri = self.__service_inscrieri.get_inscrieri()
        self.assertEqual(lista_inscrieri[0].get_persoana().get_person_id(), 3)
        self.assertEqual(lista_inscrieri[0].get_persoana().get_nume(), "Simion")
        self.assertEqual(lista_inscrieri[0].get_persoana().get_adresa(), "Str, Marului")

    def testH(self):
        self.__repository_persoane.adauga(Persoana(3, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(3, "17.10.2021", "22:30", "Zi de nastere"))
        self.__service_inscrieri.adauga_inscriere(3, 3)
        self.__service_inscrieri.modifica_eveniment_inscrieri(3, "13.10.2023", "10:00", "Nunta")
        lista_inscrieri = self.__service_inscrieri.get_inscrieri()
        self.assertEqual(lista_inscrieri[0].get_eveniment().get_event_id(), 3)
        self.assertEqual(lista_inscrieri[0].get_eveniment().get_data(), "13.10.2023")
        self.assertEqual(lista_inscrieri[0].get_eveniment().get_timp(), "10:00")
        self.assertEqual(lista_inscrieri[0].get_eveniment().get_descriere(), "Nunta")

    def testI(self):
        self.__repository_persoane.adauga(Persoana(1, "das", "da"))
        self.__repository_evenimente.adauga(Eveniment(1, "01.01.2023", "00:00", "a"))
        self.__repository_evenimente.adauga(Eveniment(2, "10.01.2022", "00:00", "a"))
        self.__repository_evenimente.adauga(Eveniment(3, "09.10.2022", "00:00", "aa"))
        self.__repository_evenimente.adauga(Eveniment(4, "09.11.2021", "00:00", "aa"))
        self.__repository_evenimente.adauga(Eveniment(5, "13.10.2021", "00:00", "aaa"))
        self.__repository_evenimente.adauga(Eveniment(6, "09.10.2021", "00:00", "aaa"))
        self.__repository_evenimente.adauga(Eveniment(7, "10.10.2021", "00:00", "aaaaz"))
        self.__repository_evenimente.adauga(Eveniment(8, "10.11.2021", "00:00", "aaaa"))
        self.__repository_evenimente.adauga(Eveniment(9, "10.10.2022", "00:00", "aaaaz"))
        self.__service_inscrieri.adauga_inscriere(1, 1)
        self.__service_inscrieri.adauga_inscriere(1, 2)
        self.__service_inscrieri.adauga_inscriere(1, 3)
        self.__service_inscrieri.adauga_inscriere(1, 4)
        self.__service_inscrieri.adauga_inscriere(1, 5)
        self.__service_inscrieri.adauga_inscriere(1, 6)
        self.__service_inscrieri.adauga_inscriere(1, 7)
        self.__service_inscrieri.adauga_inscriere(1, 8)
        self.__service_inscrieri.adauga_inscriere(1, 9)
        lista_evenimente = self.__service_inscrieri.lista_evenimente_persoana(Persoana(1, "das", "da"))
        self.assertEqual(lista_evenimente, [Eveniment(2, "10.01.2022", "00:00", "a"),
                                            Eveniment(1, "01.01.2023", "00:00", "a"),
                                            Eveniment(4, "09.11.2021", "00:00", "aa"),
                                            Eveniment(3, "09.10.2022", "00:00", "aa"),
                                            Eveniment(6, "09.10.2021", "00:00", "aaa"),
                                            Eveniment(5, "13.10.2021", "00:00", "aaa"),
                                            Eveniment(8, "10.11.2021", "00:00", "aaaa"),
                                            Eveniment(7, "10.10.2021", "00:00", "aaaaz"),
                                            Eveniment(9, "10.10.2022", "00:00", "aaaaz")])

    def testJ(self):
        self.__repository_persoane.adauga(Persoana(1, "das", "da"))
        self.__repository_evenimente.adauga(Eveniment(1, "01.01.2023", "00:00", "a"))
        lista_evenimente = self.__service_inscrieri.lista_evenimente_persoana(Persoana(1, "das", "da"))
        self.assertEqual(lista_evenimente, [])

    def testK(self):
        self.__repository_persoane.adauga(Persoana(1, "das", "da"))
        self.__repository_persoane.adauga(Persoana(2, "das", "da"))
        self.__repository_persoane.adauga(Persoana(3, "das", "da"))
        self.__repository_evenimente.adauga(Eveniment(1, "01.01.2023", "00:00", "a"))
        self.__repository_evenimente.adauga(Eveniment(2, "01.01.2023", "00:00", "a"))
        self.__service_inscrieri.adauga_inscriere(1, 1)
        self.__service_inscrieri.adauga_inscriere(2, 1)
        self.__service_inscrieri.adauga_inscriere(2, 2)
        lista_persoane = self.__service_inscrieri.persoane_multe_inscrieri()
        self.assertEqual(lista_persoane[0].get_id(), 2)
        self.assertEqual(lista_persoane[0].get_nr_inscrieri(), 2)
        self.assertEqual(lista_persoane[1].get_id(), 1)
        self.assertEqual(lista_persoane[1].get_nr_inscrieri(), 1)
        self.assertEqual(lista_persoane[2].get_id(), 3)
        self.assertEqual(lista_persoane[2].get_nr_inscrieri(), 0)

    def testL(self):
        self.__repository_persoane.adauga(Persoana(1, "das", "da"))
        self.__repository_persoane.adauga(Persoana(2, "das", "da"))
        self.__repository_evenimente.adauga(Eveniment(1, "01.01.2023", "00:00", "a"))
        self.__repository_evenimente.adauga(Eveniment(2, "01.01.2023", "00:00", "a"))
        self.__repository_evenimente.adauga(Eveniment(3, "01.01.2023", "00:00", "a"))
        self.__service_inscrieri.adauga_inscriere(1, 1)
        self.__service_inscrieri.adauga_inscriere(1, 2)
        self.__service_inscrieri.adauga_inscriere(2, 2)
        lista_evenimente = self.__service_inscrieri.evenimente_multe_inscrieri()
        self.assertEqual(lista_evenimente[0].get_id(), 2)
        self.assertEqual(lista_evenimente[0].get_nr_inscrieri(), 2)
        self.assertEqual(lista_evenimente[1].get_id(), 1)
        self.assertEqual(lista_evenimente[1].get_nr_inscrieri(), 1)
        self.assertEqual(lista_evenimente[2].get_id(), 3)
        self.assertEqual(lista_evenimente[2].get_nr_inscrieri(), 0)

class TesteServicePersoaneFisier(unittest.TestCase):
    def setUp(self):
        self.file_persoane = open("teste_persoane_fisier.txt", "w")
        self.__repository_persoane = RepositoryPersoaneFiles("teste_persoane_fisier.txt")
        self.__validator_persoana = ValidatorPersoana()
        self.__service_persoane = ServicePersoane(self.__validator_persoana, self.__repository_persoane)

    def tearDown(self):
        self.file_persoane.close()

    def testA(self):
        self.assertEqual(len(self.__repository_persoane), 0)
        self.__service_persoane.adauga_persoana(3, "Andrei", "Str Tipografiei, nr. 3")
        self.assertEqual(len(self.__repository_persoane), 1)

    def testB(self):
        self.__service_persoane.adauga_persoana(3, "Andrei", "Str Tipografiei, nr. 3")
        self.__service_persoane.sterge_persoana(3)
        self.assertEqual(len(self.__repository_persoane), 0)

    def testC(self):
        self.__service_persoane.adauga_persoana(3, "Andrei", "Str Tipografiei, nr. 3")
        self.__service_persoane.adauga_persoana(4, "Simion", "Str Marului")
        self.assertEqual(self.__service_persoane.get_persoane()[0].get_person_id(), 3)
        self.assertEqual(self.__service_persoane.get_persoane()[0].get_nume(), "Andrei")
        self.assertEqual(self.__service_persoane.get_persoane()[0].get_adresa(), "Str Tipografiei, nr. 3")
        self.assertEqual(self.__service_persoane.get_persoane()[1].get_person_id(), 4)
        self.assertEqual(self.__service_persoane.get_persoane()[1].get_nume(), "Simion")
        self.assertEqual(self.__service_persoane.get_persoane()[1].get_adresa(), "Str Marului")

    def testD(self):
        self.__service_persoane.adauga_persoana(3, "Andrei", "Str Tipografiei, nr. 3")
        self.__service_persoane.modifica_persoana(3, "Simion", "Str Marului")
        self.assertEqual(self.__service_persoane.get_persoane()[0].get_person_id(), 3)
        self.assertEqual(self.__service_persoane.get_persoane()[0].get_nume(), "Simion")
        self.assertEqual(self.__service_persoane.get_persoane()[0].get_adresa(), "Str Marului")

    def testE(self):
        self.__service_persoane.adauga_persoana(3, "Andrei", "Str Tipografiei, nr. 3")
        persoana_gasita = self.__service_persoane.cauta_persoana(3)
        self.assertEqual(persoana_gasita.get_person_id(), 3)
        self.assertEqual(persoana_gasita.get_nume(), "Andrei")
        self.assertEqual(persoana_gasita.get_adresa(), "Str Tipografiei, nr. 3")

    def testF(self):
        nr_persoane = random.randrange(20, 50)
        self.__service_persoane.adauga_persoane_random(nr_persoane)
        self.assertEqual(len(self.__repository_persoane), nr_persoane)


class TesteServiceEvenimenteFisier(unittest.TestCase):
    def setUp(self):
        self.file_evenimente = open("teste_evenimente_fisier.txt", "w")
        self.__repository_evenimente = RepositoryEvenimenteFiles("teste_evenimente_fisier.txt")
        self.__validator_eveniment = ValidatorEveniment()
        self.__service_evenimente = ServiceEvenimente(self.__validator_eveniment, self.__repository_evenimente)

    def tearDown(self):
        self.file_evenimente.close()

    def testA(self):
        self.assertEqual(len(self.__repository_evenimente), 0)
        self.__service_evenimente.adauga_eveniment(3, "17.10.2021", "22:30", "Zi de nastere")
        self.assertEqual(len(self.__repository_evenimente), 1)

    def testB(self):
        self.__service_evenimente.adauga_eveniment(3, "17.10.2021", "22:30", "Zi de nastere")
        self.__service_evenimente.sterge_eveniment(3)
        self.assertEqual(len(self.__repository_evenimente), 0)

    def testC(self):
        self.__service_evenimente.adauga_eveniment(3, "17.10.2021", "22:30", "Zi de nastere")
        self.__service_evenimente.adauga_eveniment(4, "13.12.2021", "15:00", "Aniversare")
        self.assertEqual(self.__service_evenimente.get_evenimente()[0].get_event_id(), 3)
        self.assertEqual(self.__service_evenimente.get_evenimente()[0].get_data(), "17.10.2021")
        self.assertEqual(self.__service_evenimente.get_evenimente()[0].get_timp(), "22:30")
        self.assertEqual(self.__service_evenimente.get_evenimente()[0].get_descriere(), "Zi de nastere")
        self.assertEqual(self.__service_evenimente.get_evenimente()[1].get_event_id(), 4)
        self.assertEqual(self.__service_evenimente.get_evenimente()[1].get_data(), "13.12.2021")
        self.assertEqual(self.__service_evenimente.get_evenimente()[1].get_timp(), "15:00")
        self.assertEqual(self.__service_evenimente.get_evenimente()[1].get_descriere(), "Aniversare")

    def testD(self):
        self.__service_evenimente.adauga_eveniment(3, "17.10.2021", "22:30", "Zi de nastere")
        self.__service_evenimente.modifica_eveniment(3, "13.12.2021", "15:00", "Aniversare")
        self.assertEqual(self.__service_evenimente.get_evenimente()[0].get_event_id(), 3)
        self.assertEqual(self.__service_evenimente.get_evenimente()[0].get_data(), "13.12.2021")
        self.assertEqual(self.__service_evenimente.get_evenimente()[0].get_timp(), "15:00")
        self.assertEqual(self.__service_evenimente.get_evenimente()[0].get_descriere(), "Aniversare")

    def testE(self):
        self.__service_evenimente.adauga_eveniment(3, "17.10.2021", "22:30", "Zi de nastere")
        eveniment_gasit = self.__service_evenimente.cauta_eveniment(3)
        self.assertEqual(eveniment_gasit.get_event_id(), 3)
        self.assertEqual(eveniment_gasit.get_data(), "17.10.2021")
        self.assertEqual(eveniment_gasit.get_timp(), "22:30")
        self.assertEqual(eveniment_gasit.get_descriere(), "Zi de nastere")

    def testF(self):
        nr_evenimente = random.randrange(20, 50)
        self.__service_evenimente.adauga_evenimente_random(nr_evenimente)
        self.assertEqual(len(self.__repository_evenimente), nr_evenimente)


class TesteServiceInscrieriFisier(unittest.TestCase):
    def setUp(self):
        self.file_persoane = open("teste_persoane_fisier.txt", "w")
        self.__repository_persoane = RepositoryPersoaneFiles("teste_persoane_fisier.txt")
        self.file_evenimente = open("teste_evenimente_fisier.txt", "w")
        self.__repository_evenimente = RepositoryEvenimenteFiles("teste_evenimente_fisier.txt")
        self.file_inscrieri = open("teste_inscrieri_fisier.txt", "w")
        self.__repository_inscrieri = RepositoryInscrieriFiles("teste_inscrieri_fisier.txt")
        self.__service_inscrieri = ServiceInscrieri(self.__repository_persoane, self.__repository_evenimente, self.__repository_inscrieri)
    
    def tearDown(self):
        self.file_persoane.close()
        self.file_evenimente.close()
        self.file_inscrieri.close()
    
    def testA(self):
        self.__repository_persoane.adauga(Persoana(3, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(3, "17.10.2021", "22:30", "Zi de nastere"))
        self.__service_inscrieri.adauga_inscriere(3, 3)
        self.assertEqual(len(self.__repository_inscrieri), 1)

    def testB(self):
        self.__repository_persoane.adauga(Persoana(3, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(3, "17.10.2021", "22:30", "Zi de nastere"))
        self.__service_inscrieri.adauga_inscriere(3, 3)
        self.__service_inscrieri.sterge_inscriere(3, 3)
        self.assertEqual(len(self.__repository_inscrieri), 0)

    def testC(self):
        self.__repository_persoane.adauga(Persoana(3, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(3, "17.10.2021", "22:30", "Zi de nastere"))
        self.__repository_persoane.adauga(Persoana(4, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(4, "17.10.2021", "22:30", "Zi de nastere"))
        self.__service_inscrieri.adauga_inscriere(3, 3)
        self.__service_inscrieri.adauga_inscriere(4, 4)
        self.__service_inscrieri.sterge_persoana_inscrieri(3)
        self.assertEqual(len(self.__repository_inscrieri), 1)

    def testD(self):
        self.__repository_persoane.adauga(Persoana(3, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(3, "17.10.2021", "22:30", "Zi de nastere"))
        self.__repository_persoane.adauga(Persoana(4, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(4, "17.10.2021", "22:30", "Zi de nastere"))
        self.__service_inscrieri.adauga_inscriere(3, 3)
        self.__service_inscrieri.adauga_inscriere(4, 4)
        self.__service_inscrieri.sterge_eveniment_inscrieri(3)
        self.assertEqual(len(self.__repository_inscrieri), 1)

    def testE(self):
        self.__repository_persoane.adauga(Persoana(3, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(3, "17.10.2021", "22:30", "Zi de nastere"))
        self.__service_inscrieri.adauga_inscriere(3, 3)
        lista_inscrieri = self.__service_inscrieri.get_inscrieri()
        self.assertEqual(lista_inscrieri[0].get_persoana().get_person_id(), 3)
        self.assertEqual(lista_inscrieri[0].get_persoana().get_nume(), "Andrei")
        self.assertEqual(lista_inscrieri[0].get_persoana().get_adresa(), "Str Tipografiei, nr. 3")
        self.assertEqual(lista_inscrieri[0].get_eveniment().get_event_id(), 3)
        self.assertEqual(lista_inscrieri[0].get_eveniment().get_data(), "17.10.2021")
        self.assertEqual(lista_inscrieri[0].get_eveniment().get_timp(), "22:30")
        self.assertEqual(lista_inscrieri[0].get_eveniment().get_descriere(), "Zi de nastere")

    def testG(self):
        self.__repository_persoane.adauga(Persoana(3, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(3, "17.10.2021", "22:30", "Zi de nastere"))
        self.__service_inscrieri.adauga_inscriere(3, 3)
        self.__service_inscrieri.modifica_persoana_inscrieri(3, "Simion", "Str, Marului")
        lista_inscrieri = self.__service_inscrieri.get_inscrieri()
        self.assertEqual(lista_inscrieri[0].get_persoana().get_person_id(), 3)
        self.assertEqual(lista_inscrieri[0].get_persoana().get_nume(), "Simion")
        self.assertEqual(lista_inscrieri[0].get_persoana().get_adresa(), "Str, Marului")

    def testH(self):
        self.__repository_persoane.adauga(Persoana(3, "Andrei", "Str Tipografiei, nr. 3"))
        self.__repository_evenimente.adauga(Eveniment(3, "17.10.2021", "22:30", "Zi de nastere"))
        self.__service_inscrieri.adauga_inscriere(3, 3)
        self.__service_inscrieri.modifica_eveniment_inscrieri(3, "13.10.2023", "10:00", "Nunta")
        lista_inscrieri = self.__service_inscrieri.get_inscrieri()
        self.assertEqual(lista_inscrieri[0].get_eveniment().get_event_id(), 3)
        self.assertEqual(lista_inscrieri[0].get_eveniment().get_data(), "13.10.2023")
        self.assertEqual(lista_inscrieri[0].get_eveniment().get_timp(), "10:00")
        self.assertEqual(lista_inscrieri[0].get_eveniment().get_descriere(), "Nunta")

    def testI(self):
        self.__repository_persoane.adauga(Persoana(1, "das", "da"))
        self.__repository_evenimente.adauga(Eveniment(1, "01.01.2023", "00:00", "a"))
        self.__repository_evenimente.adauga(Eveniment(2, "10.01.2022", "00:00", "a"))
        self.__repository_evenimente.adauga(Eveniment(3, "09.10.2022", "00:00", "aa"))
        self.__repository_evenimente.adauga(Eveniment(4, "09.11.2021", "00:00", "aa"))
        self.__repository_evenimente.adauga(Eveniment(5, "13.10.2021", "00:00", "aaa"))
        self.__repository_evenimente.adauga(Eveniment(6, "09.10.2021", "00:00", "aaa"))
        self.__repository_evenimente.adauga(Eveniment(7, "10.10.2021", "00:00", "aaaaz"))
        self.__repository_evenimente.adauga(Eveniment(8, "10.11.2021", "00:00", "aaaa"))
        self.__service_inscrieri.adauga_inscriere(1, 1)
        self.__service_inscrieri.adauga_inscriere(1, 2)
        self.__service_inscrieri.adauga_inscriere(1, 3)
        self.__service_inscrieri.adauga_inscriere(1, 4)
        self.__service_inscrieri.adauga_inscriere(1, 5)
        self.__service_inscrieri.adauga_inscriere(1, 6)
        self.__service_inscrieri.adauga_inscriere(1, 7)
        self.__service_inscrieri.adauga_inscriere(1, 8)
        lista_evenimente = self.__service_inscrieri.lista_evenimente_persoana(Persoana(1, "das", "da"))
        self.assertEqual(lista_evenimente, [Eveniment(2, "01.01.2023", "00:00", "a"),
                                            Eveniment(1, "01.01.2023", "00:00", "a"),
                                            Eveniment(4, "01.01.2023", "00:00", "a"),
                                            Eveniment(3, "01.01.2023", "00:00", "a"),
                                            Eveniment(6, "01.01.2023", "00:00", "a"),
                                            Eveniment(5, "01.01.2023", "00:00", "a"),
                                            Eveniment(8, "01.01.2023", "00:00", "a"),
                                            Eveniment(7, "01.01.2023", "00:00", "a")])

    def testJ(self):
        self.__repository_persoane.adauga(Persoana(1, "das", "da"))
        self.__repository_evenimente.adauga(Eveniment(1, "01.01.2023", "00:00", "a"))
        lista_evenimente = self.__service_inscrieri.lista_evenimente_persoana(Persoana(1, "das", "da"))
        self.assertEqual(lista_evenimente, [])

    def testK(self):
        self.__repository_persoane.adauga(Persoana(1, "das", "da"))
        self.__repository_persoane.adauga(Persoana(2, "das", "da"))
        self.__repository_persoane.adauga(Persoana(3, "das", "da"))
        self.__repository_evenimente.adauga(Eveniment(1, "01.01.2023", "00:00", "a"))
        self.__repository_evenimente.adauga(Eveniment(2, "01.01.2023", "00:00", "a"))
        self.__service_inscrieri.adauga_inscriere(1, 1)
        self.__service_inscrieri.adauga_inscriere(2, 1)
        self.__service_inscrieri.adauga_inscriere(2, 2)
        lista_persoane = self.__service_inscrieri.persoane_multe_inscrieri()
        self.assertEqual(lista_persoane[0].get_id(), 2)
        self.assertEqual(lista_persoane[0].get_nr_inscrieri(), 2)
        self.assertEqual(lista_persoane[1].get_id(), 1)
        self.assertEqual(lista_persoane[1].get_nr_inscrieri(), 1)
        self.assertEqual(lista_persoane[2].get_id(), 3)
        self.assertEqual(lista_persoane[2].get_nr_inscrieri(), 0)

    def testL(self):
        self.__repository_persoane.adauga(Persoana(1, "das", "da"))
        self.__repository_persoane.adauga(Persoana(2, "das", "da"))
        self.__repository_evenimente.adauga(Eveniment(1, "01.01.2023", "00:00", "a"))
        self.__repository_evenimente.adauga(Eveniment(2, "01.01.2023", "00:00", "a"))
        self.__repository_evenimente.adauga(Eveniment(3, "01.01.2023", "00:00", "a"))
        self.__service_inscrieri.adauga_inscriere(1, 1)
        self.__service_inscrieri.adauga_inscriere(1, 2)
        self.__service_inscrieri.adauga_inscriere(2, 2)
        lista_evenimente = self.__service_inscrieri.evenimente_multe_inscrieri()
        self.assertEqual(lista_evenimente[0].get_id(), 2)
        self.assertEqual(lista_evenimente[0].get_nr_inscrieri(), 2)
        self.assertEqual(lista_evenimente[1].get_id(), 1)
        self.assertEqual(lista_evenimente[1].get_nr_inscrieri(), 1)
        self.assertEqual(lista_evenimente[2].get_id(), 3)
        self.assertEqual(lista_evenimente[2].get_nr_inscrieri(), 0)

class BlackBox(unittest.TestCase):
    # blackbox testing pentru functionalitatea de returnare a unei liste de frecventa de tipul:
    # [[persoana_id, nr_inscrieri_persoana], ... ] pentru persoanele inscrise in obiectul de clasa RepositoryPersoane,
    # cu lucrul in memorie, dar si in fisier
    # versiunea whitebox: linia - 952 + 1197
    def testA(self):
        self.__repository_persoane = RepositoryPersoane()
        self.__repository_evenimente = RepositoryEvenimente()
        self.__repository_inscrieri = RepositoryInscrieri()
        self.__repository_persoane = RepositoryPersoane()
        self.__repository_evenimente = RepositoryEvenimente()
        self.__service_inscrieri = ServiceInscrieri(self.__repository_persoane, self.__repository_evenimente,
                                                    self.__repository_inscrieri)

        self.__repository_persoane.adauga(Persoana(1, "das", "da"))
        self.__repository_persoane.adauga(Persoana(2, "das", "da"))
        self.__repository_evenimente.adauga(Eveniment(1, "01.01.2023", "00:00", "a"))
        self.__service_inscrieri.adauga_inscriere(1, 1)
        self.__service_inscrieri.adauga_inscriere(2, 1)
        lista_persoane = self.__service_inscrieri.persoane_multe_inscrieri()
        self.assertEqual(lista_persoane[0].get_id(), 1)
        self.assertEqual(lista_persoane[0].get_nr_inscrieri(), 1)
        self.assertEqual(lista_persoane[1].get_id(), 2)
        self.assertEqual(lista_persoane[1].get_nr_inscrieri(), 1)

    def testB(self):
        self.file_persoane = open("teste_persoane_fisier.txt", "w")
        self.__repository_persoane = RepositoryPersoaneFiles("teste_persoane_fisier.txt")
        self.file_evenimente = open("teste_evenimente_fisier.txt", "w")
        self.__repository_evenimente = RepositoryEvenimenteFiles("teste_evenimente_fisier.txt")
        self.file_inscrieri = open("teste_inscrieri_fisier.txt", "w")
        self.__repository_inscrieri = RepositoryInscrieriFiles("teste_inscrieri_fisier.txt")
        self.__service_inscrieri = ServiceInscrieri(self.__repository_persoane, self.__repository_evenimente,
                                                    self.__repository_inscrieri)

        self.__repository_persoane.adauga(Persoana(1, "das", "da"))
        self.__repository_persoane.adauga(Persoana(2, "das", "da"))
        self.__repository_evenimente.adauga(Eveniment(1, "01.01.2023", "00:00", "a"))
        self.__service_inscrieri.adauga_inscriere(1, 1)
        self.__service_inscrieri.adauga_inscriere(2, 1)
        lista_persoane = self.__service_inscrieri.persoane_multe_inscrieri()
        self.assertEqual(lista_persoane[0].get_id(), 1)
        self.assertEqual(lista_persoane[0].get_nr_inscrieri(), 1)
        self.assertEqual(lista_persoane[1].get_id(), 2)
        self.assertEqual(lista_persoane[1].get_nr_inscrieri(), 1)

        self.file_persoane.close()
        self.file_evenimente.close()
        self.file_inscrieri.close()


if __name__ == '__main__':
    unittest.main()
