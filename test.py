import pandas as pd

# Load the temperature dataset
df_temp = pd.read_csv('data/calabar_temp_april2024.csv')

# Ensure 'date' column is in datetime format
df_temp['date'] = pd.to_datetime(df_temp['date'], errors='coerce')

# Filter for April 2024
df_temp_april = df_temp[
    (df_temp['date'] >= '2024-04-01') & (df_temp['date'] <= '2024-04-24')
]

# Drop any rows with missing dates or temperatures (optional but recommended)
df_temp_april = df_temp_april.dropna(subset=['date', 't2m'])

# Save the filtered dataset
df_temp_april.to_csv('data/filtered_calabar_temp_april2024.csv', index=False)

print("✅ Filtered temperature data saved to 'data/filtered_calabar_temp_april2024.csv'")
