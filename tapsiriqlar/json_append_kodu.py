import json
import time

musteri_info = {"ad":"orkhan", "soyad":"aliyev"}

def write_data(filename,data):
    f = open(filename, "w")
    json.dump(data, f, indent=4)
    f.close()

def read_data(filename):
    f1 = open(filename, "r")
    data = json.load(f1)
    return data

def check_file(filename):
    f = open(filename, "r")
    if f.read(): # dolu -> True
        return True
    else: # bos -> False
        return False
    
if __name__ == "__main__":
    if check_file("sample_file.json"): #doludursa
        data = read_data("sample_file.json")
        data[str(int(time.time()))] = musteri_info
        write_data("sample_file.json", data)
        print("dolu fayla elave edildi")
    else: #bosdursa
        write_data("sample_file.json", {str(int(time.time())): musteri_info})
        print("bos fayl dolduruldu")
