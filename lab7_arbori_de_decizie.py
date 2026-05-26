import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report




wine = load_wine()

X = wine.data
y = wine.target

df = pd.DataFrame(X, columns=wine.feature_names)

print("1. Primele 5 rânduri:")
print(df.head())
print()

print("Clase disponibile:")
print(wine.target_names)
print()

print("Shape dataset:", df.shape)
print()




X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("2. Shape train:", X_train.shape)
print("Shape test:", X_test.shape)
print()




tree_model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=4,
    random_state=42
)

tree_model.fit(X_train, y_train)

y_pred_tree = tree_model.predict(X_test)

acc_tree = accuracy_score(y_test, y_pred_tree)

print("3. Accuracy Decision Tree:", acc_tree)
print()




print("4. Matrice de confuzie:")
print(confusion_matrix(y_test, y_pred_tree))
print()

print("Classification Report:")
print(classification_report(y_test, y_pred_tree))
print()




plt.figure(figsize=(20, 10))

plot_tree(
    tree_model,
    filled=True,
    feature_names=wine.feature_names,
    class_names=wine.target_names
)

plt.title("Decision Tree - Wine Dataset")
plt.show()




forest_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

forest_model.fit(X_train, y_train)

y_pred_forest = forest_model.predict(X_test)

acc_forest = accuracy_score(y_test, y_pred_forest)

print("6. Accuracy Random Forest:", acc_forest)
print()




print("7. Comparare modele:")
print("Decision Tree Accuracy :", acc_tree)
print("Random Forest Accuracy :", acc_forest)
print()

if acc_forest > acc_tree:
    print("Random Forest oferă rezultate mai bune.")
elif acc_tree > acc_forest:
    print("Decision Tree oferă rezultate mai bune.")
else:
    print("Modelele au aceeași acuratețe.")




importance = forest_model.feature_importances_

importance_df = pd.DataFrame({
    "Caracteristica": wine.feature_names,
    "Importanta": importance
})

importance_df = importance_df.sort_values(
    by="Importanta",
    ascending=False
)

print()
print("8. Importanța caracteristicilor:")
print(importance_df)

plt.figure(figsize=(12, 6))

plt.bar(
    importance_df["Caracteristica"],
    importance_df["Importanta"]
)

plt.xticks(rotation=45)
plt.title("Importanța caracteristicilor")
plt.xlabel("Caracteristici")
plt.ylabel("Importanță")

plt.show()




exemplu_nou = [13.2, 2.7, 2.5, 18.0, 100.0,
               2.8, 3.0, 0.3, 1.5, 5.0,
               1.0, 3.0, 1000.0]

predictie = forest_model.predict([exemplu_nou])

print()
print("9. Predicție pentru exemplu nou:")
print("Clasa prezisă:", wine.target_names[predictie[0]])