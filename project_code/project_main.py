# Imports
import project_functions

# Set fullpath to csv file
input_csv_folder = 'C:/Users/s44ba/Documents/Training/Northeastern/AdvSpatialAnalysis/Project/Data/fromSeabirdTrackingNetwork/'
input_csv_filename = 'Dataset_1044__Black-legged_Kittiwake_Grumant_GLS_2009_2010_2011.csv'
#input_csv_filename = 'Dataset_1038__Black-legged_Kittiwake_Anda_GLS_2009_2010_2011.csv'
#input_csv_filename = 'Dataset_1041__Black-legged_Kittiwake_Bulbjerg_GLS_2009_2010_2011.csv'
#input_csv_filename = 'Dataset_1043__Black-legged_Kittiwake_Faroe_Islands_GLS_2009_2010.csv'
#input_csv_filename = 'Dataset_1049__Black-legged_Kittiwake_Kippaku_GLS_2008_2009_2010_2011.csv'
input_csv_fullpath = input_csv_folder + input_csv_filename

# Call functions
speed_min = 0.0
speed_max = 1.0
gdf_stops = project_functions.get_gdf_with_speed(input_csv_fullpath, speed_min, speed_max)