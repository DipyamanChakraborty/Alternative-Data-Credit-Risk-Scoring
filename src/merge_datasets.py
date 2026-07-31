import pandas as pd
import numpy as np

# Load credit dataset
credit_df = pd.read_csv("application_train.csv")

# Load behavioral dataset
behavior_df = pd.read_csv("behavior_features.csv")

print("Credit dataset shape:", credit_df.shape)
print("Behavior dataset shape:", behavior_df.shape)

np.random.seed(42)

credit_df["user_segment"] = np.random.choice(
    behavior_df["user_segment"],
    size=len(credit_df)
)

final_df = credit_df.merge(
    behavior_df,
    on="user_segment",
    how="left"
)

print("Final dataset shape:", final_df.shape)
print(final_df.head())

final_df.to_csv("final_dataset.csv", index=False)