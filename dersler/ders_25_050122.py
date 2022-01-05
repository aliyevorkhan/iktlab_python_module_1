from covid import Covid
import threading
import time
from datetime import datetime
covid = Covid()

def show_az_covid():
    while True:
        for i in covid.get_data():
            if i["country"] == "Azerbaijan":
                olke = i["country"]
                tesdiqlenen = i["confirmed"]
                olum_sayisi = i["deaths"]
                son_yenileme_timestamp = i["last_update"]/1000
                son_yenileme_datetime = datetime.fromtimestamp(son_yenileme_timestamp)

                print("*"*25)
                print("Olke: {}\nTesdiqlenen: {}\nOlum sayisi: {}\nSon yenileme: {}".format(olke,tesdiqlenen,olum_sayisi,son_yenileme_datetime))
                print("*"*25)
        time.sleep(5)

threading.Thread(target=show_az_covid, args=()).start()

while True:
    print("Covid Melumatlari gozlenilir..")
    time.sleep(1)
