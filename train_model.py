import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pickle

# Dummy dataset (aap apna dataset bhi use kar sakte ho)
data = {
    "year": [2015, 2016, 2017, 2018, 2019, 2020],
    "mileage": [20000, 30000, 25000, 40000, 35000, 50000],
    "price": [1500000, 1600000, 1700000, 1800000, 1750000, 2000000]
}

df = pd.DataFrame(data)

# Features & target
X = df[["year", "mileage"]]
y = df["price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Lasso regression
model = Lasso(alpha=0.1)
model.fit(X_train, y_train)

# Save model
with open("lasso_regression_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as lasso_regression_model.pkl")

