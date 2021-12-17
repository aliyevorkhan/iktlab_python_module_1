# ad = input("adi daxil edin: ")
# soyad = input("soyadi daxil edin: ")

# def salamla_args(*melumatlar):
#     print("Ad: ", melumatlar[0])
#     print("Soyad: ", melumatlar[1])
# salamla_args(ad,soyad)

# def salamla(ad, soyad):
#     print("salam, xos gelmisen ", ad, soyad)
# salamla(soyad=soyad, ad=ad)

# def salamla_kwargs(**melumatlar):
#     print(melumatlar)
# yas = int(input("yasi daxil edin: "))
# tempratura = "20C"
# salamla_kwargs(fname=ad, lname=soyad, age=yas, t = tempratura)

# def salamla_default(ad="Ibrahim"):
#     print("Salam, xos gelmisen", ad)
# salamla_default("Ibrahim")
# salamla_default("Orxan")
# salamla_default("Ali")
# salamla_default()
# salamla_default("Feyyaz")

# def masinlari_goster(masinlar):
#     for m in masinlar:
#         print(m)

# masinlarim = ["Mercedes", "AUDI", "BMW"] 
# masinlari_goster(masinlar=masinlarim)      

def topla(a, b):
    c = a+b
    # return a+b

netice = topla(5, 4)

print(netice)
