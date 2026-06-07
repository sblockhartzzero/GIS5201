# Imports
# Imports
import ee
import geemap
import geemap.colormaps as cm
import geedim
import pandas as pd
import geopandas as gpd
import movingpandas as mpd
from shapely.geometry import Point
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import project_functions

# Set fullpath to csv file
input_csv_folder = 'C:/Users/s44ba/Documents/Training/Northeastern/AdvSpatialAnalysis/Project/Data/fromSeabirdTrackingNetwork/'
input_csv_filenames = ["Dataset_1044__Black-legged_Kittiwake_Grumant_GLS_2009_2010_2011.csv", 
                      "Dataset_1038__Black-legged_Kittiwake_Anda_GLS_2009_2010_2011.csv", 
                      "Dataset_1041__Black-legged_Kittiwake_Bulbjerg_GLS_2009_2010_2011.csv", 
                      "Dataset_1043__Black-legged_Kittiwake_Faroe_Islands_GLS_2009_2010.csv", 
                      "Dataset_1049__Black-legged_Kittiwake_Kippaku_GLS_2008_2009_2010_2011.csv"]

# Call functions
# Stops
# Specify speed range for stops
speed_min = 0.0
speed_max = 0.25
# Init df_list_stops
df_list_stops = []
# Loop through csv files, aggregating stops
for input_csv_filename in input_csv_filenames:
    # Get fullpath
    input_csv_fullpath = input_csv_folder + input_csv_filename
    # Get stops for this csv file
    print("Processing ", input_csv_fullpath)
    gdf_stops_temp =   project_functions.get_gdf_with_speed(input_csv_fullpath, speed_min=0, speed_max=0.25)
    # Append to list
    df_list_stops.append(gdf_stops_temp)
#endfor

# Concatenate
gdf_stops_combined = pd.concat(df_list_stops, ignore_index=True)

