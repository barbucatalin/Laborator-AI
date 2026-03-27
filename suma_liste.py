def sum_lists(l1, l2):
    result = [a + b for a, b in zip(l1, l2)]
    return result
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

result = sum_lists(list1, list2)

print(f"Lista 1: {list1}")
print(f"Lista 2: {list2}")
print(f"Rezultat: {result}")  