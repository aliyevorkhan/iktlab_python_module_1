#list nece yaradilir ve istifade edilir?:
thislist = ["apple", "banana", "cherry"]
print(thislist)

#tekrarlara icaze verir, apple ve cherry kimi
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#listin uzunlugunu oyrenmek ucun len() funksiyasindan istifade edilir
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#listin icinde ferqli data tipleri olabiler
list1 = ["abc", 34, True, 40, "male"]

#listin data tipi list'dir ve type() ile oyrenebilirik
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#mueyyen data kolleksiyasini liste cevirebilerik
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#list indexlenir ve ilk element 0'dan (sifir) baslayir
thislist = ["apple", "banana", "cherry"]
print(thislist[0])

#list'in son elementi -1'den (menfi bir) baslayir
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#   0    1   2     3  -->
l=['a', 33, 0.4, True]
#  -4   -3  -2    -1  <--

#listin elementlerini verilen araliq seklinde istifadesi
#index olaraq 2den baslayir(2 daxildi), 5'e qeder(daxil deyil)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) 

#2den baslayir listin sonuna kimi
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#neqativ indexleme ile araliq istifadesi
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#listin icerisinde sorusulan elementin var olub olmamasini yoxlamaq ucun
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
#listin verilen indexdeki deyerinin deyisdirilmesi
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#listin verilen araliqdaki deyerlerinin deyisdirilmesi
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#insert() funksiyasi ile verilen indexe deyer elave etme
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append() funksiyasi ile listin sonuna deyer elave etme
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#2 listi birlesdirmek
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#listden verilen deyere sahib deyeri silmek
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#listden verilen indexdeki deyeri silmek
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#listin sonundan silmek
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#listi tamamile silmek
thislist = ["apple", "banana", "cherry"]
del thislist

#listin icini temizlemek
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

############### * STRING * ################
#stringin verilen indexdeki karakterini yazdirmaq
a = "Hello, World!"
print(a[1])

#stringin uzunlugu
a = "Hello, World!"
print(len(a))

#verilen deyerin stringin icinde var olub olmadigini yoxlamaq
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
#verilen deyerin stringin icinde var olmadigini deqiqlesdirmek
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
#verilen araliqdaki karakterleri yazdirmaq
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])


