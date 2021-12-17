while True:
    print("*"*15)
    print("ZEHMET OLMASA BIR SAYI DAXIL EDIN")
    print("*"*15)
    sayi = int(input("SAYI: "))
    if sayi%2 == 0 and sayi != 0:
        print("SAYI CUT SAYIDIR!")
    elif sayi%2 != 0:
        print("SAYI TEK SAYIDIR!")
    else:
        print("SIZ PROGRAMDAN CIXIRSINIZ")
        break