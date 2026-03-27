def ridica_la_patrat(lista_input):
    rezultat = list(map(lambda x: x**2, lista_input))
    return rezultat
my_list = [1, 2, 3, 4, 5]
lista_finala = ridica_la_patrat(my_list)
print(f"Input:  {my_list}")
print(f"Output: {lista_finala}")