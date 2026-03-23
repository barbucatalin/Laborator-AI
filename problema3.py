import random


numar_secret = random.randint(1, 50)
incercari = 0

print("Am ales un număr între 1 și 50. Încearcă să-l ghicești!")

while True:

    try:
        ghicit = int(input("Introdu un număr: "))
        incercari += 1

        if ghicit < numar_secret:
            print("Numărul este mai mare!")
        elif ghicit > numar_secret:
            print("Numărul este mai mic!")
        else:
            print("Felicitări! Ai ghicit numărul {numar_secret} din {incercari} încercări!")
            break

    except ValueError:
        print("Te rog să introduci un număr valid (întreg).")