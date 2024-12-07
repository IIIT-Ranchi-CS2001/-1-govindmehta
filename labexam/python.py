import pandas as pd
import numpy as np

#reading the csv file
df = pd.read_csv('AQI_Data.csv')

#display the first 8 rows 
print("\nFirst 8 rows of the DataFrame:") 
print(df.head(8))

#display the last 5 rows 
print("\nLast 5 rows of the DataFrame:")
print(df.tail(5))

#display data types and non-null values for each column
print("\nDataFrame Info:")
print(df.info())

# Compute mean AQI, max PM2.5, and min PM10 values for each city
mean_aqi = df.groupby('City')['AQI'].mean()
max_pm25 = df.groupby('City')['PM2.5'].max()
min_pm10 = df.groupby('City')['PM10'].min()

print("\nMean AQI for each city:", mean_aqi)
print("\nMax PM2.5 for each city:", max_pm25)
print("\nMin PM10 for each city:", min_pm10)


#create pivot table showing maximum PM2.5 by city
pivot_table = pd.pivot_table(df, 
                           values='PM2.5',
                           index='City',
                           aggfunc='max')

print("\nMaximum PM2.5 levels by city:")
print(pivot_table)


#save pivot table to CSV file, overwrite if exists
pivot_table.to_csv('pivot.csv', mode='w')

