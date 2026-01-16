# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv("delivery_data.csv")

X = df[["distance_km", "traffic_level", "weather"]]
y = df["delivery_time_min"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, "delivery_time_model.pkl")
print("ML model trained and saved")
