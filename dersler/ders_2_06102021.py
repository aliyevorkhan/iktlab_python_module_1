print(bool(True))
print(bool(False))
print(bool(""))
print(bool(" "))
print(bool())
print(bool(None))

hec_ne = None
print(hec_ne, type(hec_ne))

sifir = 0.0
print(sifir, type(sifir))


#**************************
print("Xos gelmisiniz!")

#ad = input("Zehmet olmasa adiniz daxil edin: ")
#soyad = input("Zehmet olmasa soyadiniz daxil edin: ")
yas = int(input("Zehmet olmasa yasinizi daxil edin: "))
#yasadigi_seher = input("Zehmet olmasa yasadiginiz seheri daxil edin: ")

#print("Xos gelmisen "+ad)
toplam = 20 + yas
print(toplam, type(toplam))

#print(ad+"/"+soyad+"_"+yasadigi_seher)

#print("*_*"*50)
#print('\n'*8)

a, b, c = 5, 4, 10

print(a, b, c)
#***************

a = 100
b = 100

if a<b:
	print("a kicikdir b")
	print(a,b)
elif False:
	print("a beraberdir b")
else:
	print("a boyukdur b")

print("if in xarici")
