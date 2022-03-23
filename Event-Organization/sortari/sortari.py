class Sort:

    def __for_key(self, element, key):
        # folosind key (care reprezinta o functia/metoda care returneaza o valoare ca si cheie de ordonare), se
        # returneaza valoarea dupa care are lor ordonarea
        # ex : key = Eveniment.get_descriere, element = eveniment => returneaza descrierea evenimentului dat
        return key(element)

    def bubble_sort(self, lista, l=0, r=-1, key=lambda x: x, key2=0, cmp=lambda x, y: x > y, cmp2=lambda x, y: x == y, reverse=False):
        if r == -1:
            r = len(lista)
        sort = False
        if not key2:
            while not sort:
                sort = True
                for i in range(l, r - 1):
                    if (cmp(self.__for_key(lista[i], key), self.__for_key(lista[i + 1], key)) and reverse == False) or (
                            cmp(self.__for_key(lista[i + 1], key), self.__for_key(lista[i], key)) and reverse == True):
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        sort = False
        else:
            while not sort:
                sort = True
                for i in range(l, r - 1):
                    if (cmp(self.__for_key(lista[i], key), self.__for_key(lista[i + 1], key)) and reverse == False) or \
                            (cmp(self.__for_key(lista[i], key2), self.__for_key(lista[i + 1], key2)) and
                             cmp2(self.__for_key(lista[i], key),
                                  self.__for_key(lista[i + 1], key)) and reverse == False) or \
                            (cmp(self.__for_key(lista[i + 1], key),
                                 self.__for_key(lista[i], key)) and reverse == True) or \
                            (cmp(self.__for_key(lista[i + 1], key2), self.__for_key(lista[i], key2)) and
                             cmp2(self.__for_key(lista[i], key),
                                  self.__for_key(lista[i + 1], key)) and reverse == True):
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        sort = False

    def comb_sort(self, lista, l=0, r=-1, key=lambda x: x, cmp=lambda x, y: x > y, reverse=False):
        if r == -1:
            r = len(lista)
        gap = r - l
        sort = False
        while not sort or gap > 1:
            gap = max(1, int(gap / 1.3))
            sort = True
            for i in range(l, r - gap):
                if (cmp(self.__for_key(lista[i], key), self.__for_key(lista[i + gap], key)) and reverse == False) or (
                        cmp(self.__for_key(lista[i + gap], key), self.__for_key(lista[i], key)) and reverse == True):
                    lista[i], lista[i + gap] = lista[i + gap], lista[i]
                    sort = False

    def bubble_sort_old(self, lista, l=0, r=-1, key=lambda x: x, cmp=lambda x, y: x > y, reverse=False):
        if r == -1:
            r = len(lista)
        sort = False
        while not sort:
            sort = True
            for i in range(l, r - 1):
                if (cmp(self.__for_key(lista[i], key), self.__for_key(lista[i + 1], key)) and reverse == False) or (cmp(self.__for_key(lista[i + 1], key), self.__for_key(lista[i], key)) and reverse == True):
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    sort = False
