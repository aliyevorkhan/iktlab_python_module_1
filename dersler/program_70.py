m_suret = int(input("Masinin sureti[KM/SAAT]: "))
mesafe = int(input("Qet edeceyi mesafe[KM]: "))

if m_suret < 240 and mesafe>0:
    muddet = mesafe/m_suret
    print("Muddet: {} saat".format(muddet))
else:
    print("Bele bir suret ola bilmez!")