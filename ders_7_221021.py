#STRINGIN BUTUN HERFLERINI BOYUTMEK
a = "Hello, World!"
print(a.upper())

#STRINGIN BUTUN HERFLERINI KICILTMEK
a = "Hello, World!"
print(a.lower())

#STRINGIN BASINDA VE SONUNDAKI BOSLUQLARI SILIR
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#VERILEN PATTERN'I BASQA PATTERN ILE DEYISDIRMEK
a = "Hello, World!"
print(a.replace("H", "J"))

#STRINGIN PARCALARA AYIRMAQ
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#STRINGIN ICINDE SPESIFIK YERLERE DEYERLER YERLESDIRMEK
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#YUXARIDAKI NUMUNENIN INDEKSLI SEKLI
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#ESCAPE CHARACTER ISTIFADESI
txt = "We are the so-called \"Vikings\" from the north."

#FOR LOOP ISTIFADESI: LISTLERLE
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#FOR LOOP ISTIFADESI: STRING ILE
for x in "banana":
  print(x)
  
#FOR LOOP'DA BREAK ISTIFADESI
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
    
#FOR LOOP'DA CONTINUE ISTIFADESI
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#FOR LOOP RANGE ILE ISTIFADESI: 0 ile 6 arasindaki butun deyerler
for x in range(6):
  print(x)

#FOR LOOP RANGE ILE ISTIFADESI: 2 den 6 ya qeder butun deyerler(6 daxil deyil)
for x in range(2, 6):
  print(x)
  
#FOR LOOP RANGE ILE ISTIFADESI: 2 den 30 a qeder(deyerler 3-3 artacaq)
for x in range(2, 30, 3):
  print(x)
  
#FOR IC ICE LOOP
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
#FOR LOOP'DA LIST ISTIFADESI XUSUSI NUMUNE
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
#WHILE LOOP'DA LIST ISTIFADESI XUSUSI NUMUNE
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
#LISTLERDE TEK SETIRDE LOOP NUMUNESI
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#LIST'LERDE LOOP ISTIFADESI NUMUNESI
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
    
#TEK SETIRDE LIST LOOP NUMUNESI IF SERTI ILE
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#TEK SETIRDE LIST LOOP NUMUNESI IF/ELSE SERTI ILE
newlist = [x if x != "banana" else "orange" for x in fruits]
    
