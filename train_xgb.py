import pandas as pd
import joblib
from xgboost import XGBClassifier

# Load training data
df = pd.read_csv("data/processed/train.csv")

X_train = df.drop("Class", axis=1)
y_train = df["Class"]

# Initialize model
model = XGBClassifier(
    n_estimators=100,
    random_state=42,
    eval_metric="logloss"
)

# Train model
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/model_xgb.pkl")

print("XGBoost training finished!")