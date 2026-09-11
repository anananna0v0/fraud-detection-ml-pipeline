import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# Load training data
df = pd.read_csv("data/processed/train.csv")

X_train = df.drop("Class", axis=1)
y_train = df["Class"]

# Initialize model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# Train model
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/model_rf.pkl")

print("Random Forest training finished!")