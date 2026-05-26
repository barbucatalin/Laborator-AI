import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score




iris = load_iris()

X = iris.data

df = pd.DataFrame(
    X,
    columns=iris.feature_names
)

print("1. Primele 5 rânduri:")
print(df.head())
print()

print("Shape dataset:", df.shape)
print()




scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("2. Primele 3 exemple standardizate:")
print(X_scaled[:3])
print()




kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

kmeans.fit(X_scaled)

clusters = kmeans.labels_

print("3. Etichetele clusterelor:")
print(clusters)
print()




print("4. Centrele clusterelor:")
print(kmeans.cluster_centers_)
print()




plt.figure(figsize=(8, 6))

plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=clusters
)

plt.title("K-Means Clustering - Iris Dataset")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.show()




inertii = []

K = range(1, 11)

for k in K:
    model = KMeans(
        n_clusters=k,
        random_state=42
    )

    model.fit(X_scaled)

    inertii.append(model.inertia_)

plt.figure(figsize=(8, 6))

plt.plot(K, inertii, marker='o')

plt.title("Metoda Elbow")
plt.xlabel("Număr clustere")
plt.ylabel("Inertia")

plt.show()



score = silhouette_score(
    X_scaled,
    clusters
)

print("7. Silhouette Score:", score)
print()




print("8. Clase reale:")
print(iris.target)
print()

print("Clustere prezise:")
print(clusters)
print()




floare_noua = [[5.1, 3.5, 1.4, 0.2]]

floare_scaled = scaler.transform(floare_noua)

cluster_nou = kmeans.predict(floare_scaled)

print("9. Cluster pentru floarea nouă:")
print(cluster_nou[0])