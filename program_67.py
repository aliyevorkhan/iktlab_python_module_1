n = int(input("Sayi: "))

faktoryal = 1
for i in range(1, n+1):
    faktoryal = faktoryal * i

print("faktoryal {}!: {}".format(n, faktoryal))