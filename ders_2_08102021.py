# if else baslangic
balans = 300
mebleg = int(input("zehmet olmasa cekeceyiniz miqdari daxil edin: "))

if mebleg<balans:
	balans = balans - mebleg # yeni balans	
	print("sizin yeni balansiniz: " + str(balans))

if mebleg == 100:
	balans = balans - mebleg
	print(mebleg)
elif mebleg == balans:
	balans = balans - mebleg # yeni balans	
	print("sizin yeni balansiniz: " + str(balans))
	print("balansinizi artirin!")
elif mebleg == 123456:
	print("SOS!")
else:
	print("balansinizda bu qeder mebleg yoxdur!")
  
# ************************************

a = 2
b = 330
print("A") if a > b else print("B")

# *************************************
a = 200
b = 33
c = 500
if a > b and c > a:
  print("her iki sert True")
# **************************************
a = 200
b = 33
c = 50
if a > b or c >a:
	print("sadece birinin True olmagi besdir")
# **************************************
a = 33
b = 200

if b > a:
  pass
