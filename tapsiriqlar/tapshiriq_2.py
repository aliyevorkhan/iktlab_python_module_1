this_list = []
while True:
    print("insert <index> <val>")
    print("append <val>")
    print("remove <val>")
    print("pop <index>")
    print("clear")
    print("exit")
    emr = input("emri daxil edin: ").split()
    if emr[0] == "exit":
        break

    print(emr)
    if emr[0] == "insert":
        this_list.insert(int(emr[1]), int(emr[2]))
    elif emr[0] == "append":
        this_list.append(int(emr[1]))
    elif emr[0] == "remove":
        this_list.remove(int(emr[1]))
    elif emr[0] == "pop":
        this_list.pop(int(emr[1]))
    elif emr[0] == "clear":
        this_list.clear()
    else:
        print("YANLIS EMR")

    print(this_list)

while True:
    print("ELEMENTLERI TOPLA [0]")
    print("EKRANA YAZDIR TEK TEK [1]")
    print("ILK VE SON TOPLA [2]")
    print("SPESIFIK ARALIQ: 2 7 [3]")
    print("EXIT [4]:")

    secim = int(input("SECIM: "))
    if secim == 4:
        break
    
    if secim == 0:
        toplam = 0
        for i in this_list:
            toplam = toplam + i
        print("TOPLAM: {}".format(toplam))
    elif secim == 1:
        for i in this_list:
            print(i, end=" ")
        print()
    elif secim == 2:
        print("ilk + son = {}".format(this_list[0]+this_list[-1]))
    elif secim == 3:
        araliq = input("araligi daxil edin [1 3]: ").split()
        print(this_list[int(araliq[0]):int(araliq[1])])    
