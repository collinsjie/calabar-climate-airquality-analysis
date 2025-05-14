import pandas as pd

df = pd.read_csv('data/filtered_calabar_temp_april2024.csv')
print("🔍 Columns:", df.columns.tolist())
print("\n🧪 Sample rows:")
print(df.head())

# Try parsing the 'date' column
try:
    df['date'] = pd.to_datetime(df['date'])
    print("\n✅ Date column parsed successfully.")
    print("📅 Date range:", df['date'].min(), "to", df['date'].max())
except Exception as e:
    print("\n❌ Error parsing 'date' column:", e)
