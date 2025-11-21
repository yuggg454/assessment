import pandas as pd

# 1) Read the CSV file into a DataFrame called banks
banks = pd.read_csv("banklist.csv")
print("-----------------------------------------------------------")

# 2) Show the head of the dataframe
print(banks.head())
print("-----------------------------------------------------------")

# 3) What are the column names?
print(banks.columns.tolist())
print("-----------------------------------------------------------")

# 4) How many States (ST) are represented in this dataset?
num_states = banks['ST'].nunique()
print("Number of unique states:", num_states)
print("-----------------------------------------------------------")

# 5) Get a list or array of all the states in the dataset
states_list = banks['ST'].unique()
print("States represented:", states_list)
print("-----------------------------------------------------------")

# 6) What are the top 5 states with the most failed banks?
top5_states = banks['ST'].value_counts().head(5)
print("Top 5 states with most failed banks:\n", top5_states)
print("-----------------------------------------------------------")

# 7) What are the top 5 acquiring institutions?
top5_acquirers = banks['Acquiring Institution'].value_counts().head(5)
print("Top 5 acquiring institutions:\n", top5_acquirers)
print("-----------------------------------------------------------")

# 8) How many banks has the “State Bank of Texas” acquired? How many of them were actually in Texas?
acquired_by_sbot = banks[banks['Acquiring Institution'] == "State Bank of Texas"]
count_sbot = acquired_by_sbot.shape[0]
count_sbot_in_texas = acquired_by_sbot[acquired_by_sbot['ST'] == "TX"].shape[0]
print("Number of banks acquired by State Bank of Texas:", count_sbot)
print("Of those, how many were in Texas:", count_sbot_in_texas)
print("-----------------------------------------------------------")

# 9) What is the most common city in California for a bank to fail in?
ca_failures = banks[banks['ST'] == "CA"]
most_common_city_ca = ca_failures['City'].value_counts().idxmax()
print("Most common city in CA for bank failures:", most_common_city_ca)