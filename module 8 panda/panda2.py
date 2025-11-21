import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# ----------------------------------
# Load your single CSV file here
# ----------------------------------
df = pd.read_csv("historical_automobile_sales.csv")   # change file name if needed


# -------------------------------------------------
# Q1: LINE CHART — Year-wise Automobile Sales
# -------------------------------------------------
plt.figure(figsize=(10,5))
df.groupby("Year")["Automobile_Sales"].sum().plot(kind='line', marker='o')

plt.title("Total Automobile Sales by Year")
plt.xlabel("Year")
plt.ylabel("Automobile Sales")
plt.grid(True)
plt.show()


# -------------------------------------------------
# Q2: LINE CHART — Trend by Vehicle Type
# -------------------------------------------------
plt.figure(figsize=(12,6))

for vtype in df["Vehicle_Type"].unique():
    subset = df[df["Vehicle_Type"] == vtype]
    plt.plot(subset["Year"], subset["Automobile_Sales"], marker='o', label=vtype)

plt.title("Sales Trend by Vehicle Type Across Years")
plt.xlabel("Year")
plt.ylabel("Automobile Sales")
plt.legend()
plt.grid(True)
plt.show()


# -------------------------------------------------
# Q3: SEABORN BAR CHART — Recession vs Non-Recession
# -------------------------------------------------
plt.figure(figsize=(12,6))

sns.barplot(
    data=df,
    x="Vehicle_Type",
    y="Automobile_Sales",
    hue="Recession",
    estimator="mean"
)

plt.title("Average Sales per Vehicle Type (Recession vs Non-Recession)")
plt.xlabel("Vehicle Type")
plt.ylabel("Average Automobile Sales")
plt.show()


# -------------------------------------------------
# Q4: COMPARE SALES BY VEHICLE TYPE (AGGREGATED)
# -------------------------------------------------
plt.figure(figsize=(12,6))

grouped = df.groupby(["Recession", "Vehicle_Type"])["Automobile_Sales"].mean().reset_index()

sns.barplot(
    data=grouped,
    x="Vehicle_Type",
    y="Automobile_Sales",
    hue="Recession"
)

plt.title("Comparison of Sales by Vehicle Type (Recession vs Non-Recession)")
plt.xlabel("Vehicle Type")
plt.ylabel("Average Automobile Sales")
plt.show()