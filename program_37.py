im1 = 100.0
im2 = 39.9
im3 = 100

herf_dict = {
    "5": "A",
    "4": "B",
    "3": "C",
    "2": "D",
    "1": "F",
    "0": "ERROR",
}

ort = (im1 + im2 + im3)/3
if 81 <= ort <= 100:
    sistem_bali = 5
elif 61 <= ort <= 80:
    sistem_bali = 4
elif 41 <= ort <= 60:
    sistem_bali = 3
elif 21 <= ort <= 40:
    sistem_bali = 2
elif 0 <= ort <= 20:
    sistem_bali = 1
else:
    sistem_bali = 0

print("Ortalama: {}\nSistem bali: {}\nHerf bali: {}".format(ort, sistem_bali, herf_dict[str(sistem_bali)]))

