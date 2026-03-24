def joaca_joc():
    continuare = True

    while continuare:
        print("\n Joc Nou ")

        jucator1 = input("Jucător 1, alege (piatra, hartia, foarfeca): ").lower()
        jucator2 = input("Jucător 2, alege (piatra, hartia, foarfeca): ").lower()

        if jucator1 == jucator2:
            print("Este egalitate!")
        elif jucator1 == "piatra":
            if jucator2 == "foarfeca":
                print("Felicitări Jucător 1! Piatra bate foarfeca.")
            else:
                print("Felicitări Jucător 2! Hartia bate piatra.")
        elif jucator1 == "foarfeca":
            if jucator2 == "hartia":
                print("Felicitări Jucător 1! Foarfeca taie hartia.")
            else:
                print("Felicitări Jucător 2! Piatra bate foarfeca.")
        elif jucator1 == "hartia":
            if jucator2 == "piatra":
                print("Felicitări Jucător 1! Hartia bate piatra.")
            else:
                print("Felicitări Jucător 2! Foarfeca taie hartia.")
        else:
            print("Alegere invalidă. Vă rugăm să alegeți dintre: piatra, hartia, foarfeca.")


        raspuns = input("\nDoriți să începeți un nou joc? (da/nu): ").lower()
        if raspuns != "da":
            continuare = False
            print("Mulțumim pentru joc!")



joaca_joc()