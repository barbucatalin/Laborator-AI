def normalizeaza():

    date = [10, 20, 30, 40, 50]

    i_min = min(date)
    i_max = max(date)

    print(f"Date originale: {date}")
    print(f"Min: {i_min}, Max: {i_max}\n")
    print("Valori normalizate:")

    for i in date:
      
        i_norm = (i - i_min) / (i_max - i_min)
        print(f"Valoarea {i} -> {i_norm:.2f}")


if __name__ == "__main__":
    normalizeaza()