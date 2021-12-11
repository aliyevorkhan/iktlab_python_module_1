from Telebe import Telebe

class Isci(Telebe):
    def __init__(self, ad="NO_DATA", soyad="NO_DATA", 
            dogum_tarixi="NO_DATA", kilo=0, boy=0, cins="NO_DATA", 
            telebe_nom="NO_DATA", qrup_nom="NO_DATA", ortalama=0, giris_ili=0,
            maas=0.0, baslama_ili=0, tecrube_ili=0, xercler=0.0):
        super().__init__(ad=ad, soyad=soyad, dogum_tarixi=dogum_tarixi, kilo=kilo, 
                    boy=boy, cins=cins, telebe_nom=telebe_nom, qrup_nom=qrup_nom, 
                    ortalama=ortalama, giris_ili=giris_ili)
        self.maas = maas
        self.xercler = xercler
        self.baslama_ili = baslama_ili
        self.tecrube_ili = tecrube_ili
        self.bonus = self.maas*0.5 

    def print_isci(self):
        self.print_telebe()
        print("MAAS: {}\nBONUS: {}\nXERCLER: {}".format(self.maas, self.bonus,self.xercler))
        print("ISE_BASLAMA_ILI: {}\nTECRUBE_ILI: {}".format(self.baslama_ili, self.tecrube_ili))
        print("*"*50)

    def isle(self):
        self.kilo -= self.kilo*0.01
        self.tecrube_ili += 1
        print("KILO AZALDI: {}\nTECRUBE_ILI ARTTI: {}".format(self.kilo, self.tecrube_ili))

if __name__=='__main__':
    isci1 = Isci("Ali", "Aliyev", "01/01/1990", 70, 180, "K", "994455", 
                    "A777", 50, 2019, 2000, 2005, 15, 800)
    isci1.print_isci()
    isci1.isle()