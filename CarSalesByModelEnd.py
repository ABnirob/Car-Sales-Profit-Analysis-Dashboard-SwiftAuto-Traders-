# ============================================
# Car Sales Analysis - SwiftAuto Traders
# ============================================

import pandas as pd

# Load dataset
df = pd.read_excel("CarSalesByModelStart.xlsx")

# 1. Total quantity sold by Dealer ID (sorted descending)
dealer_qty = df.groupby("Dealer ID")["Quantity Sold"].sum().sort_values(ascending=False)

# 2. Total profit by Model (sorted ascending to see lowest first)
model_profit = df.groupby("Model")["Profit"].sum().sort_values()

# 3. Profit for Hudson model by Dealer ID (sorted descending)
hudson_profit = df[df["Model"] == "Hudson"].groupby("Dealer ID")["Profit"].sum().sort_values(ascending=False)

# Display results
print("=" * 50)
print("🔹 DEALER ID – TOTAL QUANTITY SOLD (Top first)")
print("=" * 50)
print(dealer_qty.head())
print("\n")

print("=" * 50)
print("🔹 MODEL – TOTAL PROFIT (Lowest first)")
print("=" * 50)
print(model_profit)
print("\n")

print("=" * 50)
print("🔹 HUDSON MODEL PROFIT BY DEALER ID (Highest first)")
print("=" * 50)
print(hudson_profit.head())