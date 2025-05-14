# Climate & Air Quality Correlation in Calabar, Nigeria (April 2024)
## 🎯 Aim
To explore the relationship between temperature and fine particulate matter (PM1) to understand how climate variables may influence air quality in Calabar, Nigeria during April 2024.

## Objectives
- Extract daily average temperature from NetCDF files over a 1x1° grid around Calabar.
- Process air quality data (PM1) collected from Clarity sensors.
- Perform statistical analysis including Pearson correlation and covariance.
- Visualize the relationship using scatter plots and correlation matrices.

## 🧪 Methodology

1. Collected April 2024 temperature data (NetCDF processed to CSV) and PM1 air quality data.
2. Preprocessed both datasets (date formatting, filtering).
3. Merged data by matching dates.
4. Converted temperature from Kelvin to Celsius.
5. Visualized the relationship between temperature and PM1 levels.
6. Computed Pearson correlation.

## 📈 Results

A moderate **positive correlation** was observed between temperature and PM1 levels, suggesting warmer days may coincide with higher pollutant levels.

![Temperature vs PM1 Correlation](outputs/correlation_plot.png)

## 📊 Correlation Coefficient
 Weak positive correlation between temperature and PM1 (r ≈ 0.13)

## Tools Used
- Python (xarray, pandas, numpy, matplotlib, seaborn, scipy)
- Jupyter Notebook
- NetCDF climate datasets
- Air quality CSV data


## How to Run
1. Clone the repository
2. Place your data in the `data/` folder
3. Run the notebook in `notebooks/analysis.ipynb`


📌 *Note: This project contributes to early-stage research on environmental impacts on human health in West Africa.*

## 👤 Author

Toracee-tech  
Email: Ehijie Collins Agbadu  
GitHub: [github.com/collinsjie
Linkedin: https://www.linkedin.com/in/ehijie-agbadu-57732242/
