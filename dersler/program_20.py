# deyer = input 
# eger 3'e tam ve 5'e tam bolunurse
# ekrana "TAM BOLUNUR YAZ"
# eks teqdirde "TAM BOLUNMUR YAZ"

deyer = int(input("Deyer: "))

if deyer%3==0 and deyer%5==0:
    print("TAM BOLUNUR")
else:
    print("TAM BOLUNMUR")