def rezolva_list_comprehension():
 
    pare = [x for x in range(101) if x % 2 == 0]

    cuburi = [x ** 3 for x in range(10)]


    lista_a = [1, 2, 3, 4, 5, 8]
    lista_b = [3, 4, 5, 6, 7, 8]
    comune = [x for x in lista_a if x in lista_b]


    print("1. Numere pare (0-100):", pare)
    print("\n2. Cuburile primelor 10 numere:", cuburi)
    print("\n3. Elemente comune:", comune)


if __name__ == "__main__":
    rezolva_list_comprehension()