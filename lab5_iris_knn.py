from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# =========================
# 1. Explorarea setului de date
# =========================

iris = load_iris()

X = iris.data
y = iris.target

print("=== 1. EXPLORAREA SETULUI DE DATE ===")
print("Numar de exemple:", X.shape[0])
print("Numar de caracteristici:", X.shape[1])
print("Forma datelor X:", X.shape)
print("Denumirile coloanelor:", iris.feature_names)
print("Numele claselor:", iris.target_names)

# =========================
# 2. Impartirea setului de date
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=None,
    stratify=y
)

print("\n=== 2. IMPARTIREA DATELOR ===")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# =========================
# 3. Preprocesarea datelor
# =========================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\n=== 3. STANDARDIZAREA DATELOR ===")
print("Primele 3 exemple inainte de scalare:")
print(X_train[:3])

print("\nPrimele 3 exemple dupa scalare:")
print(X_train_scaled[:3])

# =========================
# 4. Construirea si antrenarea modelului KNN
# =========================

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print("\n=== 4. MODEL KNN CU k = 3 ===")
print("Acuratete pe setul de testare:", accuracy)

# =========================
# 5. Impactul valorii k
# =========================

k_values = range(1, 16)
accuracies = []

for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)

    y_pred_k = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred_k)

    accuracies.append(acc)

print("\n=== 5. IMPACTUL VALORII k ===")
for k, acc in zip(k_values, accuracies):
    print(f"k = {k}, acuratete = {acc:.4f}")

best_accuracy = max(accuracies)
best_k = list(k_values)[accuracies.index(best_accuracy)]

print("\nCea mai buna valoare pentru k este:", best_k)
print("Acuratetea maxima obtinuta este:", round(best_accuracy, 4))
print("Interpretare: valoarea optima pentru k este cea care obtine cea mai mare acuratete.")
print("Un k mic poate fi sensibil la zgomot, iar un k prea mare poate generaliza prea mult.")

plt.figure(figsize=(8, 5))
plt.plot(k_values, accuracies, marker="o")
plt.title("Acuratetea modelului KNN in functie de k")
plt.xlabel("Valoarea lui k")
plt.ylabel("Acuratete")
plt.xticks(k_values)
plt.grid(True)
plt.show()

# =========================
# 6. Evaluarea modelului
# =========================

print("\n=== 6. EVALUAREA MODELULUI ===")

print("Matricea de confuzie:")
print(confusion_matrix(y_test, y_pred))

print("\nRaport complet de clasificare:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

print("Interpretare:")
print("Clasa Iris setosa este de obicei cel mai bine prezisa, deoarece este mai usor separabila.")
print("Clasele versicolor si virginica pot fi uneori confundate deoarece au valori apropiate ale petalelor.")

# =========================
# 7. Vizualizarea datelor
# =========================

print("\n=== 7. VIZUALIZAREA DATELOR ===")

petal_length = iris.data[:, 2]
petal_width = iris.data[:, 3]

plt.figure(figsize=(8, 5))
plt.scatter(petal_length, petal_width, c=y)
plt.title("Iris Dataset - Lungime petala vs Latime petala")
plt.xlabel("Lungime petala")
plt.ylabel("Latime petala")
plt.grid(True)
plt.show()

# =========================
# 7.2 Predictie pentru o floare noua
# =========================

print("\n=== 7.2 PREDICTIE PENTRU O FLOARE NOUA ===")

print("Introdu datele pentru o floare noua:")

sepal_length = float(input("Lungimea sepalei: "))
sepal_width = float(input("Latimea sepalei: "))
petal_length_input = float(input("Lungimea petalei: "))
petal_width_input = float(input("Latimea petalei: "))

new_flower = [[sepal_length, sepal_width, petal_length_input, petal_width_input]]

new_flower_scaled = scaler.transform(new_flower)
prediction = knn.predict(new_flower_scaled)

predicted_class = iris.target_names[prediction[0]]

print("Modelul prezice ca floarea este:", predicted_class)