
fructe = ["mere", "pere", "portocale"]


fructe.append("banane")
fructe.insert(1, "struguri") # Inserează la indexul 1


print("Al doilea fruct din listă:", fructe[1])
fructe[0] = "mere roșii"


fructe.sort()
print("Lista sortată alfabetic:", fructe)
print("Număr total de fructe:", len(fructe))


ultimul = fructe.pop()
print(f"Am scos '{ultimul}' din listă. Rămase: {fructe}")