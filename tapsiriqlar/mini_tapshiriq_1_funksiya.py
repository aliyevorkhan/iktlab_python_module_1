def boyukdurMu(yas):
    boyukdur = False
    if yas>18:
        boyukdur = True
    else:
        boyukdur = False
    return boyukdur

b_m = boyukdurMu(45)

def topla(a, b):
    print(a+b)
    return a+b

def cixart(a,b):
    print("a - b = " + str(a-b))

def vur(a,b):
    print("a x b = " + str(a*b))

def bol(a, b):
    if b!=0:
        print("a / b = " + str(a/b))
    else:
        print("Xeta!!! SIFIRA BOLMEK QADAGANDIR!!!")
        
if b_m:
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
        c = topla(a,b)
        print(c)
    elif secim == 1:
        cixart(a,b)
    elif secim == 2:
        vur(a,b)
    elif secim == 3:
        bol(a,b)
    else:
        print("YANLIS SECIM ETDINIZ!")