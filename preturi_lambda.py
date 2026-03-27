def proceseaza_preturi(lista_preturi):

    lista_curata = filter(lambda x: x is not None, lista_preturi)

    lista_redusa = map(lambda x: x * 0.9, lista_curata)


    return list(lista_redusa)

preturi_originale = [100, None, 200, 50, None, 300]


rezultat_final = proceseaza_preturi(preturi_originale)

print(f"Prețuri originale: {preturi_originale}")
print(f"Prețuri reduse (fără None): {rezultat_final}")