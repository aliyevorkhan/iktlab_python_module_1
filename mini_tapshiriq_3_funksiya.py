def tek_cut_yoxla(s):
    if s%2 == 0 and s != 0:
        print("SAYI CUT SAYIDIR!")
    elif s%2 != 0:
        print("SAYI TEK SAYIDIR!")
    
def tek_cut_yoxla_r(s):
    # cutdurse True
    # tekdirse False
    netice = False
    if s%2 == 0 and s != 0:
        netice = True
    elif s%2 != 0:
        netice = False
    return netice

while True:
    print("*"*15)
    print("ZEHMET OLMASA BIR SAYI DAXIL EDIN")
    print("*"*15)
    sayi = int(input("SAYI: "))
    if sayi==0:
        print("SIZ PROGRAMDAN CIXIRSINIZ")
        break
    
    cutdurMu = tek_cut_yoxla_r(sayi)
    if cutdurMu:
        print("cutdur")
    else:
        print("tekdir")
    
    
    