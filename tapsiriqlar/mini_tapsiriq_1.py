print("Zehmet olmasa hesablama edeceyiniz 2 sayini daxil edin")

a = float(input("a: "))
b = float(input("b: "))

print()
print("*******************")
print("0: toplama")
print("1: cixma")
print("2: vurma")
print("3: bolme")
print("*******************")
print()

secim = int(input("Hansi riyazi emeliyyati yerine yetirmek isteyirsiniz? : "))
print()

if secim == 0:
    print("a + b = " + str(a+b))
elif secim == 1:
    print("a - b = " + str(a-b))
elif secim == 2:
    print("a x b = " + str(a*b))
elif secim == 3:
    print("a / b = " + str(a/b))
else:
    print("YANLIS SECIM ETDINIZ!")