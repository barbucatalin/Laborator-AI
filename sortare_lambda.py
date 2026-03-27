def sorteaza_dupa_al_doilea_element(lista_tupluri):

    lista_sortata = sorted(lista_tupluri, key=lambda x: x[1])
    return lista_sortata

a = [(0, 2), (4, 3), (9, 9), (10, -1)]


sorted_a = sorteaza_dupa_al_doilea_element(a)


print("Lista originală:", a)
print("Lista sortată (după al doilea element):", sorted_a)