import random


numar_secret=int(random.randint(1,50))
incercari=0
print("Am ales un numar intre 1 si 50")
int(input("am incercat numarul: "))

while True:

    if numar_secret>input:
        print("numarul este mai mic")


