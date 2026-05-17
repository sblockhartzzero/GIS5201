
"""
Probe data from Seabird Tracking Database, demonstrating how to use movingpandas to get speed

To do:
-Verify conversion to geopandas
-What is units of speed?
-Plot of mpd trajectory, color-coded by speed

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

# Convert to datetime
# Add new column, derived timestamp_datetime, initialized to 1/1/1970
df["timestamp_datetime"] = datetime(1970,1,1)
# Convert
format_string = "%Y-%m-%d %H:%M:%S"
for k in range(len(df)):
    date_string = df.loc[k,"date_gmt"]
    time_string = df.loc[k,"time_gmt"]
    datetime_string = date_string + ' ' + time_string
    df.loc[k,"timestamp_datetime"] = datetime.strptime(datetime_string,format_string)
#endfor

# Fewer columns
df_subset = df[['bird_id','timestamp_datetime','longitude','latitude']]

# Convert to geopandas
geometry = gpd.points_from_xy(df_subset['longitude'],df_subset['latitude'])
gdf_subset = gpd.GeoDataFrame(df_subset,geometry=geometry,crs="EPSG:4326")

# Before converting to movingpandas, we need to set index to timestamp_datetime
gdf_subset.set_index('timestamp_datetime')
print(gdf_subset.head())

# Convert to movingpandas
traj = mpd.Trajectory(gdf_subset,this_bird_id, traj_id_col='bird_id', t='timestamp_datetime')
traj.add_speed(overwrite=True)
print(traj.df.describe())

# Plot
ax2 = plt.plot(traj.df['speed'])
plt.show()