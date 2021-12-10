class Heyvan:
    def __init__(self, ayaq_sayisi, tek_huceyrelidir_mi):
        self.ayaq_sayisi = ayaq_sayisi
        self.tek_huceyrelidir_mi = tek_huceyrelidir_mi

    def nefes_almaq(self):
        print("{} ayaqli nefes alir".format(self.ayaq_sayisi))

class Qus(Heyvan):
    def __init__(self, ayaq_sayisi, tek_huceyrelidir_mi, ucabilir_mi):
        super().__init__(ayaq_sayisi, tek_huceyrelidir_mi)
        self.ucabilir_mi = ucabilir_mi

    def ucmaq(self, max):
        if self.ucabilir_mi:
           print("Men ucabilen bir qusam | max_suret: {}".format(max))
        else:
           print("Men ucabilmeyen bir qusam")

class Memeli(Heyvan):
    pass

class Bakteriya(Heyvan):
    pass

q1 = Qus(2, False, True)
m1 = Memeli(4, False)
b1 = Bakteriya(0, True)

q1.nefes_almaq()
q1.ucmaq(88)
m1.nefes_almaq()
b1.nefes_almaq()