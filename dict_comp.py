def rezolva_dict_comprehension():

    patrate = {x: x ** 2 for x in range(1, 11)}


    text = "inteligența artificială"

    frecventa_litere = {char: text.count(char) for char in text if char.isalpha()}

    divizori = {x: [d for d in range(1, x + 1) if x % d == 0] for x in range(1, 11)}


    print("1. Numere și pătrate:", patrate)
    print("\n2. Frecvență litere:", frecventa_litere)
    print("\n3. Numere și divizori:", divizori)


if __name__ == "__main__":
    rezolva_dict_comprehension()