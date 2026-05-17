
"""
Probe data from Seabird Tracking Database, demonstrating how to use movingpandas to get speed

To do:
-Combine date, time fileds into a timestamp
-Convert to geopandas/movingpandas to get speed per data point, per track

"""
# Imports
import numpy as np
import pandas as pd
import geopandas as gpd
import movingpandas as mpd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Specify fullpath to csv
# i.e. csv downloaded from Seabird Tracking Database
input_csv_folder = 'C:/Users/s44ba/Documents/Training/Northeastern/AdvSpatialAnalysis/Project/Data/fromSeabirdTrackingNetwork/'
input_csv_filename = 'Dataset_1044__Black-legged_Kittiwake_Grumant_GLS_2009_2010_2011.csv'
input_csv_fullpath = input_csv_folder + input_csv_filename
df = pd.read_csv(input_csv_fullpath)
df.info()

# Show unique bird ids
unique_bird_ids = df["bird_id"].unique()
print(unique_bird_ids)

# group by bird id
grouped_df = df.groupby('bird_id')
grouped_df.describe()

# Look at a single bird's track(s)
this_bird_id = 8840
these_tracks = df[df['bird_id']==this_bird_id]

# Extract arrays 
df_lat = these_tracks['latitude']
df_lon = these_tracks['longitude']

# Convert to numpy
lat_array = np.array(df_lat)
lon_array = np.array(df_lon)

# Plot
ax1 = plt.plot(lon_array,lat_array)
plt.show()