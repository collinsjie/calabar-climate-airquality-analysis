import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# File paths
temp_file = 'data/filtered_calabar_temp_april2024.csv'
air_file = 'data/calabar_air_april2024.csv'
output_file = 'outputs/merged_calabar_april2024.csv'

def load_data(temp_path, air_path):
    df_temp = pd.read_csv(temp_path, parse_dates=['date'])
    df_air = pd.read_csv(air_path, parse_dates=['date', 'datetimeLocal'])
    return df_temp, df_air

def preprocess_data(df_temp, df_air):
    print(f"✅ Temperature file columns: {df_temp.columns.tolist()}")
    print(f"✅ Air quality file columns: {df_air.columns.tolist()}")

    print(f"📅 Temp date range: {df_temp['date'].min()} to {df_temp['date'].max()}")
    print(f"📅 Air date range: {df_air['date'].min()} to {df_air['date'].max()}")

    # Convert temperature from Kelvin to Celsius
    df_temp['t2m'] = df_temp['t2m'] - 273.15

    # Strip time to keep only the date
    df_temp['date'] = df_temp['date'].dt.date
    df_air['date'] = df_air['date'].dt.date

    # Group air quality by date and calculate average value
    df_air_daily = df_air.groupby('date')['value'].mean().reset_index()

    # Merge datasets on 'date'
    df_merged = pd.merge(df_temp, df_air_daily, on='date', how='inner')

    return df_merged

# Load merged data
df = pd.read_csv("outputs/merged_calabar_april2024.csv", parse_dates=["date"])

# Compute correlation
correlation = df["t2m"].corr(df["value"])
print(f"📊 Correlation between Temperature and PM1: {correlation:.3f}")

# Plot temperature and PM1 values
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="date", y="t2m", label="Temperature (°C)", marker="o")
sns.lineplot(data=df, x="date", y="value", label="PM1 Value", marker="s")
plt.title("Temperature vs PM1 Air Quality in Calabar (April 2024)")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig("outputs/temp_vs_pm1_plot.png")
plt.show()

def main():
    df_temp, df_air = load_data(temp_file, air_file)
    df = preprocess_data(df_temp, df_air)

    if df.empty:
        print("❌ Merged dataset is empty. Check for matching dates.")
    else:
        print(f"✅ Merged dataset shape: {df.shape}")
        print("📊 Sample rows:\n", df.head())
        df.to_csv(output_file, index=False)
        print(f"💾 Merged data saved to '{output_file}'")

if __name__ == "__main__":
    main()
