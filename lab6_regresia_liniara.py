import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score



diabetes = load_diabetes()

X = diabetes.data
y = diabetes.target

df = pd.DataFrame(X, columns=diabetes.feature_names)
df["target"] = y

print("1. Setul de date Diabetes a fost încărcat.\n")



print("2. Primele 5 rânduri:")
print(df.head())
print()



print("3. Caracteristicile disponibile:")
print(diabetes.feature_names)
print()



print("4. Informații statistice:")
print(df.describe())
print()



plt.figure()
plt.hist(df["bmi"], bins=20)
plt.title("Histograma caracteristicii BMI")
plt.xlabel("BMI")
plt.ylabel("Frecvență")
plt.show()



plt.figure()
plt.scatter(df["bmi"], df["target"])
plt.title("BMI în funcție de target")
plt.xlabel("BMI")
plt.ylabel("Target")
plt.show()

plt.figure()
plt.scatter(df["age"], df["target"])
plt.title("Vârsta în funcție de target")
plt.xlabel("Age")
plt.ylabel("Target")
plt.show()





X_bmi = df[["bmi"]]
y = df["target"]


X_train, X_test, y_train, y_test = train_test_split(
    X_bmi, y, test_size=0.2, random_state=42
)


model_bmi = LinearRegression()
model_bmi.fit(X_train, y_train)


y_pred = model_bmi.predict(X_test)


plt.figure()
plt.scatter(X_test, y_test, label="Date reale")
plt.plot(X_test, y_pred, label="Linia de regresie")
plt.title("Regresie liniară simplă folosind BMI")
plt.xlabel("BMI")
plt.ylabel("Target")
plt.legend()
plt.show()


mse_bmi = mean_squared_error(y_test, y_pred)
print("7. Regresie liniară simplă folosind BMI")
print("Coeficient:", model_bmi.coef_[0])
print("Intercept:", model_bmi.intercept_)
print("MSE:", mse_bmi)
print()





X_bmi_bp = df[["bmi", "bp"]]
y = df["target"]


X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X_bmi_bp, y, test_size=0.2, random_state=42
)


model_bmi_bp = LinearRegression()
model_bmi_bp.fit(X_train2, y_train2)


y_pred2 = model_bmi_bp.predict(X_test2)


print("8. Regresie liniară folosind BMI și BP")
print("Coeficient pentru BMI:", model_bmi_bp.coef_[0])
print("Coeficient pentru BP:", model_bmi_bp.coef_[1])
print("Intercept:", model_bmi_bp.intercept_)


r2 = r2_score(y_test2, y_pred2)
print("R²:", r2)