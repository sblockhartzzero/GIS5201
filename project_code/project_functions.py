# Imports
import pandas as pd
import geopandas as gpd
import movingpandas as mpd
from shapely.geometry import Point
from datetime import datetime, timedelta
import numpy as np


def get_gdf_with_speed(input_csv_fullpath, speed_min, speed_max):

    # Read csv file into pandas dataframe
    df = pd.read_csv(input_csv_fullpath)

    # Convert to datetime
    # Add new column, derived timestamp_datetime, initialized to 1/1/1970
    df["timestamp_datetime"] = datetime(1970,1,1)
    # Add a copy of this column, to be used as an index
    df["timestamp_datetime_index"] =  df["timestamp_datetime"] 
    # Convert
    format_string = "%Y-%m-%d %H:%M:%S"
    for k in range(len(df)):
        date_string = df.loc[k,"date_gmt"]
        time_string = df.loc[k,"time_gmt"]
        datetime_string = date_string + ' ' + time_string
        df.loc[k,"timestamp_datetime"] = datetime.strptime(datetime_string,format_string)
        df.loc[k,"timestamp_datetime_index"] = datetime.strptime(datetime_string,format_string)
    #endfor

    # Fewer columns
    df_subset = df[['bird_id','timestamp_datetime_index','timestamp_datetime','longitude','latitude']]

    # Convert to geopandas
    geometry = gpd.points_from_xy(df_subset['longitude'],df_subset['latitude'])
    gdf_subset = gpd.GeoDataFrame(df_subset,geometry=geometry,crs="EPSG:4326")

    # Before converting to movingpandas, we need to set index to timestamp_datetime
    gdf_subset.set_index('timestamp_datetime_index')
    #print(gdf_subset.head())

    # Show unique bird ids
    unique_bird_ids = gdf_subset["bird_id"].unique()
    print(unique_bird_ids)

    # Convert to movingpandas trajectory collection 
    # Try trajectory collection
    tc = mpd.TrajectoryCollection(gdf_subset, "bird_id", t='timestamp_datetime_index')

    # Add speed
    tc.add_speed(overwrite=True)

    # Now that we have speed, convert back to geodataframe, where we can filter it more easily
    gdf_with_speed = tc.to_point_gdf()
    #print(gdf_with_speed.describe())

    # Filter gdf to get "stops"
    gdf_with_speed_filtered = gdf_with_speed[gdf_with_speed["speed"].between(speed_min,speed_max)]
    #print(gdf_with_speed_filtered.describe())
    #print(gdf_with_speed_filtered["bird_id"].unique())

    return gdf_with_speed_filtered








