print("--- Generator Factură ---")
produs = input("Numele produsului: ")
cantitate = int(input("Cantitate: "))
pret_unitar = float(input("Preț unitar (fără TVA): "))


subtotal = cantitate * pret_unitar
tva = subtotal * 0.19
total_general = subtotal + tva


print("\n" + "="*30)
print(f"FACTURĂ FISCALĂ")
print("="*30)
print(f"Produs:     {produs}")
print(f"Cantitate:  {cantitate}")
print(f"Preț Unit:  {pret_unitar:.2f} RON")
print("-" * 30)
print(f"Subtotal:   {subtotal:.2f} RON")
print(f"TVA (19%):  {tva:.2f} RON")
print(f"TOTAL:      {total_general:.2f} RON")
print("="*30)