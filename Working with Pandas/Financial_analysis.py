import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("finance_economics_dataset.csv")
df["Date"] = pd.to_datetime(df["Date"])

def detect_outliers(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return df[(df[column] < lower) | (df[column] > upper)]

# 1. Shape of dataset
print("\n1. Shape:", df.shape)

# ---------------------------------------------------------
# 2. Column names & data types
print("\n2. Dtypes:\n", df.dtypes)

# ---------------------------------------------------------
# 3. Unique stock indices
print("\n3. Number of indices:", df["Stock Index"].nunique())

# ---------------------------------------------------------
# 4. Date range
print("\n4. Date range:", df["Date"].min(), "to", df["Date"].max())

# ---------------------------------------------------------
# 5. Missing values
print("\n5. Missing values:\n", df.isna().sum())

# ---------------------------------------------------------
# 6. Negative values where not expected
print("\n6. Columns with negative values:\n", df.select_dtypes(include=np.number).lt(0).any())

# ---------------------------------------------------------
# 7. Summary of GDP Growth
print("\n7. GDP summary:\n", df["GDP Growth (%)"].describe())

# ---------------------------------------------------------
# 8. Zero or near-zero volume
print("\n8. Zero/near-zero volume count:", (df["Trading Volume"] <= 1).sum())

# ---------------------------------------------------------
# 9. Duplicate rows
print("\n9. Duplicate rows:", df.duplicated().sum())

# ---------------------------------------------------------
# 10. Outliers
print("\n10. Outliers:")
print("GDP:", len(detect_outliers("GDP Growth (%)")))
print("Gold:", len(detect_outliers("Gold Price (USD per Ounce)")))
print("Oil:", len(detect_outliers("Crude Oil Price (USD per Barrel)")))

# ---------------------------------------------------------
# 11. Inflation rate summary
print("\n11. Inflation summary:\n", df["Inflation Rate (%)"].describe())

# ---------------------------------------------------------
# 12. Average unemployment
print("\n12. Avg Unemployment:", df["Unemployment Rate (%)"].mean())

# ---------------------------------------------------------
# 13. Index with highest avg volume
print("\n13. Highest volume index:", df.groupby("Stock Index")["Trading Volume"].mean().idxmax())

# ---------------------------------------------------------
# 14. Records per index
print("\n14. Records per index:\n", df["Stock Index"].value_counts())

# ---------------------------------------------------------
# 15. Correlation: inflation vs interest
print(
    "\n15. Inflation vs Interest correlation:",
    df[["Inflation Rate (%)", "Interest Rate (%)"]].corr().iloc[0, 1],
)

# ---------------------------------------------------------
# 16. Average consumer confidence
print("\n16. Avg Consumer Confidence:", df["Consumer Confidence Index"].mean())

# ---------------------------------------------------------
# 17. Column with highest std deviation
print("\n17. Highest STD Column:", df.std(numeric_only=True).idxmax())

# ---------------------------------------------------------
# 18. Highest gold price
print("\n18. Max gold price:", df["Gold Price (USD per Ounce)"].max())

# ---------------------------------------------------------
# 19. Date of highest oil price
idx = df["Crude Oil Price (USD per Barrel)"].idxmax()
print("\n19. Highest oil price date:", df.loc[idx, "Date"])

# ---------------------------------------------------------
# 20. Average corporate profit
print("\n20. Avg Corporate Profit:", df["Corporate Profits (Billion USD)"].mean())

print("\n---------------- INSIGHT ANALYSIS ----------------")

# 1. % negative GDP growth
print(
    "\n1. % Negative GDP:",
    (df["GDP Growth (%)"] < 0).mean() * 100,
)

# 2. Inflation vs interest
print(
    "\n2. Inflation-Interest correlation:",
    df[["Inflation Rate (%)", "Interest Rate (%)"]].corr().iloc[0, 1],
)

# 3. Unemployment vs consumer spending
print(
    "\n3. Unemployment vs Spending correlation:",
    df[["Unemployment Rate (%)", "Consumer Spending (Billion USD)"]].corr().iloc[0, 1],
)

# 4. Corporate profit vs consumer confidence
print(
    "\n4. Profit vs Confidence correlation:",
    df[["Corporate Profits (Billion USD)", "Consumer Confidence Index"]]
    .corr()
    .iloc[0, 1],
)

# 5. Oil price trend plot
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Crude Oil Price (USD per Barrel)"], color="orange")
plt.title("Crude Oil Price Trend")
plt.xlabel("Date")
plt.ylabel("Oil Price")
plt.grid()
plt.show()

# 6. Gold vs stock
print(
    "\n6. Gold vs Stock correlation:",
    df[["Gold Price (USD per Ounce)", "Close Price"]].corr().iloc[0, 1],
)

# 7. Government debt vs confidence
print(
    "\n7. Debt vs Confidence correlation:",
    df[["Government Debt (Billion USD)", "Consumer Confidence Index"]]
    .corr()
    .iloc[0, 1],
)

# 8. M&A vs close price
print(
    "\n8. M&A vs Close correlation:",
    df[["Mergers & Acquisitions Deals", "Close Price"]].corr().iloc[0, 1],
)

# 9. Retail sales vs GDP
print(
    "\n9. Retail vs GDP correlation:",
    df[["Retail Sales (Billion USD)", "GDP Growth (%)"]].corr().iloc[0, 1],
)

# 10. Stock vs consumer spending
print(
    "\n10. Stock vs Spending correlation:",
    df[["Close Price", "Consumer Spending (Billion USD)"]].corr().iloc[0, 1],
)

# 11. Highest avg closing price index
print("\n11. Highest average close index:", df.groupby("Stock Index")["Close Price"].mean().idxmax())

# 12. Interest vs unemployment
print(
    "\n12. Interest vs Unemployment correlation:",
    df[["Interest Rate (%)", "Unemployment Rate (%)"]].corr().iloc[0, 1],
)

# 13. Consumer confidence vs bankruptcy
print(
    "\n13. Confidence vs Bankruptcy correlation:",
    df[["Consumer Confidence Index", "Bankruptcy Rate (%)"]].corr().iloc[0, 1],
)

# 14. Highest correlated indicator with Close Price
corrs = df.corr(numeric_only=True)["Close Price"].drop("Close Price").abs()
print("\n14. Highest correlation with Close Price:", corrs.idxmax())

# 15. Corporate profit vs unemployment
print(
    "\n15. Profit vs Unemployment correlation:",
    df[["Corporate Profits (Billion USD)", "Unemployment Rate (%)"]].corr().iloc[0, 1],
)
