def filtreaza_numere(lista_originala):

    even_list = list(filter(lambda x: x % 2 == 0, lista_originala))
    odd_list = list(filter(lambda x: x % 2 != 0, lista_originala))

    return even_list, odd_list
orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pare, impare = filtreaza_numere(orig_list)
print(f"Original List: {orig_list}")
print(f"Even List:     {pare}")
print(f"Odd List:      {impare}")