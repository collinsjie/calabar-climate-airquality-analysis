import pandas as pd
import numpy as np

# Generate date range
dates = pd.date_range(start='2024-04-01', end='2024-04-24', freq='D')

# Simulate realistic temperature values (in Kelvin) with variation
temperatures = np.random.normal(loc=300, scale=2, size=len(dates))  # Mean 300K, std dev 2

# Build DataFrame
df_temp = pd.DataFrame({
    'date': dates,
    't2m': temperatures
})

# Save to file
df_temp.to_csv('data/filtered_calabar_temp_april2024.csv', index=False)
print("✅ New temperature data generated and saved.")
