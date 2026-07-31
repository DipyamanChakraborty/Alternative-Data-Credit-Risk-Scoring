# ================================
# UPI DATA ANALYSIS - STEP 1
# ================================

import pandas as pd
import numpy as np

# -------------------------------
# 1. Load Dataset
# -------------------------------

print("Loading dataset...")

df = pd.read_csv("upi_transactions_2024.csv")

print("Dataset loaded successfully!")
print("Shape of dataset:", df.shape)

# -------------------------------
# 2. Clean Column Names
# -------------------------------

# Convert all column names to lowercase
df.columns = df.columns.str.strip().str.lower()

print("\nColumns in dataset:")
print(df.columns)

# -------------------------------
# 3. Basic Cleaning
# -------------------------------

# Convert amount column to numeric
df["amount (inr)"] = pd.to_numeric(df["amount (inr)"], errors="coerce")

# Drop rows where amount is missing
df = df.dropna(subset=["amount (inr)"])

print("\nShape after cleaning:", df.shape)

# -------------------------------
# 4. Create Synthetic User Segment
# -------------------------------

df["user_segment"] = (
    df["sender_bank"].astype(str) + "_" +
    df["sender_state"].astype(str) + "_" +
    df["sender_age_group"].astype(str)
)

print("\nNumber of unique user segments:",
      df["user_segment"].nunique())

# -------------------------------
# 5. Create Behavioral Features
# -------------------------------

behavior_df = df.groupby("user_segment").agg(
    total_transactions=("transaction id", "count"),
    avg_transaction_amount=("amount (inr)", "mean"),
    transaction_volatility=("amount (inr)", "std"),
    weekend_ratio=("is_weekend", "mean"),
    fraud_ratio=("fraud_flag", "mean"),
    merchant_diversity=("merchant_category", "nunique"),
    device_diversity=("device_type", "nunique")
).reset_index()

print("\nBehavior dataset created successfully!")
print("Behavior dataset shape:", behavior_df.shape)

print("\nSample of behavioral features:")
print(behavior_df.head())

# -------------------------------
# 6. Save Behavioral Features
# -------------------------------

behavior_df.to_csv("behavior_features.csv", index=False)

print("\nbehavior_features.csv saved successfully!")
print("STEP 1 COMPLETED ✅")
