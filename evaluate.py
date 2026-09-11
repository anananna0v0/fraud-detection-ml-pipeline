import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix

# Load test data
df = pd.read_csv("data/processed/test.csv")

X_test = df.drop("Class", axis=1)
y_test = df["Class"]

# Load models
rf_model = joblib.load("models/model_rf.pkl")
xgb_model = joblib.load("models/model_xgb.pkl")

# Random Forest
rf_pred = rf_model.predict(X_test)

print("\n=== Random Forest ===")
print(classification_report(y_test, rf_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, rf_pred))

# XGBoost
xgb_pred = xgb_model.predict(X_test)

print("\n=== XGBoost ===")
print(classification_report(y_test, xgb_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, xgb_pred))