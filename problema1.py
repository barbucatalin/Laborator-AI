nota=float(input("Nota examen: " ))
nota_valida=list(range(1,11))

while nota not in nota_valida:
    nota=float(input("reintroduceti nota examen: " ))

if nota<5:
    print("reexaminare")
elif nota <= 6:
     (print("suficient"))
elif nota <=8:
    print("bine")
else :
     print("excelent")