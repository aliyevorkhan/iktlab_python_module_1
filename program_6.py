maas = int(input("Maasi daxil edin: ")) 
faiz_derecesi = int(input("Faiz derecesini daxil edin: "))

print("Hesablanir...")
netice = (maas * faiz_derecesi) / 100
print("Sizin odemeli oldugunuz vergi: {}".format(netice))
