import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("finance_economics_dataset.csv")
df["Date"] = pd.to_datetime(df["Date"])

def find_outliers(col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return df[(df[col] < lower) | (df[col] > upper)]

print("\n=== 1. SHAPE OF DATASET ===")
print(df.shape)
print("Summary: Dataset contains", df.shape[0], "rows and", df.shape[1], "columns.\n")

print("\n=== 2. COLUMN NAMES & DATA TYPES ===")
print(df.dtypes)
print("Summary: Dataset contains numeric, object, and datetime columns.\n")

print("\n=== 3. UNIQUE STOCK INDICES ===")
print(df["Stock Index"].nunique())
print("Summary: Three unique indices (S&P 500, NASDAQ, Dow Jones).\n")

print("\n=== 4. DATE RANGE ===")
print(df["Date"].min(), "to", df["Date"].max())
print("Summary: Data spans from 2000 to early 2008.\n")

print("\n=== 5. MISSING VALUES ===")
print(df.isna().sum())
print("Summary: No missing values detected.\n")

print("\n=== 6. NEGATIVE VALUES IN NON-NEGATIVE COLUMNS ===")
negatives = df.select_dtypes(include=np.number).lt(0).any()
print(negatives)
print("Summary: GDP may contain negatives, others mostly non-negative.\n")

print("\n=== 7. SUMMARY OF GDP GROWTH (%) ===")
print(df["GDP Growth (%)"].describe())
print("Summary: GDP ranges from -5% to 10%, avg ~5%.\n")

print("\n=== 8. ZERO OR NEAR-ZERO TRADING VOLUME ===")
print((df["Trading Volume"] <= 1).sum())
print("Summary: No zero-volume rows.\n")

print("\n=== 9. DUPLICATE ROWS ===")
print(df.duplicated().sum())
print("Summary: No duplicates found.\n")

print("\n=== 10. OUTLIERS (GDP, GOLD, OIL) ===")
print("GDP outliers:", len(find_outliers("GDP Growth (%)")))
print("Gold outliers:", len(find_outliers("Gold Price (USD per Ounce)")))
print("Oil outliers:", len(find_outliers("Crude Oil Price (USD per Barrel)")))
print("Summary: Moderate outliers present in all three.\n")

print("\n=== 11. SUMMARY INFLATION RATE (%) ===")
print(df["Inflation Rate (%)"].describe())
print("Summary: Inflation ranges from 0.5% to 10%.\n")

print("\n=== 12. AVERAGE UNEMPLOYMENT RATE ===")
print(df["Unemployment Rate (%)"].mean())
print("Summary: Mean unemployment is ~8.66%.\n")

print("\n=== 13. INDEX WITH HIGHEST TRADING VOLUME ===")
print(df.groupby("Stock Index")["Trading Volume"].mean().idxmax())
print("Summary: S&P 500 has highest average volume.\n")

print("\n=== 14. RECORD COUNT PER INDEX ===")
print(df["Stock Index"].value_counts())
print("Summary: Slight variation in number of entries.\n")

print("\n=== 15. CORRELATION: INFLATION VS INTEREST RATE ===")
print(df[["Inflation Rate (%)", "Interest Rate (%)"]].corr().iloc[0,1])
print("Summary: Almost zero correlation.\n")

print("\n=== 16. AVERAGE CONSUMER CONFIDENCE INDEX ===")
print(df["Consumer Confidence Index"].mean())
print("Summary: Avg confidence is ~85.\n")

print("\n=== 17. COLUMN WITH HIGHEST STANDARD DEVIATION ===")
print(df.std(numeric_only=True).idxmax())
print("Summary: Trading Volume is most volatile.\n")

print("\n=== 18. HIGHEST GOLD PRICE ===")
print(df["Gold Price (USD per Ounce)"].max())
print("Summary: Highest gold price ~2500 USD.\n")

print("\n=== 19. DATE OF HIGHEST OIL PRICE ===")
oil_idx = df["Crude Oil Price (USD per Barrel)"].idxmax()
print(df.loc[oil_idx, "Date"])
print("Summary: Oil peak was in late 2001.\n")

print("\n=== 20. AVERAGE CORPORATE PROFIT ===")
print(df["Corporate Profits (Billion USD)"].mean())
print("Summary: Avg corporate profits ~2553B USD.\n")

# =========================================================

print("\n========== INSIGHT ANALYSIS ==========\n")

print("\n1. % OF NEGATIVE GDP GROWTH:")
print((df["GDP Growth (%)"] < 0).mean() * 100)

print("\n2. INFLATION vs INTEREST RATE CORRELATION:")
print(df[["Inflation Rate (%)", "Interest Rate (%)"]].corr().iloc[0,1])

print("\n3. UNEMPLOYMENT vs CONSUMER SPENDING:")
print(df[["Unemployment Rate (%)", "Consumer Spending (Billion USD)"]].corr().iloc[0,1])

print("\n4. CORPORATE PROFITS vs CONSUMER CONFIDENCE:")
print(df[["Corporate Profits (Billion USD)", "Consumer Confidence Index"]].corr().iloc[0,1])

print("\n5. OIL PRICE TREND PLOT:")
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Crude Oil Price (USD per Barrel)"], color="orange")
plt.title("Crude Oil Price Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Oil Price")
plt.grid(True)
plt.show()

print("\n6. GOLD PRICE vs STOCK CLOSE PRICE CORRELATION:")
print(df[["Gold Price (USD per Ounce)", "Close Price"]].corr().iloc[0,1])

print("\n7. GOVERNMENT DEBT vs CONSUMER CONFIDENCE:")
print(df[["Government Debt (Billion USD)", "Consumer Confidence Index"]].corr().iloc[0,1])

print("\n8. M&A DEALS vs STOCK CLOSING PRICE:")
print(df[["Mergers & Acquisitions Deals", "Close Price"]].corr().iloc[0,1])

print("\n9. RETAIL SALES vs GDP GROWTH:")
print(df[["Retail Sales (Billion USD)", "GDP Growth (%)"]].corr().iloc[0,1])

print("\n10. STOCK PRICE vs CONSUMER SPENDING:")
print(df[["Close Price", "Consumer Spending (Billion USD)"]].corr().iloc[0,1])

print("\n11. HIGHEST AVG CLOSING PRICE INDEX:")
print(df.groupby("Stock Index")["Close Price"].mean().idxmax())

print("\n12. INTEREST RATE vs UNEMPLOYMENT CORRELATION:")
print(df[["Interest Rate (%)", "Unemployment Rate (%)"]].corr().iloc[0,1])

print("\n13. CONSUMER CONFIDENCE vs BANKRUPTCY RATE:")
print(df[["Consumer Confidence Index", "Bankruptcy Rate (%)"]].corr().iloc[0,1])

print("\n14. FEATURE MOST CORRELATED WITH STOCK CLOSE PRICE:")
corrs = df.corr(numeric_only=True)["Close Price"].drop("Close Price").abs()
print(corrs.idxmax())

print("\n15. CORPORATE PROFITS vs UNEMPLOYMENT:")
print(df[["Corporate Profits (Billion USD)", "Unemployment Rate (%)"]].corr().iloc[0,1])

print("\n\n=== END OF ANALYSIS ===")