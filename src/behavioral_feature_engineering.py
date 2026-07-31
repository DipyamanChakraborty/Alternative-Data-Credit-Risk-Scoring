import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load aggregated behavioral features
behavior_df = pd.read_csv("behavior_features.csv")

print("Shape:", behavior_df.shape)
print(behavior_df.head())

print("\nAverage transactions per segment:",
      behavior_df["total_transactions"].mean())

print("\nTop 5 most active segments:")
print(behavior_df.sort_values("total_transactions",ascending=False).head())

plt.figure()
sns.histplot(behavior_df["transaction_volatility"].dropna())
plt.title("Transaction Volatility Distribution")
plt.show()

plt.figure()
sns.histplot(behavior_df["weekend_ratio"])
plt.title("Weekend Transaction Ratio")
plt.show()

print("\nSegments with highest fraud ratio:")
print(behavior_df.sort_values("fraud_ratio",ascending=False).head())


print("\nTotal user segments:")
print(behavior_df.shape[0])

print("\nAverage fraud ratio:")
print(behavior_df["fraud_ratio"].mean())

print("\nAverage weekend ratio:")
print(behavior_df["weekend_ratio"].mean())