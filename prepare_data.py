import pandas as pd
from sklearn.model_selection import train_test_split

# Load raw dataset
df = pd.read_csv("data/raw/creditcard.csv")

# Split into train and test sets
train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42,
    stratify=df["Class"]
)

# Save processed datasets
train_df.to_csv("data/processed/train.csv", index=False)
test_df.to_csv("data/processed/test.csv", index=False)

print("Data preparation finished!")
print(f"Train: {len(train_df)} rows")
print(f"Test: {len(test_df)} rows")