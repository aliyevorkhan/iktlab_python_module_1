class Insan:
    def __init__(self, ad="NO_DATA", soyad="NO_DATA", dogum_tarixi="NO_DATA", kilo=0.0, boy=0.0, cins="NO_DATA"):
        self.ad = ad #str
        self.soyad = soyad #str
        self.dogum_tarixi = dogum_tarixi #str
        self.kilo = kilo #float -> kq.q
        self.boy = boy #float -> sm.mm
        self.cins = cins #str -> K/Q

    def print_insan(self):
        print("*"*50)
        print("AD: {}\nSOYAD: {}\nDOGUM_TARIXI: {}\nKILO: {}".format(self.ad, self.soyad,self.dogum_tarixi,self.kilo))
        print("BOY: {}\nCINS: {}".format(self.boy, self.cins))
        print("*"*50)

    def qidalan(self):
        self.kilo = self.kilo * 0.02 + self.kilo
        print("{} {} {} kq'a kokeldi".format(self.ad, self.soyad, self.kilo))

    def idman_et(self):
        self.kilo = self.kilo - self.kilo * 0.03
        self.boy += self.boy * 0.02 
        print("{} {} {} kq'a ariqladi".format(self.ad, self.soyad, self.kilo))
        print("{} {} {} sm'a boyu artti".format(self.ad, self.soyad, self.boy))

    def yat(self):
        self.kilo += self.kilo * 0.01
        self.boy += self.boy * 0.01
        print("{} {} {} kq'a kokeldi".format(self.ad, self.soyad, self.kilo))
        print("{} {} {} sm'a boyu artti".format(self.ad, self.soyad, self.boy))

if __name__ == '__main__':
    i1 = Insan("Ali", "Aliyev", "01/01/1990", 77.8, 177.8, "K")
    i1.print_insan()
    i1.qidalan()
    i1.idman_et()
    i1.yat()
    i1.idman_et()
    i1.qidalan()
    print("*"*50)
