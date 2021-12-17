from Insan import Insan

class Telebe(Insan):
    def __init__(self, ad="NO_DATA", soyad="NO_DATA", 
                dogum_tarixi="NO_DATA", kilo=0, boy=0, 
                cins="NO_DATA", telebe_nom="NO_DATA", qrup_nom="NO_DATA", ortalama=0.0, giris_ili=0):
        super().__init__(ad=ad, soyad=soyad, dogum_tarixi=dogum_tarixi, kilo=kilo, boy=boy, cins=cins)
        self.telebe_nom = telebe_nom
        self.qrup_nom = qrup_nom
        self.ortalama = ortalama
        self.giris_ili = giris_ili
        self.bitirme_ili = giris_ili+4
    def print_telebe(self):
        self.print_insan()
        print("TELEBE_NOMRESI: {}\nQRUP_NOMRESI: {}\nORTALAMA: {}".format(self.telebe_nom, self.qrup_nom,self.ortalama))
        print("GIRIS_ILI: {}\nBITIRME_ILI: {}".format(self.giris_ili, self.bitirme_ili))
        print("*"*50)

    def imtahandan_kec(self):
        self.ortalama += self.ortalama*0.1
        print("IMTAHANDAN KECDI!\nMOVCUD ORTALAMA BALI: {}".format(self.ortalama))
    
    def imtahandan_kesil(self):
        self.ortalama -= self.ortalama*0.1
        print("IMTAHANDAN KESILDI!\nMOVCUD ORTALAMA BALI: {}".format(self.ortalama))

if __name__=='__main__':
    t1 = Telebe("Ali", "Aliyev", "01/01/1990", 70, 180, "K", "994455", "A777", 50, 2019)
    t1.print_telebe()
    t1.imtahandan_kec()
    t1.imtahandan_kec()
    t1.imtahandan_kesil()