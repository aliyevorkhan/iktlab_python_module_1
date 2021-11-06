a = [1, 2, 3]

for i in a:
    for j in a:
        for k in a:
            if (i!=j and j!=k and i!=k):
                print(i, j, k)