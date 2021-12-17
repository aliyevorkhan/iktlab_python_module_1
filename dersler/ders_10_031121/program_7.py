list_1 = [3, 7, 9, 1, 0]

toplam = 0
for i in list_1:
    toplam = toplam + i
    print(toplam)
print(toplam, type(toplam))

ortalama = toplam/len(list_1)
print(ortalama, type(ortalama))