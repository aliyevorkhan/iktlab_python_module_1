import random

print(random.random())
print(random.randint(1,10))
mylist=[5, 4, 7, 8, 11]
print(random.choice(mylist))
print(random.choice('ikt-lab dersleri'))

print(mylist) #evvelki hali
random.shuffle(mylist) #qarisdir
print(mylist) #sonraki hali