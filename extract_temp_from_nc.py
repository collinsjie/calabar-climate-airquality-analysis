# extract_temp_from_nc.py

import os
import xarray as xr
import pandas as pd

# Create data folder if not exists
os.makedirs('data', exist_ok=True)

# Load NetCDF file
ds = xr.open_dataset('calabar_temp_april2024.nc')

# Assign 'valid_time' as the main time coordinate (if needed)
if 'valid_time' in ds:
    ds = ds.rename({'valid_time': 'time'})

# Filter for April 2024
ds_april = ds.sel(time=slice('2024-04-01', '2024-04-30'))

# Select Calabar region (approx. 4° to 5° N, 8° to 9° E)
ds_subset = ds_april.sel(latitude=slice(5.0, 4.0), longitude=slice(8.0, 9.0))

# Resample to daily average temperature (Kelvin to Celsius)
daily_temp = ds_subset['t2m'].resample(time='1D').mean(dim=['latitude', 'longitude']) - 273.15

# Convert to DataFrame
df_temp = daily_temp.to_dataframe().reset_index()
df_temp = df_temp[['time', 't2m']].rename(columns={'time': 'date'})

# Save to CSV
df_temp.to_csv('data/calabar_temp_april2024.csv', index=False)

print("✅ Temperature data extracted and saved to 'data/calabar_temp_april2024.csv'")
