from utils import *
from colorama import Fore, Back, Style,init
init(autoreset=True)
con = create_connection()
create_table(con)

while True:
    print("*******MENU*******")
    print("TODO DAXIL ET   [1]")
    print("TODOLARI GOSTER [2]")
    print("TODO SIL        [3]")
    print("TODO YENILE     [4]")
    print("STATUS DEYISDIR [5]")

    choice = int(input("SECIMINIZ: "))

    if choice == 1:
        rows = select(con)
        print(rows)
        
        if len(rows) == 0:
            new_id = 1
        else:
            new_id = rows[-1][0] + 1
        
        title = input("TODO basligi ne olsun: ")
        description = input("TODO aciqlamasi ne olsun: ")
        deadline = input("TODO bitis tarixi ne olsun: ")

        infos = (new_id, title, description, 0, deadline)
        insert(con, infos)
    elif choice == 2:
        rows = select(con)
        for row in rows:
            if row[3] == 0:
                print(Fore.RED + str(row))
            else:
                print(Fore.GREEN + str(row))

    elif choice == 3:
        rows = select(con)
        for row in rows:
            print(row)

        id = int(input("Silinecek TODOnun id'si: "))
        delete(con, id)
    elif choice == 4:
        rows = select(con)
        for row in rows:
            print(row)

        id = int(input("Yenilenecek TODOnun id'si: "))
        row = select_by_id(con, id)
        print(row)
        info = list(row[0])
        
        action = int(input("Title deyisdirilsinmi? [1/0] "))
        if action==1:
            title = input("Yeni title: ")
            info[1] = title
        
        action = int(input("Aciqlama deyisdirilsinmi? [1/0] "))
        if action==1:
            description = input("Yeni aciqlama: ")
            info[2] = description
        
        action = int(input("Bitis tarixi deyisdirilsinmi? [1/0] "))
        if action==1:
            deadline = input("Yeni bitis tarixi: ")
            info[4] = deadline
        
        print(info)
        entity = info[1:]
        entity.append(info[0])

        update(con, tuple(entity))