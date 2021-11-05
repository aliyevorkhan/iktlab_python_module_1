m_suret = int(input("Masinin sureti[KM/SAAT]: "))

if m_suret < 240:
    mesafe = int(input("Qet edeceyi mesafe[KM]: "))
    if mesafe > 0:
        muddet = mesafe/m_suret
        print("Muddet: {} saat".format(muddet))
    else:
        print("Mesafe menfi olabilmez!")
else:
    print("Bele bir suret yoxdur!")